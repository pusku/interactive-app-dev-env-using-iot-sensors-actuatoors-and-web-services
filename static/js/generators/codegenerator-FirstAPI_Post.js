
            Blockly.Python['FirstAPI_Post'] = function(block) {
              var param = Blockly.Python.valueToCode(block, 'param', Blockly.Python.ORDER_ATOMIC);
              var param2 = Blockly.Python.valueToCode(block, 'param2', Blockly.Python.ORDER_ATOMIC);
              var code = 'FirstAPI_Post('+param+','+param2+')';
              return [code, Blockly.Python.ORDER_NONE];
            };
        