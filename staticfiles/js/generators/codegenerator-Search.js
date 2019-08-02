Blockly.Python['Search'] = function(block) {
  var param = Blockly.Python.valueToCode(block, 'param', Blockly.Python.ORDER_ATOMIC);
  var param2 = Blockly.Python.valueToCode(block, 'param2', Blockly.Python.ORDER_ATOMIC);
  var param3 = Blockly.Python.valueToCode(block, 'param3', Blockly.Python.ORDER_ATOMIC);
  var code = 'Search('+param+', '+param2+', '+param3+')';
  return [code, Blockly.Python.ORDER_NONE];
};