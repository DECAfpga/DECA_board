/*
A clock divider in Verilog
*/

module deca_top(
  input MAX10_CLK1_50,
  input [1:0] KEY,
  output reg JOYX_SEL_O
);

  // simple ripple clock divider
  
  always @(posedge MAX10_CLK1_50)
    JOYX_SEL_O <= KEY[0] ? 1'b0 : ~JOYX_SEL_O;

endmodule
