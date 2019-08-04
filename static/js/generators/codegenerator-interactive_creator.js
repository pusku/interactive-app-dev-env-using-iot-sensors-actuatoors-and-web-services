Blockly.Python['interactive_creator'] = function (block) {
    var param0 = Blockly.Python.valueToCode(block, 'name', Blockly.Python.ORDER_ATOMIC);
    var param1 = Blockly.Python.valueToCode(block, 'fields', Blockly.Python.ORDER_ATOMIC);
    var code = 'interactive_creator(' + param0 + ', ' + param1 + ')';
    return [code, Blockly.Python.ORDER_NONE];
};