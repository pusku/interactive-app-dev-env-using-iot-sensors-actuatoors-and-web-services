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
//weater block start
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
//weather block end

//motor block start
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
//motor block end

//lower sensor block start
Blockly.Blocks['l-sensor'] = {
    init: function () {
        this.appendDummyInput()
            .appendField(new Blockly.FieldLabel('lower sensor'));
        this.setOutput(true, 'Number');
        //this.setPreviousStatement(true, 'Action');
        this.setColour(20);
    }
}


//start print_content

Blockly.Blocks['print_content'] = {
    init: function () {
        this.appendValueInput("to_print")
            .setCheck(null)
            .appendField(new Blockly.FieldTextInput("Print value"), "NAME");
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
        this.setPreviousStatement(true, null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['place_finder'] = {
    init: function () {
        this.appendValueInput("param")
            .setCheck(null)
            .setAlign(Blockly.ALIGN_CENTRE)
            .appendField("place_finder");
        this.setPreviousStatement(true, null);
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
            .appendField("Read");
        this.appendValueInput("param2")
            .setCheck(null);
        this.setPreviousStatement(true, null);
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
            .appendField("Send");
        this.appendValueInput("param2")
            .setCheck(null);
        this.appendValueInput("param3")
            .setCheck(null);
        this.appendValueInput("param4")
            .setCheck(null);
        this.appendValueInput("param5")
            .setCheck(null);
        this.setPreviousStatement(true, null);
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
            .appendField("Search");
        this.appendValueInput("param2")
            .setCheck(null);
        this.appendValueInput("param3")
            .setCheck(null);
        this.setPreviousStatement(true, null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};


Blockly.Blocks['Rajon'] = {
    init: function () {
        this.appendValueInput("to_input")
            .setCheck(null)
            .appendField('Rajon');
        this.setOutput(true, null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};


Blockly.Blocks['weather_test'] = {
    init: function () {
        this.appendValueInput("param0")
            .setCheck(null)
            .setAlign(Blockly.ALIGN_CENTRE)
            .appendField('weather_test');
        this.setPreviousStatement(true, null);
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
            .appendField('recipe_puppy');
        this.appendValueInput("param1")
            .setCheck(null);
        this.appendValueInput("param2")
            .setCheck(null);
        this.setPreviousStatement(true, null);
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
            .appendField('newspaper_headlines');
        this.appendValueInput("param1")
            .setCheck(null);
        this.appendValueInput("param2")
            .setCheck(null);
        this.setPreviousStatement(true, null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

             Blockly.Blocks['cricket'] = {
                init: function() {
               this.appendValueInput("param0")
                      .setCheck(null)
                      .setAlign(Blockly.ALIGN_CENTRE)
                    .appendField('cricket completedlimit');
                   this.appendValueInput("param2")
                          .setCheck(null)
                    .appendField('inprogresslimit');
                    this.appendValueInput("param3")
                          .setCheck(null)
                    .appendField('upcomingLimit');
                    this.setPreviousStatement(true, null);
                  this.setColour(230);
              this.setTooltip("");
              this.setHelpUrl("");
              }
            };
         