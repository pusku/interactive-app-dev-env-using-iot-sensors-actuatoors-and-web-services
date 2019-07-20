
            Blockly.Python['Test_Send'] = function(block) {
              var value_to_input = Blockly.Python.valueToCode(block, 'to_input', Blockly.Python.ORDER_ATOMIC);
              var code = 'Test_Send('+value_to_input+')';
              return [code, Blockly.Python.ORDER_NONE];
            };
        