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


def api_function_writer(function_name, tag):
    file = open("app_dir/main/generated_functions.py", "a+")
    code = """
def """ + function_name + "_Post" + """(param, param2):
    data = requests.get("http://127.0.0.1:8000/api/api/").json()
    data = {
		param: param2,
    }
    
	response = requests.post(url, data=data)
	return response
	
	
    
def """ + function_name + "_Get" + """(param):
    data = requests.get("http://127.0.0.1:8000/api/api/param").json()
    print(data)
    return(data)
    
    

def """ + function_name + "_Search" + """(param):
    data = requests.get("http://127.0.0.1:8000/api/api/param").json()
    print(data)
    return(data)
    
    
"""
    file.write(code)
    file.close()
