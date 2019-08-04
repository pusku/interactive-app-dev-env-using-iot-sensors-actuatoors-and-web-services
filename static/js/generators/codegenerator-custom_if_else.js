Blockly.Python['custom_if_else'] = function (block) {
    var param0 = Blockly.Python.valueToCode(block, 'left', Blockly.Python.ORDER_ATOMIC);
    var param1 = Blockly.Python.statementToCode(block, 'inner');
    var param2 = Blockly.Python.statementToCode(block, 'else');

    var code = 'custom_if_else(' + param0 + ',' + param1 + ',' + param2 + ')';
    return [code, Blockly.Python.ORDER_NONE];
};