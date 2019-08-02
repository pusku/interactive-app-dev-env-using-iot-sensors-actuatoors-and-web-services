Blockly.Python['place_finder'] = function(block) {
  var value_to_input = Blockly.Python.valueToCode(block, 'param', Blockly.Python.ORDER_ATOMIC);
  var code = 'place_finder('+value_to_input+')';
  return [code, Blockly.Python.ORDER_NONE];
};