Blockly.Blocks['Label'] = {
  init: function() {
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
      
Blockly.Blocks['Read'] = {
  init: function() {
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
  init: function() {
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
  init: function() {
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
           
            Blockly.Blocks['temperature_checker'] = {
            init: function() {
            this.appendValueInput("to_input")
            .setCheck(null)
            .appendField('temperature_checker');
            this.setOutput(true, null);
            this.setColour(230);
            this.setTooltip("");
            this.setHelpUrl("");
      }
    };
        
                  Blockly.Blocks['Rajon'] = {
                  init: function() {
                  this.appendValueInput("to_input")
                  .setCheck(null)
                  .appendField('Rajon');
                  this.setOutput(true, null);
                  this.setColour(230);
                  this.setTooltip("");
                  this.setHelpUrl("");
            }
          };
              
                         Blockly.Blocks['FirstAPI_Post'] = {
                            init: function() {
                              this.appendValueInput("param")
                                  .setCheck(null)
                                  .setAlign(Blockly.ALIGN_CENTRE)
                                  .appendField('FirstAPI_Post');
                              this.appendValueInput("param2")
                                  .setCheck(null);
                              this.setPreviousStatement(true, null);
                              this.setColour(230);
                          this.setTooltip("");
                          this.setHelpUrl("");
                          }
                        };
                   

                   Blockly.Blocks['FirstAPI_Search'] = {
                        init: function() {
                          this.appendValueInput("param")
                              .setCheck(null)
                              .appendField('FirstAPI_Search');
                          this.setPreviousStatement(true, null);
                          this.setColour(230);
                      this.setTooltip("");
                      this.setHelpUrl("");
                        }
                      };
                 
                 Blockly.Blocks['FirstAPI_Get'] = {
                         init: function() {
                          this.appendValueInput("param")
                              .setCheck(null)
                              .appendField('FirstAPI_Get');
                          this.setPreviousStatement(true, null);
                          this.setColour(230);
                      this.setTooltip("");
                      this.setHelpUrl("");
                   }
                 };
                     