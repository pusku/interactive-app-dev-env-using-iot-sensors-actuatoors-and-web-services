def actuator_function_writer(function_name, tag):
    file = open("app_dir/main/generated_functions.py", "a+")
    code = """
def """ + function_name + """(motor_status):
    url = 'http://127.0.0.1:8000/api/actuators/'
    data = {
        "topic": '""" + tag + """',
        "value": motor_status,
        "time": "2019-01-24T13:35:24.246226Z",
        "name": "1"
        }
    response = requests.post(url, data=data)
    print(response.text)
    
    
"""
    file.write(code)
    file.close()


def sensor_function_writer(function_name, tag):
    file = open("app_dir/main/generated_functions.py", "a+")
    code = """
def """ + function_name + """():
    empty_list=[]
    sensor_tag = """ + tag + """
    data = requests.get("http://127.0.0.1:8000/api/sensors/").json()
    for i in data:
        if i['topic']==sensor_tag:
            empty_list.append(i)
    data = empty_list[-1]
    print(data)
    data = int(data['value'])
    return(data)
    
    
"""
    file.write(code)
    file.close()


def mailbox_function_writer(function_name, tag):
    file = open("app_dir/main/generated_functions.py", "a+")
    code = """
def """ + function_name + """():
    path = """ + "'" + tag + "'" + """
    result = path.split('/')
    print(result)
    return result
    
    """
    file.write(code)

    file.close()


def api_function_writer(function_name, api_link, api_fields):
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
            fields += i + '=" +' + ' param' + str(counter) + ' + "&'
            counter += 1
    print(fields)
    final_fields = fields.rstrip('&')
    file = open("app_dir/main/generated_functions.py", "a+")
    code = """
def """ + function_name + """(""" + final_param + """):
    data = requests.get(" """ + api_link + final_fields + """ ").json()
    print(data)
    return data
"""
    file.write(code)
    file.close()


def interactive_function_writer(function_name, api_fields):
    result = api_fields
    fields = ""
    parameter = ""
    for i in range(int(result)):
        parameter += "param" + str(i) + ','
        fields += "param" + str(i) + " = param" + str(i) + "\n    "
    final_param = parameter.rstrip(',')

    file = open("app_dir/main/app_creator.py", "a+")
    code = """
def """ + function_name + """(""" + final_param + """):
    """ + fields
    file.write(code)
    file.close()
