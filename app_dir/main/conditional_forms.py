import inspect


def custom_if(param0, param1):
    function_name = inspect.stack()[0][3]
    if param0 is True:
        result = """<pre style="width: 100%; height:100px" id='""" + function_name + """_result'>""" + param1 + """</pre>"""
        return result
    else:
        return """<pre style="width: 100%; height:100px" id='""" + function_name + """_result'>No Data For This Condtion At The Moment</pre>"""


def custom_if_else(param0, param1, param2):
    function_name = inspect.stack()[0][3]
    if param0 is True:
        result = """<pre style="width: 100%; height:100px" id='""" + function_name + """_result'>""" + param1 + """</pre>"""
        return result
    else:
        result = """<pre style="width: 100%; height:100px" id='""" + function_name + """_result'>""" + param2 + """</pre>"""
        return result


def value_to_print(text):
    return text


def print_content(what_to_print):
    result = what_to_print
    return result
