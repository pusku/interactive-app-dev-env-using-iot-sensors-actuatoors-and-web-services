Blockly.Python['Read'] = function(block) {
  var param = Blockly.Python.valueToCode(block, 'param', Blockly.Python.ORDER_ATOMIC);
  var param2 = Blockly.Python.valueToCode(block, 'param2', Blockly.Python.ORDER_ATOMIC);
  var code = 'Read('+param+','+param2+')';
  return [code, Blockly.Python.ORDER_NONE];
};