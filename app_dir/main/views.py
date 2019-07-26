from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import *
from .models import *
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
import requests
from app_dir.main import function_writer, block_generator
from app_dir.main.generated_functions import *


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
    mailBoxlen = mailboxes.count()
    if (mailBoxlen) > 0:
        last_mailbox = mailboxes[mailBoxlen - 1]
        read_mailbox = open('last_mailbox.txt', 'r')
        mailbox_a = read_mailbox.read()
        read_mailbox.close()
        mailbox_name = last_mailbox.name
        mailbox_tag = last_mailbox.api
        print(mailbox_tag)
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
        api_tag = api_name
        api_name = api_name.replace(".", "_")
        if int(api_a) < last_api['id']:
            write_file = open('last_api.txt', 'w+')
            write_file.write(str(last_api['id']))
            write_file.close()
            function_writer.api_function_writer(api_name, api_tag)
            block_generator.block_generator(api_name, 'api')

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


import ast
import copy


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
    else:
        return HttpResponse('Use ajax format!')

    return JsonResponse({'code': result})
