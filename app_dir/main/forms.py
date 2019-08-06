import inspect

from app_dir.main.app_creator import *

headers = """  
headers: {
    "X-CSRFToken": $("input[name=csrfmiddlewaretoken]").val()
},
"""


def Label(param0):
    function_name = inspect.stack()[0][3]
    if param0 == "":
        form = """<h1>""" + function_name + """</h1>
        <button class="btn btn-primary" onclick='""" + function_name + """()'>Run</button>
        <button class="btn btn-info" onclick='continuous""" + function_name + """()'>Run Continuously</button>
        <button class="btn btn-danger" onclick='stop""" + function_name + """()'>Stop</button>
        <form enctype="multipart/form-data" action="" method="post">{% csrf_token %}"""
        form += """<input class="form-control" type="text" name="param0" id="param0""" + function_name + """" value='""" + param0 + """'/>"""
        form += """
        </form>"""
        form += """
        <script>
            function """ + function_name + """() {
                var param0 = $("#param0""" + function_name + """").val();
                $.ajax({
                    type: 'POST',
                    url: "/""" + function_name + """/",""" + \
                headers \
                + """data: {'param0': param0},
                    success: function (response) {
                        console.log(response.code);
                        document.getElementById('""" + function_name + """_result').innerHTML = JSON.stringify(response.code, undefined, 2);
                    }
                });
            }
            var myVar;
            function continuous""" + function_name + """() {
                var param0 = $("#param0""" + function_name + """").val();
                $.ajax({
                    type: 'POST',
                    url: "/""" + function_name + """/",""" + \
                headers \
                + """data: {'param0': param0},
                    success: function (response) {
                        console.log(response.code);
                        document.getElementById('""" + function_name + """_result').innerHTML = JSON.stringify(response.code, undefined, 2);
                    }
                });
                myVar""" + function_name + """ = setTimeout("continuous""" + function_name + """()", 100);
            }
            
        </script>
        function stop""" + function_name + """() {
                clearTimeout(myVar""" + function_name + """);
        }
        
    
        <pre style="width: 100%; height:100px" id='""" + function_name + """_result'></pre>
        """
        return form
    else:
        return param0


def Read(param0, param1):
    function_name = inspect.stack()[0][3]
    form = """<h1>""" + function_name + """</h1>
    <button class="btn btn-primary" onclick='""" + function_name + """()'>Run</button>
    <button class="btn btn-info" onclick='continuous""" + function_name + """()'>Run Continuously</button>
    <button class="btn btn-danger" onclick='stop""" + function_name + """()'>Stop</button>
    <form enctype="multipart/form-data" action="" method="post">{% csrf_token %}"""
    form += """<input class="form-control" type="text" name="param0" id="param0""" + function_name + """" value='""" + param0 + """'/>"""
    form += """<input class="form-control" type="text" name="param1" id="param1""" + function_name + """" value='""" + param1 + """'/>"""
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
       var myVar;
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


