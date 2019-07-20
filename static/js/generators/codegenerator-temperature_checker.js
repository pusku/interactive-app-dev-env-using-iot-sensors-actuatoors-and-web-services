
            Blockly.Python['temperature_checker'] = function(block) {
              var value_to_input = Blockly.Python.valueToCode(block, 'to_input', Blockly.Python.ORDER_ATOMIC);
              var code = 'temperature_checker('+value_to_input+')';
              return [code, Blockly.Python.ORDER_NONE];
            };
        