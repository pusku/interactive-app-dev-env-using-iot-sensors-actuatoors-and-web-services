
            Blockly.Python['test 1'] = function(block) {
                var param0 = Blockly.Python.valueToCode(block, 'param0', Blockly.Python.ORDER_ATOMIC);var param1 = Blockly.Python.valueToCode(block, 'param1', Blockly.Python.ORDER_ATOMIC);

                var code = 'test 1('+param0+','+param1+')';
                return [code, Blockly.Python.ORDER_NONE];
            };
        