from django.contrib.auth import forms
from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import *
from .models import *
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
import requests
from app_dir.main import function_writer, block_generator
from app_dir.main.generated_functions import *
import ast
import copy

from django.views.generic import CreateView


def new_form(request):
    return render(request, 'forms.html')


def save_form(request):
    if request.method == "POST":
        print(request.POST['myfile'])
        data = Label(request.POST['myfile'])

        context = {'bank': data}
        print(context['bank'][0])
        return render(request, 'result.html', context)


# class MyForm(forms.ModelForm):  # Note that it is not inheriting from forms.ModelForm
#     a = forms.CharField(max_length=20)
#     # All my attributes here
#
#
# def form_handle(request):
#     form = MyForm()
#     if request.method == 'POST':
#         form = MyForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             # now in the object cd, you have the form as a dictionary.
#             a = cd.get('a')
#
#     # blah blah encode parameters for a url blah blah
#     # and make another post request
#     # edit : added ": "  after    if request.method=='POST'
#

def home(request):
    # Sensor and Actuators Creator
    all_service = requests.get("http://127.0.0.1:8000/api/service_registry/").json()
    if len(all_service) > 0:
        last_service = all_service[-1]
        read_file = open('last_sensor_actuator.txt', 'r')
        a = read_file.read()
        read_file.close()
        name_id = last_service['name']
        sensor_tag = name_id
        name_id = name_id.replace(".", "_")

        if int(a) < last_service['id']:
            write_file = open('last_sensor_actuator.txt', 'w+')
            write_file.write(str(last_service['id']))
            write_file.close()
            if last_service['service_type'] == 'sensor':
                function_writer.sensor_function_writer(name_id, sensor_tag)
                block_generator.block_generator(name_id, last_service['service_type'])

            elif last_service['service_type'] == 'actuator':
                function_writer.actuator_function_writer(name_id, sensor_tag)
                block_generator.block_generator(name_id, last_service['service_type'])
                url = 'http://127.0.0.1:8000/api/actuators/'
                data = {
                    "topic": name_id,
                    "value": "null",
                    "time": "null",
                    "name": "1"
                }
                requests.post(url, data=data)

    # MailBox Creator
    mailboxes = MailBox.objects.all()
    mailbox_len = mailboxes.count()
    if mailbox_len > 0:
        last_mailbox = mailboxes[mailbox_len - 1]
        read_mailbox = open('last_mailbox.txt', 'r')
        mailbox_a = read_mailbox.read()
        read_mailbox.close()
        mailbox_name = last_mailbox.name
        mailbox_tag = last_mailbox.api
        mailbox_name = mailbox_name.replace(".", "_")
        if int(mailbox_a) < last_mailbox.id:
            write_file = open('last_mailbox.txt', 'w+')
            write_file.write(str(last_mailbox.id))
            write_file.close()
            function_writer.mailbox_function_writer(mailbox_name, mailbox_tag.name)
            block_generator.block_generator(mailbox_name, 'mailbox')

    # API Creator
    api = requests.get("http://127.0.0.1:8000/api/api/").json()
    if len(api) > 0:
        last_api = api[-1]
        read_api = open('last_api.txt', 'r')
        api_a = read_api.read()
        read_api.close()
        api_name = last_api['name']
        api_link = last_api['api']
        api_fields = last_api['fields']
        api_connection = last_api['connection']
        api_name = api_name.replace(".", "_")
        if int(api_a) < last_api['id']:
            write_file = open('last_api.txt', 'w+')
            write_file.write(str(last_api['id']))
            write_file.close()
            function_writer.api_function_writer(api_name, api_link, api_fields)
            block_generator.api_block_generator(api_name, 'api', api_fields, api_connection)

    # Interactive Creator
    interactive = requests.get("http://127.0.0.1:8000/api/interactive/").json()
    if len(interactive) > 0:
        last_interactive = interactive[-1]
        read_interactive = open('last_interactive.txt', 'r')
        interactive_a = read_interactive.read()
        read_interactive.close()
        interactive_name = last_interactive['name']
        interactive_fields = last_interactive['fields']
        print(interactive_fields)
        interactive_name = interactive_name.replace(".", "_")
        if int(interactive_a) < last_interactive['id']:
            write_file = open('last_interactive.txt', 'w+')
            write_file.write(str(last_interactive['id']))
            write_file.close()
            function_writer.interactive_function_writer(interactive_name, interactive_fields)
            block_generator.interactive_block_generator(interactive_name, 'interactive', interactive_fields)

    return render(request, 'index.html')


class ActuatorAPI(viewsets.ModelViewSet):
    queryset = Actuator.objects.all()
    serializer_class = ActuatorSerializer


class SensorAPI(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class ServiceRegistryAPI(viewsets.ModelViewSet):
    queryset = ServiceRegistry.objects.all()
    serializer_class = ServiceRegistrySerializer


class MailBoxAPI(viewsets.ModelViewSet):
    queryset = MailBox.objects.all()
    serializer_class = MailBoxSerializer


class APInterfaceAPI(viewsets.ModelViewSet):
    queryset = API.objects.all()
    serializer_class = APISerializer


class InteractiveAPI(viewsets.ModelViewSet):
    queryset = Interactive.objects.all()
    serializer_class = InteractiveSerializer


class ActuatorListApiView(generics.ListAPIView):
    serializer_class = ActuatorSerializer

    def get_queryset(self):
        qs = Actuator.objects.all()
        query = self.request.GET.get("q")

        if query is not None:
            qs = qs.filter(
                Q(topic__icontains=query)
            ).distinct().order_by('-time')[:1]

        return qs


def convertExpr2Expression(Expr):
    Expr.lineno = 0
    Expr.col_offset = 0
    result = ast.Expression(Expr.value, lineno=0, col_offset=0)

    return result


def exec_with_return(code):
    code_ast = ast.parse(code)

    init_ast = copy.deepcopy(code_ast)
    init_ast.body = code_ast.body[:-1]

    last_ast = copy.deepcopy(code_ast)
    last_ast.body = code_ast.body[-1:]

    exec(compile(init_ast, "<ast>", "exec"), globals())
    if type(last_ast.body[0]) == ast.Expr:
        return eval(compile(convertExpr2Expression(last_ast.body[0]), "<ast>", "eval"), globals())
    else:
        exec(compile(last_ast, "<ast>", "exec"), globals())


def get_motor_status(request):
    if request.is_ajax():
        code = request.POST['code']

        result = exec_with_return(code)
        print(result)
    else:
        return HttpResponse('Use ajax format!')

    return JsonResponse({'code': result})
