import inspect


def custom_if(param0, param1):
    function_name = inspect.stack()[0][3]
    if param0 is True:
        result = param1
        return result
    else:
        return """<pre style="width: 100%; height:100px" id='""" + function_name + """_result'>No Data For This Condtion At The Moment</pre>"""


def custom_if_else(param0, param1, param2):
    function_name = inspect.stack()[0][3]
    if param0 is True:
        res = param1
        # result = """<pre style="width: 100%; height:100px" id='""" + function_name + """_result'>""" + param1 + """</pre>"""
        return res
    else:
        # result = """<pre style="width: 100%; height:100px" id='""" + function_name + """_result'>""" + param2 + """</pre>"""
        res = param2
        return res

def value_to_print(text):
    return text


def print_content(what_to_print):
    result = what_to_print
    return result


headers = """  
headers: {
    "X-CSRFToken": $("input[name=csrfmiddlewaretoken]").val()
},
"""


def Read(param0, param1):
    function_name = inspect.stack()[0][3]
    form = """<h1>""" + function_name + """</h1>
    <button class="btn btn-primary" onclick='""" + function_name + """()'>Run</button>
    <button class="btn btn-info" onclick='continuous""" + function_name + """()'>Run Continuously</button>
    <button class="btn btn-danger" onclick='stop""" + function_name + """()'>Stop</button>
    <form enctype="multipart/form-data" action="" method="post">{% csrf_token %}"""
    form += """<input class="form-control" type="hidden" name="param0" id="param0""" + function_name + """" value='""" + param0 + """'/>"""
    form += """<input class="form-control" type="hidden" name="param1" id="param1""" + function_name + """" value='""" + param1 + """'/>"""
    form += """
    </form>"""
    form += """<script>
       function """ + function_name + """() {
           var param0 = $("#param0""" + function_name + """").val();
           var param1 = $("#param1""" + function_name + """").val();
           $.ajax({
               type: 'POST',
               url: "/""" + function_name + """/",""" + \
            headers \
            + """
               data: {'param0': param0, 'param1': param1},
               success: function (response) {
                   console.log(response.code);
                   document.getElementById('""" + function_name + """_result').innerHTML = JSON.stringify(response.code, undefined, 2);
               }
           });
       }
       var myVar""" + function_name + """;
       function continuous""" + function_name + """() {
           var param0 = $("#param0""" + function_name + """").val();
           var param1 = $("#param1""" + function_name + """").val();
           $.ajax({
               type: 'POST',
               url: "/""" + function_name + """/",""" + \
            headers \
            + """
               data: {'param0': param0, 'param1': param1},
               success: function (response) {
                   console.log(response.code);
                   document.getElementById('""" + function_name + """_result').innerHTML = JSON.stringify(response.code, undefined, 2);
               }
           });
           myVar""" + function_name + """ = setTimeout("continuous""" + function_name + """()", 100);
       }
       function stop""" + function_name + """() {
            clearTimeout(myVar""" + function_name + """);
        }
   </script>

    <pre style="width: 100%; height:100px" id='""" + function_name + """_result'></pre>
    """
    return form
