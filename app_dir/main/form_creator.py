def api_form_creator(function_name, api_fields):
    fields = ""
    result = api_fields.split(',')
    res_len = len(result)
    c = 0
    for i in result:
        is_there_data = i.split('=')
        if len(is_there_data) > 1:
            c = c + 1
    param_should = res_len - c
    parameter = ""
    parameter_val = "param"
    post_value = ""
    declare_var = ""
    for p in range(param_should):
        fields += "<input class='form-control' type='text' name='param" + str(p) + "' id='param" + str(
            p) + function_name + "' value=''/>"
        parameter += parameter_val + str(p) + ','
        post_value += "'param" + str(p) + "': param" + str(p) + ","
        declare_var += "var param" + str(p) + " = $('#param" + str(p) + function_name + "').val();"
    final_param = parameter.rstrip(',')
    fina_post_value = post_value.rstrip((','))
    headers = "headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()},"
    form_file = open("app_dir/main/forms.py", "a+")
    form = """\n\n
def """ + function_name + """(""" + final_param + """):
    code = "<h1>""" + function_name + """</h1><button class='btn btn-primary' onclick='""" + function_name + """()'>Run</button><button class='btn btn-info' onclick='continuous""" + function_name + """()'>Run Continuously</button><button class='btn btn-danger' onclick='stop""" + function_name + """()'>Stop Continuous Run</button><form enctype='multipart/form-data' action='' method='post'>{% csrf_token %}""" + fields + """</form><script>function """ + function_name + """(){""" + declare_var + """ $.ajax({type: 'POST',url: '/""" + function_name + """/',""" + headers + """data: {""" + fina_post_value + """},success: function (response) {console.log(response.code);document.getElementById('""" + function_name + """_result').innerHTML = JSON.stringify(response.code, undefined,2);}});}var myVar;function continuous""" + function_name + """(){""" + declare_var + """ $.ajax({type: 'POST',url: '/""" + function_name + """/',""" + headers + """data: {""" + fina_post_value + """},success: function (response) {console.log(response.code);document.getElementById('""" + function_name + """_result').innerHTML = JSON.stringify(response.code, undefined,2);}});myVar""" + function_name + """ = setTimeout('continuous""" + function_name + """()', 100);}function stop""" + function_name + """() {clearTimeout(myVar""" + function_name + """);}</script><pre style='width: 100%; height:100px' id='""" + function_name + """_result'></pre><script>function """ + function_name + """() {var param0 = $('#param0""" + function_name + """').val();$.ajax({type: 'POST',url: '/""" + function_name + """/',""" + headers + """data: {'param0': param0},success: function (response) {console.log(response.code);document.getElementById('""" + function_name + """_result').innerHTML = JSON.stringify(response.code, undefined, 2);});}</script>"
    return code
    """
    form_file.write(form)
    form_file.close()


def url_creator(function_name):
    f = open("app_dir/main/urls.py", "r")
    contents = f.readlines()
    f.close()

    url = """
path('""" + function_name + """/', post_functions.""" + function_name + """, name='""" + function_name + """'),"""
    contents.insert(22, url)

    f = open("app_dir/main/urls.py", "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()


def post_function_creator(function_name, api_link, api_fields):
    result = api_fields.split(',')
    res_len = len(result)
    c = 0
    for i in result:
        is_there_data = i.split('=')
        if len(is_there_data) > 1:
            c = c + 1
    param_should = res_len - c
    parameter = ""
    parameter_val = "param"
    for p in range(param_should):
        parameter += parameter_val + str(p) + ','
    final_param = parameter.rstrip(',')
    print(final_param)
    fields = ""
    counter = 0
    for i in result:
        is_there_data = i.split('=')
        if len(is_there_data) > 1:
            fields += i + "&"
        else:
            fields += i + '=" +' + ' request.POST["param' + str(counter) + '"] + "&'
            counter += 1
    print(fields)
    final_fields = fields.rstrip('&')
    file = open("app_dir/main/post_functions.py", "a+")
    code = """
def """ + function_name + """(request):
    data = requests.get(" """ + api_link + final_fields + """ ").json()
    print(data)
    return JsonResponse({'code': data})
"""
    file.write(code)
    file.close()
