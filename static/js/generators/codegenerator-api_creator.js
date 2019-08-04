Blockly.Python['api_creator'] = function (block) {
    var param0 = Blockly.Python.valueToCode(block, 'name', Blockly.Python.ORDER_ATOMIC);
    var param1 = Blockly.Python.valueToCode(block, 'api', Blockly.Python.ORDER_ATOMIC);
    var param2 = Blockly.Python.valueToCode(block, 'fields', Blockly.Python.ORDER_ATOMIC);
    var param3 = Blockly.Python.valueToCode(block, 'connection', Blockly.Python.ORDER_ATOMIC);

    var code = 'api_creator(' + param0 + ',' + param1 + ',' + param2 + ',' + param3 + ')';
    return [code, Blockly.Python.ORDER_NONE];
};