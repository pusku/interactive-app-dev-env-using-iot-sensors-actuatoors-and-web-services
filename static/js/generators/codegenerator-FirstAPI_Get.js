
            Blockly.Python['FirstAPI_Get'] = function(block) {
              var value_to_input = Blockly.Python.valueToCode(block, 'param', Blockly.Python.ORDER_ATOMIC);
              var code = 'FirstAPI_Get('+value_to_input+')';
              return [code, Blockly.Python.ORDER_NONE];
            };
        