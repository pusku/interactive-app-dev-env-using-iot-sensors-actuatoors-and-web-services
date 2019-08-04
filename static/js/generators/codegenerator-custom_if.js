Blockly.Python['custom_if'] = function (block) {
    var param0 = Blockly.Python.valueToCode(block, 'left', Blockly.Python.ORDER_ATOMIC);
    var param1 = Blockly.Python.statementToCode(block, 'inner');

    var code = 'custom_if(' + param0 + ',' + param1 + ')';
    return [code, Blockly.Python.ORDER_NONE];
};