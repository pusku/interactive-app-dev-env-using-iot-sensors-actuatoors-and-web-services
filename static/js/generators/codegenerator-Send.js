Blockly.Python['Send'] = function(block) {
  var value_param = Blockly.Python.valueToCode(block, 'param', Blockly.Python.ORDER_ATOMIC);
  var value_param2 = Blockly.Python.valueToCode(block, 'param2', Blockly.Python.ORDER_ATOMIC);
  var value_param3 = Blockly.Python.valueToCode(block, 'param3', Blockly.Python.ORDER_ATOMIC);
  var value_param4 = Blockly.Python.valueToCode(block, 'param4', Blockly.Python.ORDER_ATOMIC);
  var value_param5 = Blockly.Python.valueToCode(block, 'param5', Blockly.Python.ORDER_ATOMIC);
  var code = 'Send('+value_param+','+value_param2+','+value_param3+','+value_param4+','+value_param5+')';
  return [code, Blockly.Python.ORDER_NONE];
};