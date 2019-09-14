Blockly.Blocks['do_it'] = {
    init: function () {
        this.appendValueInput("NAME")
            .setCheck(null)
            .appendField("Do");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};
Blockly.Blocks['weather'] = {
    init: function () {
        this.appendValueInput("to_input")
            .setCheck(null)
            .appendField("Weather info");
        this.setOutput(true, null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['motor-on'] = {
    init: function () {
        this.appendDummyInput()
            .appendField(new Blockly.FieldLabel('motor on'));//label
        //this.setOutput(true, 'String');
        this.setPreviousStatement(true, 'Action');
        this.setColour(60);
    }
}

Blockly.Blocks['motor-off'] = {
    init: function () {
        this.appendDummyInput()
            .appendField(new Blockly.FieldLabel('motor off'));
        //this.setOutput(true, 'String');
        this.setPreviousStatement(true, 'Action');
        this.setColour(20);
    }
}

Blockly.Blocks['l-sensor'] = {
    init: function () {
        this.appendDummyInput()
            .appendField(new Blockly.FieldLabel('lower sensor'));
        this.setOutput(true, 'Number');
        //this.setPreviousStatement(true, 'Action');
        this.setColour(20);
    }
}
Blockly.Blocks['print_content'] = {
    init: function () {
        this.appendValueInput("to_print")
            .setCheck(null)
            .appendField("Custom Print");
        this.setPreviousStatement(true, null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};


Blockly.Blocks['value_to_print'] = {
    init: function () {
        this.appendValueInput("to_input")
            .setCheck(null)
            .appendField("pass");
        this.setOutput(true, null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['Label'] = {
    init: function () {
        this.appendValueInput("param")
            .setCheck(null)
            .setAlign(Blockly.ALIGN_CENTRE)
            .appendField("Label");
        this.setOutput(true, null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};


Blockly.Blocks['Read'] = {
    init: function () {
        this.appendValueInput("param")
            .setCheck(null)
            .setAlign(Blockly.ALIGN_CENTRE)
            .appendField("Read")
            .appendField("Mailbox");
        this.appendValueInput("param2")
            .setCheck(null)
            .appendField("Label");
        this.setOutput(true, null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['Send'] = {
    init: function () {
        this.appendValueInput("param")
            .setCheck(null)
            .setAlign(Blockly.ALIGN_CENTRE)
            .appendField("Send")
            .appendField("Mailbox");
        this.appendValueInput("param2")
            .setCheck(null)
            .appendField("From");
        this.appendValueInput("param3")
            .setCheck(null)
            .appendField("To");
        this.appendValueInput("param4")
            .setCheck(null)
            .appendField("Subject");
        this.appendValueInput("param5")
            .setCheck(null)
            .appendField("Message");
        this.setOutput(true, null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['Search'] = {
    init: function () {
        this.appendValueInput("param")
            .setCheck(null)
            .setAlign(Blockly.ALIGN_CENTRE)
            .appendField("Search")
            .appendField("Mailbox");
        this.appendValueInput("param2")
            .setCheck(null)
            .appendField("Label");
        this.appendValueInput("param3")
            .setCheck(null)
            .appendField("Query");
        this.setOutput(true, null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['custom_if'] = {
    init: function () {
        this.appendValueInput("left")
            .setCheck(null)
            .appendField("IF");
        this.appendStatementInput("inner")
            .setCheck(null)
            .appendField("DO");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setOutput(true, null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['custom_if_else'] = {
    init: function () {
        this.appendValueInput("left")
            .setCheck(null)
            .appendField("IF");
        this.appendStatementInput("inner")
            .setCheck(null)
            .appendField("DO");
        this.appendDummyInput()
            .appendField("else");
        this.appendStatementInput("else")
            .setCheck(null)
            .appendField("DO");
        this.setOutput(true, null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['api_creator'] = {
    init: function () {
        this.appendValueInput("name")
            .setCheck(null)
            .appendField("API Creator");
        this.appendValueInput("api")
            .setCheck(null);
        this.appendValueInput("fields")
            .setCheck(null);
        this.appendValueInput("connection")
            .setCheck(null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['interactive_creator'] = {
    init: function () {
        this.appendValueInput("name")
            .setCheck(null)
            .appendField("Interactive Creator");
        this.appendValueInput("fields")
            .setCheck(null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['newspaper_headlines'] = {
    init: function () {
        this.appendValueInput("param0")
            .setCheck(null)
            .setAlign(Blockly.ALIGN_CENTRE)
            .appendField('newspaper_headlines q');
        this.appendValueInput("param1")
            .setCheck(null)
            .appendField('from');
        this.appendValueInput("param2")
            .setCheck(null)
            .appendField('sortBy');
        this.setOutput(true, null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['recipe_puppy'] = {
    init: function () {
        this.appendValueInput("param0")
            .setCheck(null)
            .setAlign(Blockly.ALIGN_CENTRE)
            .appendField('recipe_puppy i');
        this.appendValueInput("param1")
            .setCheck(null)
            .appendField('q');
        this.appendValueInput("param2")
            .setCheck(null)
            .appendField('p');
        this.setOutput(true, null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};


Blockly.Blocks['rajon'] = {
    init: function () {
        this.appendValueInput("to_input")
            .setCheck(null)
            .appendField('rajon');
        this.setOutput(true, null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

             Blockly.Blocks['custom_app'] = {
                init: function() {
               this.appendValueInput("param0")
              .setCheck(null)
              .setAlign(Blockly.ALIGN_CENTRE)
            .appendField('custom_app');
           this.appendValueInput("param1")
                  .setCheck(null);
            this.appendValueInput("param2")
                  .setCheck(null);
            this.appendValueInput("param3")
                  .setCheck(null);
            this.setColour(230);
              this.setTooltip("");
              this.setHelpUrl("");
              }
            };
         