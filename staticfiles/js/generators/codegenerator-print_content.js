// Blockly.Python['print_content'] = function(Block) {
//     var code = 'print_content('+item+')';
//     return code;
//   }
Blockly.Python['print_content'] = function(block) {
  var value_to_print = Blockly.Python.valueToCode(block, 'to_print', Blockly.Python.ORDER_ATOMIC);
  // TODO: Assemble Python into code variable.
  var code = 'print_content('+value_to_print+')';
  return code;
};