// module adapted from Terasic DECA HDMI_TX example
//
// --------------------------------------------------------------------
// Copyright (c) 2007 by Terasic Technologies Inc.
// --------------------------------------------------------------------
//
// Permission:
//
//   Terasic grants permission to use and modify this code for use
//   in synthesis for all Terasic Development Boards and Altera Development
//   Kits made by Terasic.  Other use of this code, including the selling
//   ,duplication, or modification of any portion is strictly prohibited.
//
// Disclaimer:
//
//   This VHDL/Verilog or C/C++ source code is intended as a design reference
//   which illustrates how these types of functions can be implemented.
//   It is the user's responsibility to verify their design for
//   consistency and functionality through the use of formal
//   verification methods.  Terasic provides no warranty regarding the use
//   or functionality of this code.
//
// --------------------------------------------------------------------
//
//                     Terasic Technologies Inc
//                     356 Fu-Shin E. Rd Sec. 1. JhuBei City,
//                     HsinChu County, Taiwan
//                     302
//
//                     web: http://www.terasic.com/
//                     email: support@terasic.com
//
// --------------------------------------------------------------------

module hdmi_generator(
    input              clk,
    input              reset_n,
    output  reg		     vga_hs,
    output  reg        vga_vs,
    output  reg 	     vga_de,

    output    [5:0]    comp_v_hdmi     //foggy generator
  );

  // VIDEO FOGGY EFFECT GENERATOR 
  reg  [22:0] rnd_reg;
  wire [5:0]  rnd_c = {rnd_reg[0],rnd_reg[1],rnd_reg[2],rnd_reg[2],rnd_reg[2],rnd_reg[2]};
  wire [22:0] rnd;
  wire [7:0]  cos_out;
  wire [5:0]  cos_g;
  reg  [9:0]  vvc;

  lfsr random(rnd);

  cos cos2(vvc + v_count, cos_out);
  assign cos_g = cos_out[7:3]+6'd32;

  assign comp_v_hdmi = (cos_g >= rnd_c) ? cos_g - rnd_c : 6'd0;
  // end foggy generator
  

  //=======================================================
  //  Structural coding
  //=======================================================
  //============= assign timing constant
  //h_total : total - 1
  //h_sync : sync - 1
  //h_start : sync + back porch - 1 - 2(delay)
  //h_end : h_start + avtive
  //v_total : total - 1
  //v_sync : sync - 1
  //v_start : sync + back porch - 1
  //v_end : v_start + avtive
  //v_active_14 : v_start + 1/4 avtive
  //v_active_24 : v_start + 2/4 avtive
  //v_active_34 : v_start + 3/4 avtive

  wire  [11:0] h_total, h_sync, h_start, h_end;
  wire  [11:0] v_total, v_sync, v_start, v_end;

  // SELECT VIDEO MODE.  REMEMBER TO CHANGE ALSO VIDEO PLL ACCORDING TO EACH MODE FREQUENCY

  //640x480@60 25.175 MHZ
  //assign {h_total, h_sync, h_start, h_end} = {12'd799, 12'd95, 12'd141, 12'd781};
  //assign {v_total, v_sync, v_start, v_end} = {12'd524, 12'd1, 12'd34, 12'd514};

  //720x480@60 27MHZ (VIC=3, 480P)
  assign {h_total, h_sync, h_start, h_end} = {12'd857, 12'd61, 12'd119, 12'd839};
  assign {v_total, v_sync, v_start, v_end} = {12'd524, 12'd5, 12'd35, 12'd515};

  //1024x768@60 65MHZ (XGA)
  //assign {h_total, h_sync, h_start, h_end} = {12'd1343, 12'd135, 12'd293, 12'd1317};
  //assign {v_total, v_sync, v_start, v_end} = {12'd805, 12'd5, 12'd34, 12'd802};

  //1280x1024@60   108MHZ (SXGA)
  //assign {h_total, h_sync, h_start, h_end} = {12'd1687, 12'd111, 12'd357, 12'd1637};
  //assign {v_total, v_sync, v_start, v_end} = {12'd1065, 12'd2, 12'd40, 12'd1064};

  //1920x1080p60 148.5MHZ
  //assign {h_total, h_sync, h_start, h_end} = {12'd2199, 12'd43, 12'd189, 12'd2109};
  //assign {v_total, v_sync, v_start, v_end} = {12'd1124, 12'd4, 12'd40, 12'd1120};

  //1600x1200p60 162MHZ (VESA)
  //assign {h_total, h_sync, h_start, h_end} = {12'd2159, 12'd191, 12'd493, 12'd2093};
  //assign {v_total, v_sync, v_start, v_end} = {12'd1249, 12'd2, 12'd48, 12'd1248};


  //  Signal declarations
  reg			  [9:0]	  h_count;
  reg			  [9:0]	  v_count;
  reg               h_act;
  reg               v_act;
  reg               pre_vga_de;
  wire              h_max, hs_end, hr_start, hr_end;
  wire              v_max, vs_end, vr_start, vr_end;

  //  Assignments
  assign h_max = h_count == h_total;
  assign hs_end = h_count >= h_sync;
  assign hr_start = h_count == h_start;
  assign hr_end = h_count == h_end;
  assign v_max = v_count == v_total;
  assign vs_end = v_count >= v_sync;
  assign vr_start = v_count == v_start;
  assign vr_end = v_count == v_end;

  //horizontal control signals
  always @ (posedge clk or negedge reset_n)
    if (!reset_n)
      begin
        h_count		<=	10'b0;
        vga_hs		<=	1'b1;
        h_act	    <=	1'b0;
      end
    else
      begin
        if (h_max)
          h_count	<= 10'b0;
        else
          h_count	<= h_count + 10'b1;

        if (hs_end && !h_max)
          vga_hs	<=	1'b1;
        else
          vga_hs	<= 1'b0;

        if (hr_start)
          h_act	  <=	1'b1;
        else if (hr_end)
          h_act	  <=	1'b0;

      end

  //vertical control signals
  always@(posedge clk or negedge reset_n)
    if(!reset_n)
      begin
        v_count		<=	10'b0;
        vga_vs		<=	1'b1;
        v_act	    <=	1'b0;
      end
    else
      begin
        if (h_max)
        begin
          if (v_max)
            begin
              v_count	<=	10'b0;
              vvc <= vvc + 10'd6;     //foggy generator
            end
          else
            v_count	<=	v_count + 10'b1;

          if (vs_end && !v_max)
            vga_vs	<=	1'b1;
          else
            vga_vs	<=	1'b0;

          if (vr_start)
            v_act <=	1'b1;
          else if (vr_end)
            v_act <=	1'b0;
        end

        rnd_reg <= rnd;               //foggy generator
      end

  //display enable
  always @(posedge clk or negedge reset_n)
  begin
    if (!reset_n)
    begin
      vga_de <= 1'b0;
      pre_vga_de <= 1'b0;
    end
    else
    begin
      vga_de <= pre_vga_de;
      pre_vga_de <= v_act && h_act;
    end
  end

endmodule
