def block_generator(block_name, block_type):
    ui_generator(block_name, block_type)
    declaration(block_name, block_type)
    js_generator(block_name, block_type)
    js_declaration(block_name)


def api_block_generator(block_name, block_type, api_fields):
    result = api_fields.split(',')
    res_len = len(result)
    counter1 = 0
    counter2 = 0
    else_counter = 0
    append_field = ""
    if res_len == 0:
        append_field += """this.appendValueInput("param0")
                      .setCheck(null)
                      .setAlign(Blockly.ALIGN_CENTRE)
        .appendField('""" + block_name + """');
        """
    else:
        for i in result:
            is_there_data = i.split('=')
            if len(is_there_data) > 1:
                counter1 = counter1 + 1
            else:
                if counter2 == 0:
                    append_field += """this.appendValueInput("param0")
                      .setCheck(null)
                      .setAlign(Blockly.ALIGN_CENTRE)
                    .appendField('""" + block_name + " " + i + """');
                   """
                    counter2 += 1
                else:
                    append_field += """this.appendValueInput("param""" + str(else_counter+1) + """")
                          .setCheck(null)
                    .appendField('""" + i + """');
                    """
                    else_counter += 1
    param_should = res_len - counter1
    parameter = ""
    parameter_names = ""

    for p in range(param_should - 1):
        parameter += "var param" + str(
            p+1) + " = Blockly.Python.valueToCode(block, 'param" + str(
            p+1) + "', Blockly.Python.ORDER_ATOMIC);\n"
        parameter_names += "'+param" + str(p+1) + "+',"

    final_param = parameter_names.rstrip(',')
    f = open("templates/blocks.js", "a+")
    ui_container = """
             Blockly.Blocks['""" + block_name + """'] = {
                init: function() {
               """\
                   + append_field +\
                   """this.setPreviousStatement(true, null);
                  this.setColour(230);
              this.setTooltip("");
              this.setHelpUrl("");
              }
            };
         """
    f.write(ui_container)
    f.close()
    declaration(block_name, block_type)

    f = open("static/js/generators/codegenerator-" + block_name + ".js", "w+")
    js_container = """
            Blockly.Python['""" + block_name + """'] = function(block) {
                var param0 = Blockly.Python.valueToCode(block, 'param0', Blockly.Python.ORDER_ATOMIC);""" \
                + parameter + """
                var code = '""" + block_name + """('+param0+',""" + final_param + """)';
                return [code, Blockly.Python.ORDER_NONE];
            };
        """
    f.write(js_container)
    f.close()

    js_declaration(block_name)


def ui_generator(block_name, block_type):
    f = open("templates/blocks.js", "a+")
    ui_container = get_ui(block_name, block_type)
    f.write(ui_container)
    f.close()


def declaration(block_name, block_type):
    if block_type == 'sensor':
        f = open("templates/sensor_declaration.html", "a+")
        f.write('\n' + "<block type=" + '"' + block_name + '"' + "></block>")
        f.close()
    if block_type == 'actuator':
        f = open("templates/actuator_declaration.html", "a+")
        f.write('\n' + "<block type=" + '"' + block_name + '"' + "></block>")
        f.close()
    if block_type == 'mailbox':
        f = open("templates/mailbox_declaration.html", "a+")
        f.write('\n' + "<block type=" + '"' + block_name + '"' + "></block>")
        f.close()
    if block_type == 'api':
        f = open("templates/api_declaration.html", "a+")
        f.write('\n' + "<block type=" + '"' + block_name + '"' + "></block>")
        f.close()


def js_generator(block_name, block_type):
    f = open("static/js/generators/codegenerator-" + block_name + ".js", "w+")
    js_container = get_block_js(block_name, block_type)
    f.write(js_container)
    f.close()


def get_ui(block_name, block_type):
    if block_type == 'sensor' or 'actuator':
        block_ui = """
        Blockly.Blocks['""" + block_name + """'] = {
        init: function() {
        this.appendValueInput("to_input")
        .setCheck(null)
        .appendField('""" + block_name + """');
        this.setOutput(true, null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
      }
    };
    """
        return block_ui

    if block_type == 'mailbox':
        block_ui = """
        Blockly.Blocks['""" + block_name + "" + """'] = {
        init: function() {
        this.appendValueInput("to_input")
        .setCheck(null)
        .appendField('""" + block_name + "" + """');
        this.setOutput(true, null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
        }
      };
      """
        return block_ui


def get_block_js(block_name, block_type):
    if block_type == 'sensor' or 'actuator':
        block_js = """
            Blockly.Python['""" + block_name + """'] = function(block) {
              var value_to_input = Blockly.Python.valueToCode(block, 'to_input', Blockly.Python.ORDER_ATOMIC);
              var code = '""" + block_name + """('+value_to_input+')';
              return [code, Blockly.Python.ORDER_NONE];
            };
        """
        return block_js

    if block_type == 'mailbox':
        block_js = """
                Blockly.Python['""" + block_name + """'] = function(block) {
                  var value_to_input = Blockly.Python.valueToCode(block, 'to_input', Blockly.Python.ORDER_ATOMIC);
                  var code = '""" + block_name + """('+value_to_input+')';
                  return [code, Blockly.Python.ORDER_NONE];
                };
            """
        return block_js


def js_declaration(block_name):
    f = open("templates/js_declaration.html", "a+")
    f.write("""\n\n<script src="{% static  'js/generators/codegenerator-""" + block_name + """.js' %}"></script>""")
    f.close()
