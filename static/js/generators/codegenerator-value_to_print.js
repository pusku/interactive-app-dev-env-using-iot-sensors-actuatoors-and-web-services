// Blockly.JavaScript['value_to_print'] = function(block) {
//   var text_name = block.getFieldValue('NAME');
//   var value_value_to_print = Blockly.JavaScript.valueToCode(block, 'value_to_print', Blockly.JavaScript.ORDER_ATOMIC);
//   // TODO: Assemble JavaScript into code variable.
//   var code = 'value_to_print('+value_value_to_print+')';
//   // TODO: Change ORDER_NONE to the correct strength.
//   return [code, Blockly.JavaScript.ORDER_NONE];
// };

Blockly.Python['value_to_print'] = function(block) {
  var value_to_input = Blockly.Python.valueToCode(block, 'to_input', Blockly.Python.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'value_to_print('+value_to_input+')';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};