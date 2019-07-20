
            Blockly.Python['FirstAPI_Search'] = function(block) {
              var value_to_input = Blockly.Python.valueToCode(block, 'to_input', Blockly.Python.ORDER_ATOMIC);
              var code = 'FirstAPI_Search('+value_to_input+')';
              return [code, Blockly.Python.ORDER_NONE];
            };
        