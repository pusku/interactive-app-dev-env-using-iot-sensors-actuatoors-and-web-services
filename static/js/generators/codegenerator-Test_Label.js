
            Blockly.Python['Test_Label'] = function(block) {
              var value_to_input = Blockly.Python.valueToCode(block, 'to_input', Blockly.Python.ORDER_ATOMIC);
              var code = 'Test_Label('+value_to_input+')';
              return [code, Blockly.Python.ORDER_NONE];
            };
        