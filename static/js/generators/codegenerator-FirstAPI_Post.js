
            Blockly.Python['FirstAPI_Post'] = function(block) {
              var value_to_input = Blockly.Python.valueToCode(block, 'to_input', Blockly.Python.ORDER_ATOMIC);
              var code = 'FirstAPI_Post('+value_to_input+')';
              return [code, Blockly.Python.ORDER_NONE];
            };
        