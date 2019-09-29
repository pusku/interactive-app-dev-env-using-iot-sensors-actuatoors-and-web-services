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
            var myVar""" + function_name + """;
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
          var myVar""" + function_name + """;
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
    print(param0)
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
        var myVar""" + function_name + """;
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
        var myVar""" + function_name + """;
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



def newspaper_headlines(param0,param1,param2):
    code = "<h1>newspaper_headlines</h1><button class='btn btn-primary' onclick='newspaper_headlines()'>Run</button><button class='btn btn-info' onclick='continuousnewspaper_headlines()'>Run Continuously</button><button class='btn btn-danger' onclick='stopnewspaper_headlines()'>Stop Continuous Run</button><form enctype='multipart/form-data' action='' method='post'>{% csrf_token %}<input class='form-control' type='text' name='param0' id='param0newspaper_headlines' value=''/><input class='form-control' type='text' name='param1' id='param1newspaper_headlines' value=''/><input class='form-control' type='text' name='param2' id='param2newspaper_headlines' value=''/></form><script>function newspaper_headlines(){var param0 = $('#param0newspaper_headlines').val();var param1 = $('#param1newspaper_headlines').val();var param2 = $('#param2newspaper_headlines').val(); $.ajax({type: 'POST',url: '/newspaper_headlines/',headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()},data: {'param0': param0,'param1': param1,'param2': param2},success: function (response) {console.log(response.code);document.getElementById('newspaper_headlines_result').innerHTML = JSON.stringify(response.code, undefined,2);}});}var myVarnewspaper_headlines;function continuousnewspaper_headlines(){var param0 = $('#param0newspaper_headlines').val();var param1 = $('#param1newspaper_headlines').val();var param2 = $('#param2newspaper_headlines').val(); $.ajax({type: 'POST',url: '/newspaper_headlines/',headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()},data: {'param0': param0,'param1': param1,'param2': param2},success: function (response) {console.log(response.code);document.getElementById('newspaper_headlines_result').innerHTML = JSON.stringify(response.code, undefined,2);}});myVarnewspaper_headlines = setTimeout('continuousnewspaper_headlines()', 100);}function stopnewspaper_headlines() {clearTimeout(myVarnewspaper_headlines);}</script><pre style='width: 100%; height:100px' id='newspaper_headlines_result'></pre><script>function newspaper_headlines() {var param0 = $('#param0newspaper_headlines').val();$.ajax({type: 'POST',url: '/newspaper_headlines/',headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()},data: {'param0': param0},success: function (response) {console.log(response.code);document.getElementById('newspaper_headlines_result').innerHTML = JSON.stringify(response.code, undefined, 2);});}</script>"
    return code
    


def recipe_puppy(param0,param1,param2):
    code = "<h1>recipe_puppy</h1><button class='btn btn-primary' onclick='recipe_puppy()'>Run</button><button class='btn btn-info' onclick='continuousrecipe_puppy()'>Run Continuously</button><button class='btn btn-danger' onclick='stoprecipe_puppy()'>Stop Continuous Run</button><form enctype='multipart/form-data' action='' method='post'>{% csrf_token %}<input class='form-control' type='text' name='param0' id='param0recipe_puppy' value=''/><input class='form-control' type='text' name='param1' id='param1recipe_puppy' value=''/><input class='form-control' type='text' name='param2' id='param2recipe_puppy' value=''/></form><script>function recipe_puppy(){var param0 = $('#param0recipe_puppy').val();var param1 = $('#param1recipe_puppy').val();var param2 = $('#param2recipe_puppy').val(); $.ajax({type: 'POST',url: '/recipe_puppy/',headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()},data: {'param0': param0,'param1': param1,'param2': param2},success: function (response) {console.log(response.code);document.getElementById('recipe_puppy_result').innerHTML = JSON.stringify(response.code, undefined,2);}});}var myVarrecipe_puppy;function continuousrecipe_puppy(){var param0 = $('#param0recipe_puppy').val();var param1 = $('#param1recipe_puppy').val();var param2 = $('#param2recipe_puppy').val(); $.ajax({type: 'POST',url: '/recipe_puppy/',headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()},data: {'param0': param0,'param1': param1,'param2': param2},success: function (response) {console.log(response.code);document.getElementById('recipe_puppy_result').innerHTML = JSON.stringify(response.code, undefined,2);}});myVarrecipe_puppy = setTimeout('continuousrecipe_puppy()', 100);}function stoprecipe_puppy() {clearTimeout(myVarrecipe_puppy);}</script><pre style='width: 100%; height:100px' id='recipe_puppy_result'></pre><script>function recipe_puppy() {var param0 = $('#param0recipe_puppy').val();$.ajax({type: 'POST',url: '/recipe_puppy/',headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()},data: {'param0': param0},success: function (response) {console.log(response.code);document.getElementById('recipe_puppy_result').innerHTML = JSON.stringify(response.code, undefined, 2);});}</script>"
    return code
    


