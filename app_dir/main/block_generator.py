import string
import random


def name_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def block_generator(block_name, block_type):
    ui_generator(block_name, block_type)
    declaration(block_name, block_type)
    js_generator(block_name, block_type)
    js_declaration(block_name, block_type)


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
        f.write('\n' + "<block type=" + '"' + block_name + "_Label" + '"' + "></block>")
        f.write('\n' + "<block type=" + '"' + block_name + "_Read" + '"' + "></block>")
        f.write('\n' + "<block type=" + '"' + block_name + "_Send" + '"' + "></block>")
        f.write('\n' + "<block type=" + '"' + block_name + "_Search" + '"' + "></block>")
        f.close()
    if block_type == 'api':
        f = open("templates/api_declaration.html", "a+")
        f.write('\n' + "<block type=" + '"' + block_name + "_Post" + '"' + "></block>")
        f.write('\n' + "<block type=" + '"' + block_name + "_Get" + '"' + "></block>")
        f.write('\n' + "<block type=" + '"' + block_name + "_Search" + '"' + "></block>")
        f.close()


def js_generator(block_name, block_type):
    if block_type == 'sensor':
        f = open("static/js/generators/codegenerator-" + block_name + ".js", "w+")
        js_container = get_block_js(block_name, block_type)
        f.write(js_container)
        f.close()
    if block_type == 'actuator':
        f = open("static/js/generators/codegenerator-" + block_name + ".js", "w+")
        js_container = get_block_js(block_name, block_type)
        f.write(js_container)
        f.close()
    if block_type == 'mailbox':
        f = open("static/js/generators/codegenerator-" + block_name + "_Label.js", "w+")
        js_container = get_block_js_others(block_name, 'Label')
        f.write(js_container)
        f.close()

        f = open("static/js/generators/codegenerator-" + block_name + "_Read.js", "w+")
        js_container = get_block_js_others(block_name, 'Read')
        f.write(js_container)
        f.close()

        f = open("static/js/generators/codegenerator-" + block_name + "_Send.js", "w+")
        js_container = get_block_js_others(block_name, 'Send')
        f.write(js_container)
        f.close()

        f = open("static/js/generators/codegenerator-" + block_name + "_Search.js", "w+")
        js_container = get_block_js_others(block_name, 'Search')
        f.write(js_container)
        f.close()

    if block_type == 'api':
        f = open("static/js/generators/codegenerator-" + block_name + "_Post.js", "w+")
        js_container = get_block_js_others(block_name, 'Post')
        f.write(js_container)
        f.close()

        f = open("static/js/generators/codegenerator-" + block_name + "_Get.js", "w+")
        js_container = get_block_js_others(block_name, 'Get')
        f.write(js_container)
        f.close()

        f = open("static/js/generators/codegenerator-" + block_name + "_Search.js", "w+")
        js_container = get_block_js_others(block_name, 'Search')
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
    if block_type == 'mailbox':
        block_ui = """
                  Blockly.Blocks['""" + block_name + "_Label" + """'] = {
                  init: function() {
                  this.appendValueInput("to_input")
                  .setCheck(null)
                  .appendField('""" + block_name + "_Label" + """');
                  this.setOutput(true, null);
                  this.setColour(230);
                  this.setTooltip("");
                  this.setHelpUrl("");
            }
          };
          
            Blockly.Blocks['""" + block_name + "_Read" + """'] = {
                  init: function() {
                  this.appendValueInput("to_input")
                  .setCheck(null)
                  .appendField('""" + block_name + "_Read" + """');
                  this.setOutput(true, null);
                  this.setColour(230);
                  this.setTooltip("");
                  this.setHelpUrl("");
            }
          };
          
            Blockly.Blocks['""" + block_name + "_Send" + """'] = {
                  init: function() {
                  this.appendValueInput("to_input")
                  .setCheck(null)
                  .appendField('""" + block_name + "_Send" + """');
                  this.setOutput(true, null);
                  this.setColour(230);
                  this.setTooltip("");
                  this.setHelpUrl("");
            }
          };
          
            Blockly.Blocks['""" + block_name + "_Search" + """'] = {
                  init: function() {
                  this.appendValueInput("to_input")
                  .setCheck(null)
                  .appendField('""" + block_name + "_Search" + """');
                  this.setOutput(true, null);
                  this.setColour(230);
                  this.setTooltip("");
                  this.setHelpUrl("");
            }
          };
              """
    if block_type == 'api':
        block_ui = """
                         Blockly.Blocks['""" + block_name + "_Post" + """'] = {
                         init: function() {
                         this.appendValueInput("to_input")
                         .setCheck(null)
                         .appendField('""" + block_name + "_Post" + """');
                         this.setOutput(true, null);
                         this.setColour(230);
                         this.setTooltip("");
                         this.setHelpUrl("");
                   }
                 };

                   Blockly.Blocks['""" + block_name + "_Search" + """'] = {
                         init: function() {
                         this.appendValueInput("to_input")
                         .setCheck(null)
                         .appendField('""" + block_name + "_Search" + """');
                         this.setOutput(true, null);
                         this.setColour(230);
                         this.setTooltip("");
                         this.setHelpUrl("");
                   }
                 };
                 
                 Blockly.Blocks['""" + block_name + "_Get" + """'] = {
                         init: function() {
                         this.appendValueInput("to_input")
                         .setCheck(null)
                         .appendField('""" + block_name + "_Get" + """');
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

def get_block_js_others(block_name, block_label):

    if block_label == 'Label':
        block_js = """
            Blockly.Python['""" + block_name + "_Label" + """'] = function(block) {
              var value_to_input = Blockly.Python.valueToCode(block, 'to_input', Blockly.Python.ORDER_ATOMIC);
              var code = '""" + block_name + "_Label" + """('+value_to_input+')';
              return [code, Blockly.Python.ORDER_NONE];
            };
        """
        return block_js
        
    if block_label == 'Read':
        block_js = """
            Blockly.Python['""" + block_name + "_Read" + """'] = function(block) {
              var value_to_input = Blockly.Python.valueToCode(block, 'to_input', Blockly.Python.ORDER_ATOMIC);
              var code = '""" + block_name + "_Read" + """('+value_to_input+')';
              return [code, Blockly.Python.ORDER_NONE];
            };
        """
        return block_js

    if block_label == 'Send':
        block_js = """
            Blockly.Python['""" + block_name + "_Send" + """'] = function(block) {
              var value_to_input = Blockly.Python.valueToCode(block, 'to_input', Blockly.Python.ORDER_ATOMIC);
              var code = '""" + block_name + "_Send" + """('+value_to_input+')';
              return [code, Blockly.Python.ORDER_NONE];
            };
        """
        return block_js

    if block_label == 'Search':
        block_js = """
            Blockly.Python['""" + block_name + "_Search" + """'] = function(block) {
              var value_to_input = Blockly.Python.valueToCode(block, 'to_input', Blockly.Python.ORDER_ATOMIC);
              var code = '""" + block_name + "_Search" + """('+value_to_input+')';
              return [code, Blockly.Python.ORDER_NONE];
            };
        """
        return block_js

    if block_label == 'Post':
        block_js = """
            Blockly.Python['""" + block_name + "_Post" + """'] = function(block) {
              var value_to_input = Blockly.Python.valueToCode(block, 'to_input', Blockly.Python.ORDER_ATOMIC);
              var code = '""" + block_name + "_Post" + """('+value_to_input+')';
              return [code, Blockly.Python.ORDER_NONE];
            };
        """
        return block_js

    if block_label == 'Get':
        block_js = """
            Blockly.Python['""" + block_name + "_Get" + """'] = function(block) {
              var value_to_input = Blockly.Python.valueToCode(block, 'to_input', Blockly.Python.ORDER_ATOMIC);
              var code = '""" + block_name + "_Get" + """('+value_to_input+')';
              return [code, Blockly.Python.ORDER_NONE];
            };
        """
        return block_js


def js_declaration(block_name, block_type):
    if block_type == 'sensor' or 'actuator':
        f = open("templates/js_declaration.js", "a+")
        f.write('\n\n<script src="static/js/generators/codegenerator-' + block_name + '.js"></script>')
        f.close()
    if block_type == 'mailbox':
        f = open("templates/js_declaration.js", "a+")
        f.write('\n\n<script src="static/js/generators/codegenerator-' + block_name + '_Label.js"></script>')
        f.write('\n\n<script src="static/js/generators/codegenerator-' + block_name + '_Read.js"></script>')
        f.write('\n\n<script src="static/js/generators/codegenerator-' + block_name + '_Send.js"></script>')
        f.write('\n\n<script src="static/js/generators/codegenerator-' + block_name + '_Search.js"></script>')
        f.close()
    if block_type == 'api':
        f = open("templates/js_declaration.js", "a+")
        f.write('\n\n<script src="static/js/generators/codegenerator-' + block_name + '_Post.js"></script>')
        f.write('\n\n<script src="static/js/generators/codegenerator-' + block_name + '_Get.js"></script>')
        f.write('\n\n<script src="static/js/generators/codegenerator-' + block_name + '_Search.js"></script>')
        f.close()
