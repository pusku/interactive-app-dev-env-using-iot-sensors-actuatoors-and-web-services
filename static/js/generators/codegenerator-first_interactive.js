
            Blockly.Python['first_interactive'] = function(block) {var param0 = Blockly.Python.valueToCode(block, 'param0', Blockly.Python.ORDER_ATOMIC);
var param1 = Blockly.Python.valueToCode(block, 'param1', Blockly.Python.ORDER_ATOMIC);
var param2 = Blockly.Python.valueToCode(block, 'param2', Blockly.Python.ORDER_ATOMIC);

                var code = 'first_interactive('+param0+','+param1+','+param2+')';
                return [code, Blockly.Python.ORDER_NONE];
            };
        