def cricket(param0,param1,param2):
    code = "<h1>cricket</h1><button class='btn btn-primary' onclick='cricket()'>Run</button><button class='btn btn-info' onclick='continuouscricket()'>Run Continuously</button><button class='btn btn-danger' onclick='stopcricket()'>Stop Continuous Run</button><form enctype='multipart/form-data' action='' method='post'>{% csrf_token %}<input class='form-control' type='text' name='param0' id='param0cricket' value=''/><input class='form-control' type='text' name='param1' id='param1cricket' value=''/><input class='form-control' type='text' name='param2' id='param2cricket' value=''/></form><script>function cricket(){var param0 = $('#param0cricket').val();var param1 = $('#param1cricket').val();var param2 = $('#param2cricket').val(); $.ajax({type: 'POST',url: '/cricket/',headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()},data: {'param0': param0,'param1': param1,'param2': param2},success: function (response) {console.log(response.code);document.getElementById('cricket_result').innerHTML = JSON.stringify(response.code, undefined,2);}});}var myVarcricket;function continuouscricket(){var param0 = $('#param0cricket').val();var param1 = $('#param1cricket').val();var param2 = $('#param2cricket').val(); $.ajax({type: 'POST',url: '/cricket/',headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()},data: {'param0': param0,'param1': param1,'param2': param2},success: function (response) {console.log(response.code);document.getElementById('cricket_result').innerHTML = JSON.stringify(response.code, undefined,2);}});myVarcricket = setTimeout('continuouscricket()', 100);}function stopcricket() {clearTimeout(myVarcricket);}</script><pre style='width: 100%; height:100px' id='cricket_result'></pre><script>function cricket() {var param0 = $('#param0cricket').val();$.ajax({type: 'POST',url: '/cricket/',headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()},data: {'param0': param0},success: function (response) {console.log(response.code);document.getElementById('cricket_result').innerHTML = JSON.stringify(response.code, undefined, 2);});}</script>"
    return code
    


def doctor(param0,param1,param2):
    code = "<h1>doctor</h1><button class='btn btn-primary' onclick='doctor()'>Run</button><button class='btn btn-info' onclick='continuousdoctor()'>Run Continuously</button><button class='btn btn-danger' onclick='stopdoctor()'>Stop Continuous Run</button><form enctype='multipart/form-data' action='' method='post'>{% csrf_token %}<input class='form-control' type='text' name='param0' id='param0doctor' value=''/><input class='form-control' type='text' name='param1' id='param1doctor' value=''/><input class='form-control' type='text' name='param2' id='param2doctor' value=''/></form><script>function doctor(){var param0 = $('#param0doctor').val();var param1 = $('#param1doctor').val();var param2 = $('#param2doctor').val(); $.ajax({type: 'POST',url: '/doctor/',headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()},data: {'param0': param0,'param1': param1,'param2': param2},success: function (response) {console.log(response.code);document.getElementById('doctor_result').innerHTML = JSON.stringify(response.code, undefined,2);}});}var myVardoctor;function continuousdoctor(){var param0 = $('#param0doctor').val();var param1 = $('#param1doctor').val();var param2 = $('#param2doctor').val(); $.ajax({type: 'POST',url: '/doctor/',headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()},data: {'param0': param0,'param1': param1,'param2': param2},success: function (response) {console.log(response.code);document.getElementById('doctor_result').innerHTML = JSON.stringify(response.code, undefined,2);}});myVardoctor = setTimeout('continuousdoctor()', 100);}function stopdoctor() {clearTimeout(myVardoctor);}</script><pre style='width: 100%; height:100px' id='doctor_result'></pre><script>function doctor() {var param0 = $('#param0doctor').val();$.ajax({type: 'POST',url: '/doctor/',headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()},data: {'param0': param0},success: function (response) {console.log(response.code);document.getElementById('doctor_result').innerHTML = JSON.stringify(response.code, undefined, 2);});}</script>"
    return code


def rajon():
    path = 'mailbox/credentials.json'
    result = path.split('/')
    print(result)
    return result[1]



def news(param0,param1,param2):
    code = "<h1>news</h1><button class='btn btn-primary' onclick='news()'>Run</button><button class='btn btn-info' onclick='continuousnews()'>Run Continuously</button><button class='btn btn-danger' onclick='stopnews()'>Stop Continuous Run</button><form enctype='multipart/form-data' action='' method='post'>{% csrf_token %}<input class='form-control' type='text' name='param0' id='param0news' value=''/><input class='form-control' type='text' name='param1' id='param1news' value=''/><input class='form-control' type='text' name='param2' id='param2news' value=''/></form><script>function news(){var param0 = $('#param0news').val();var param1 = $('#param1news').val();var param2 = $('#param2news').val(); $.ajax({type: 'POST',url: '/news/',headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()},data: {'param0': param0,'param1': param1,'param2': param2},success: function (response) {console.log(response.code);document.getElementById('news_result').innerHTML = JSON.stringify(response.code, undefined,2);}});}var myVarnews;function continuousnews(){var param0 = $('#param0news').val();var param1 = $('#param1news').val();var param2 = $('#param2news').val(); $.ajax({type: 'POST',url: '/news/',headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()},data: {'param0': param0,'param1': param1,'param2': param2},success: function (response) {console.log(response.code);document.getElementById('news_result').innerHTML = JSON.stringify(response.code, undefined,2);}});myVarnews = setTimeout('continuousnews()', 100);}function stopnews() {clearTimeout(myVarnews);}</script><pre style='width: 100%; height:100px' id='news_result'></pre><script>function news() {var param0 = $('#param0news').val();$.ajax({type: 'POST',url: '/news/',headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()},data: {'param0': param0},success: function (response) {console.log(response.code);document.getElementById('news_result').innerHTML = JSON.stringify(response.code, undefined, 2);});}</script>"
    return code
    