def Search(param0, param1, param2):
    function_name = inspect.stack()[0][3]
    form = """<h1>""" + function_name + """</h1>
    <button class="btn btn-primary" onclick='""" + function_name + """()'>Run</button>
     <button class="btn btn-info" onclick='continuous""" + function_name + """()'>Run Continuously</button>
    <button class="btn btn-danger" onclick='stop""" + function_name + """()'>Stop</button>
    <form enctype="multipart/form-data" action="" method="post">{% csrf_token %}"""
    form += """<input class="form-control" type="text" name="param0" id="param0""" + function_name + """" value='""" + param0 + """'/>"""
    form += """<input class="form-control" type="text" name="param1" id="param1""" + function_name + """" value='""" + param1 + """'/>"""
    form += """<input class="form-control" type="text" name="param2" id="param2""" + function_name + """" value='""" + param2 + """'/>"""
    form += """
       </form>"""
    form += """<script>
          function """ + function_name + """() {
              var param0 = $("#param0""" + function_name + """").val();
              var param1 = $("#param1""" + function_name + """").val();
              var param2 = $("#param2""" + function_name + """").val();
              $.ajax({
                  type: 'POST',
                  url: "/""" + function_name + """/",""" + \
            headers \
            + """
                 data: {'param0': param0, 'param1': param1, 'param2': param2},
                  success: function (response) {
                      console.log(response.code);
                      document.getElementById('""" + function_name + """_result').innerHTML = JSON.stringify(response.code, undefined, 2);
                  }
              });
          }
          var myVar;
          function continuous""" + function_name + """() {
              var param0 = $("#param0""" + function_name + """").val();
              var param1 = $("#param1""" + function_name + """").val();
              var param2 = $("#param2""" + function_name + """").val();
              $.ajax({
                  type: 'POST',
                  url: "/""" + function_name + """/",""" + \
            headers \
            + """
                 data: {'param0': param0, 'param1': param1, 'param2': param2},
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


def Send(param0, param1, param2, param3, param4):
    function_name = inspect.stack()[0][3]
    form = """<h1>""" + function_name + """</h1>
    <button class="btn btn-primary" onclick='""" + function_name + """()'>Run</button>
    <button class="btn btn-info" onclick='continuous""" + function_name + """()'>Run Continuously</button>
    <button class="btn btn-danger" onclick='stop""" + function_name + """()'>Stop</button>
    <form enctype="multipart/form-data" action="" method="post">{% csrf_token %}"""
    form += """<input class="form-control" type="text" name="param0" id="param0""" + function_name + """" value='""" + param0 + """'/>"""
    form += """<input class="form-control" type="text" name="param1" id="param1""" + function_name + """" value='""" + param1 + """'/>"""
    form += """<input class="form-control" type="text" name="param1" id="param2""" + function_name + """" value='""" + param2 + """'/>"""
    form += """<input class="form-control" type="text" name="param3" id="param3""" + function_name + """" value='""" + param3 + """'/>"""
    form += """<input class="form-control" type="text" name="param4" id="param4""" + function_name + """" value='""" + param4 + """'/>"""
    form += """
    </form>"""
    form += """
    <script>
        function """ + function_name + """() {
              var param0 = $("#param0""" + function_name + """").val();
              var param1 = $("#param1""" + function_name + """").val();
              var param2 = $("#param2""" + function_name + """").val();
              var param3 = $("#param3""" + function_name + """").val();
              var param4 = $("#param4""" + function_name + """").val();
              $.ajax({
                  type: 'POST',
                  url: "/""" + function_name + """/",
                  """ + \
            headers \
            + """
                 data: {'param0': param0, 'param1': param1, 'param2': param2, 'param3': param3, 'param4': param4},
                  success: function (response) {
                      console.log(response.code);
                      document.getElementById('""" + function_name + """_result').innerHTML = JSON.stringify(response.code, undefined, 2);
                  }
              });
        }
        var myVar;
        function continuous""" + function_name + """() {
              var param0 = $("#param0""" + function_name + """").val();
              var param1 = $("#param1""" + function_name + """").val();
              var param2 = $("#param2""" + function_name + """").val();
              var param3 = $("#param3""" + function_name + """").val();
              var param4 = $("#param4""" + function_name + """").val();
              $.ajax({
                  type: 'POST',
                  url: "/""" + function_name + """/",
                  """ + \
            headers \
            + """
                 data: {'param0': param0, 'param1': param1, 'param2': param2, 'param3': param3, 'param4': param4},
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


def weather_info(city):
    function_name = inspect.stack()[0][3]
    form = """<h1>""" + function_name + """</h1>
    <button class="btn btn-primary" onclick='""" + function_name + """()'>Run</button>
    <button class="btn btn-info" onclick='continuous""" + function_name + """()'>Run Continuously</button>
    <button class="btn btn-danger" onclick='stop""" + function_name + """()'>Stop</button>
    <form enctype="multipart/form-data" action="" method="post">{% csrf_token %}"""
    form += """<input class="form-control" type="text" name="param0" id="param0""" + function_name + """" value='""" + city + """'/>"""
    form += """
     </form>"""
    form += """<script>
        function """ + function_name + """() {
          var param0 = $("#param0""" + function_name + """").val();
          $.ajax({
              type: 'POST',
              url: "/""" + function_name + """/",""" + \
            headers \
            + """
             data: {'param0': param0},
              success: function (response) {
                  console.log(response.code);
                  document.getElementById('""" + function_name + """_result').innerHTML = JSON.stringify(response.code, undefined, 2);
              }
          });
        }
        var myVar;
        function continuous""" + function_name + """() {
              var param0 = $("#param0""" + function_name + """").val();
              $.ajax({
                  type: 'POST',
                  url: "/""" + function_name + """/",""" + \
            headers \
            + """
                 data: {'param0': param0},
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


def rajon():
    path = 'mailbox/credentials.json'
    result = path.split('/')
    print(result[1])
    return result[1]


def newspaper_headlines_reader(param0, param1, param2):
    code = "<h1>newspaper_headlines_reader</h1><button class='btn btn-primary' onclick='newspaper_headlines_reader()'>Run</button><button class='btn btn-info' onclick='continuousnewspaper_headlines_reader()'>Run Continuously</button><button class='btn btn-danger' onclick='stopnewspaper_headlines_reader()'>Stop Continuous Run</button><form enctype='multipart/form-data' action='' method='post'>{% csrf_token %}<input class='form-control' type='text' name='param0' id='param0newspaper_headlines_reader' value=''/><input class='form-control' type='text' name='param1' id='param1newspaper_headlines_reader' value=''/><input class='form-control' type='text' name='param2' id='param2newspaper_headlines_reader' value=''/></form><script>function newspaper_headlines_reader(){var param0 = $('#param0newspaper_headlines_reader').val();var param1 = $('#param1newspaper_headlines_reader').val();var param2 = $('#param2newspaper_headlines_reader').val(); $.ajax({type: 'POST',url: '/newspaper_headlines_reader/',headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()},data: {'param0': param0,'param1': param1,'param2': param2},success: function (response) {console.log(response.code);document.getElementById('newspaper_headlines_reader_result').innerHTML = JSON.stringify(response.code, undefined,2);}});}var myVar;function continuousnewspaper_headlines_reader(){var param0 = $('#param0newspaper_headlines_reader').val();var param1 = $('#param1newspaper_headlines_reader').val();var param2 = $('#param2newspaper_headlines_reader').val(); $.ajax({type: 'POST',url: '/newspaper_headlines_reader/',headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()},data: {'param0': param0,'param1': param1,'param2': param2},success: function (response) {console.log(response.code);document.getElementById('newspaper_headlines_reader_result').innerHTML = JSON.stringify(response.code, undefined,2);}});myVarnewspaper_headlines_reader = setTimeout('continuousnewspaper_headlines_reader()', 100);}function stopnewspaper_headlines_reader() {clearTimeout(myVarnewspaper_headlines_reader);}</script><pre style='width: 100%; height:100px' id='newspaper_headlines_reader_result'></pre><script>function newspaper_headlines_reader() {var param0 = $('#param0newspaper_headlines_reader').val();$.ajax({type: 'POST',url: '/newspaper_headlines_reader/',headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()},data: {'param0': param0},success: function (response) {console.log(response.code);document.getElementById('newspaper_headlines_reader_result').innerHTML = JSON.stringify(response.code, undefined, 2);});}</script>"
    return code
