////////////////////////////////////////////////////////////////////////////////
//
//
//
//  MENU for MIST board
//  (C) 2016 Sorgelig
//
//
//
////////////////////////////////////////////////////////////////////////////////

module menu
    (
        input         iCLK,   // Input clock 50 MHz

	    input         key0,

        output  [2:0] VGA_R_o,
        output  [2:0] VGA_G_o,
        output  [2:0] VGA_B_o,
        output        VGA_HS,
        output        VGA_VS,

        output        LED,

        input         SPI_SCK,
        output        SPI_DO,
        input         SPI_DI,
        input         SPI_SS3,
        input         CONF_DATA0,

        output [12:0] SDRAM_A,
        inout  [15:0] SDRAM_DQ,
        output        SDRAM_DQML,
        output        SDRAM_DQMH,
        output        SDRAM_nWE,
        output        SDRAM_nCAS,
        output        SDRAM_nRAS,
        output        SDRAM_nCS,
        output  [1:0] SDRAM_BA,
        output        SDRAM_CLK,
        output        SDRAM_CKE,
  
        // HDMI-TX  DECA 
        inout 		  	HDMI_I2C_SCL,
        inout 		  	HDMI_I2C_SDA,
        // inout 	[3:0]	HDMI_I2S,
        // inout 		 	HDMI_LRCLK,
        // inout 		 	HDMI_MCLK,
        // inout 		  	HDMI_SCLK,
        output		  	HDMI_TX_CLK,
        output	[23:0]	HDMI_TX_D,
        output		    HDMI_TX_DE,    
        output		    HDMI_TX_HS,
        input 		    HDMI_TX_INT,
        output		    HDMI_TX_VS

    );

    wire clk_x2, clk_pix, clk_ram, locked;
    pll pll
        (
            .inclk0(iCLK),
            .c0(clk_ram),
            .c1(SDRAM_CLK),
            .c2(clk_x2),
            .c3(clk_pix),
            .locked(locked)
        );

    //adapting to 3 bits VGA addon
    wire  [5:0] VGA_R;
    wire  [5:0] VGA_G;
    wire  [5:0] VGA_B;
    assign VGA_R_o = VGA_R[5:3];
    assign VGA_G_o = VGA_G[5:3];
    assign VGA_B_o = VGA_B[5:3];


    //______________________________________________________________________________
    //
    // MIST ARM I/O
    //
    wire		   scandoubler_disable;
    wire		   ypbpr;

    user_io #(.STRLEN(6)) user_io
            (
                .conf_str("MENU;;"),

                .SPI_SCK(SPI_SCK),
                .CONF_DATA0(CONF_DATA0),
                .SPI_DO(SPI_DO),
                .SPI_DI(SPI_DI),
                .scandoubler_disable(scandoubler_disable),
                .ypbpr(ypbpr)
            );

    assign LED = 1'b0;

    // sram ram
    //      (
    //          .*,
    //          .init(~locked),
    //          .clk(clk_ram),
    //          .wtbt(3),
    //          .dout(),
    //          .din(0),
    //          .rd(0),
    //          .ready()
    //      );

    // reg        we;
    // reg [24:0] addr = 0;
    // integer   init = 5000000;
    // reg [4:0] cnt = 9;
    
    // always @(posedge clk_ram)
    // begin
    //     if(init)
    //         init <= init - 1;
    //     else
    //     begin
    //         cnt <= cnt + 1'b1;
    //         we <= &cnt;
    //         if(cnt == 8)
    //             addr <= addr + 1'd1;
    //     end
    // end

    //______________________________________________________________________________
    //
    // Video
    //

    reg  [9:0] hc;
    reg  [8:0] vc;
    reg  [9:0] vvc;

    reg [22:0] rnd_reg;
    wire [5:0] rnd_c = {rnd_reg[0],rnd_reg[1],rnd_reg[2],rnd_reg[2],rnd_reg[2],rnd_reg[2]};

    wire [22:0] rnd;
    lfsr random(rnd);

    always @(negedge clk_pix)
    begin
        if(hc == 639)
        begin
            hc <= 0;
            if(vc == 311)
            begin
                vc <= 0;
                vvc <= vvc + 10'd6;
            end
            else
            begin
                vc <= vc + 1'd1;
            end
        end
        else
        begin
            hc <= hc + 1'd1;
        end

        rnd_reg <= rnd;
    end

    reg  HBlank;
    reg  HSync;
    reg  VBlank;
    reg  VSync;
    wire viden  = !HBlank && !VBlank;

    always @(posedge clk_pix)
    begin
        if (hc == 310)
            HBlank <= 1;
        else if (hc == 420)
            HBlank <= 0;

        if (hc == 336)
            HSync <= 1;
        else if (hc == 368)
            HSync <= 0;

        if(vc == 308)
            VSync <= 1;
        else if (vc == 0)
            VSync <= 0;

        if(vc == 306)
            VBlank <= 1;
        else if (vc == 2)
            VBlank <= 0;
    end


    reg  [7:0] cos_out;
    wire [5:0] cos_g = cos_out[7:3]+6'd32;
    cos cos(vvc + {vc, 1'b0}, cos_out);

    wire [5:0] comp_v = (cos_g >= rnd_c) ? cos_g - rnd_c : 6'd0;
    wire [5:0] R_in = !viden ? 6'd0 : comp_v;
    wire [5:0] G_in = !viden ? 6'd0 : comp_v;
    wire [5:0] B_in = !viden ? 6'd0 : comp_v;


    wire [5:0] R_out, G_out, B_out;

    osd osd
        (
            .*,
            .OSD_X_OFFSET(10'd10),
            .OSD_Y_OFFSET(10'd0),
            .OSD_COLOR(3'd4)
        );

    wire hs_out, vs_out;
    wire [5:0] r_out, g_out, b_out;

    scandoubler scandoubler
                (
                    .*,
                    .scanlines(2'b00),
                    .hs_in(HSync),
                    .vs_in(VSync),
                    .r_in(R_out),
                    .g_in(G_out),
                    .b_in(B_out)
                );

    video_mixer video_mixer
                (
                    .*,
                    .ypbpr_full(1),

                    .r_i({R_out, R_out[5:4]}),
                    .g_i({G_out, G_out[5:4]}),
                    .b_i({B_out, B_out[5:4]}),
                    .hsync_i(HSync),
                    .vsync_i(VSync),

                    .r_p({r_out, r_out[5:4]}),
                    .g_p({g_out, g_out[5:4]}),
                    .b_p({b_out, b_out[5:4]}),
                    .hsync_p(hs_out),
                    .vsync_p(vs_out)
                );


    /////////////////////////////////
    //// DECA HDMI & AUDIO CODEC ////
    /////////////////////////////////

    //  HDMI I2C CONFIG
    I2C_HDMI_Config u_I2C_HDMI_Config (
        .iCLK		(iCLK         ),
        .iRST_N		(reset_n      ),			
        .I2C_SCLK	(HDMI_I2C_SCL ),
        .I2C_SDAT	(HDMI_I2C_SDA ),
        .HDMI_TX_INT(HDMI_TX_INT  )
        );

    //  HDMI VIDEO   
    // assign HDMI_TX_CLK = clk_x2;    
    // assign HDMI_TX_DE = viden;
    // assign HDMI_TX_HS = !VGA_HS;   
    // assign HDMI_TX_VS = !VGA_VS;   
    // assign HDMI_TX_D  = {R_in,3'b0,G_in,3'b0,B_in,3'b0};  	  		 


    // vpg.v
    wire  vpg_pclk;
    wire  vpg_de_out;
    wire  vpg_hs_out, vpg_vs_out;
    wire  [5:0] vpg_r_out, vpg_g_out, vpg_b_out;
    wire  [5:0] comp_v_hdmi;
    wire  reset_n;

    assign reset_n = key0;   //1'b1


    pll2 u_pll (
            .inclk0(iCLK),
            .areset(!reset_n),
            .c0(vpg_pclk)
        );


    //=============== hs/vs/de generator according to vga timing
    hdmi_generator u_hdmi_generator (
                    .clk(vpg_pclk),
                    .reset_n(reset_n),
                    .vga_hs(vpg_hs_out),
                    .vga_vs(vpg_vs_out),
                    .vga_de(vpg_de_out),
                    .comp_v_hdmi(comp_v_hdmi)
                );

    //  HDMI VIDEO   
    // assign HDMI_TX_CLK = ~vpg_pclk;    
    // assign HDMI_TX_DE = vpg_de_out;
    // assign HDMI_TX_HS = vpg_hs_out;   
    // assign HDMI_TX_VS = vpg_vs_out;   
    // assign HDMI_TX_D  = {vpg_r_out,vpg_g_out,vpg_b_out};  	  

    assign vpg_r_out = !vpg_de_out ? 6'd0 : comp_v_hdmi;
    assign vpg_g_out = !vpg_de_out ? 6'd0 : comp_v_hdmi ;
    assign vpg_b_out = !vpg_de_out ? 6'd0 : comp_v_hdmi;

    wire [5:0] R_out2, G_out2, B_out2;

    osd  osd_hdmi (
        .clk_pix (vpg_pclk ),
        .scandoubler_disable (scandoubler_disable ),
        .OSD_X_OFFSET (10'd10 ),
        .OSD_Y_OFFSET (10'd0 ),
        .OSD_COLOR (3'd4 ),
        .SPI_SCK (SPI_SCK ),
        .SPI_SS3 (SPI_SS3 ),
        .SPI_DI (SPI_DI ),
        .R_in (vpg_r_out ),
        .G_in (vpg_g_out ),
        .B_in (vpg_b_out ),
        .HSync (vpg_hs_out ),
        .VSync (vpg_vs_out ),
        .R_out (R_out2 ),
        .G_out (G_out2 ),
        .B_out (B_out2 )
    );

    //  HDMI VIDEO   
    // assign HDMI_TX_CLK = ~vpg_pclk;    
    // assign HDMI_TX_DE = vpg_de_out;
    // assign HDMI_TX_HS = vpg_hs_out;   
    // assign HDMI_TX_VS = vpg_vs_out;   
    // assign HDMI_TX_D  = {R_out2,R_out2[5:4],G_out2,G_out2[5:4],B_out2,B_out2[5:4]};  	  


    wire [5:0] R_out3, G_out3, B_out3;
    // wire vpg_hs_out3, vpg_vs_out3;

    video_mixer video_mixer_hdmi
                (
                    .scandoubler_disable (1),     // 0 = HVSync 31KHz, 1 = CSync 15KHz
                    .ypbpr(ypbpr),
                    .ypbpr_full(1),

                    .r_i({R_out2, R_out2[5:4]}),
                    .g_i({G_out2, G_out2[5:4]}),
                    .b_i({B_out2, B_out2[5:4]}),
                    .hsync_i(vpg_hs_out),
                    .vsync_i(vpg_vs_out),

                    .r_p(),
                    .g_p(),
                    .b_p(),
                    .hsync_p(),
                    .vsync_p(),

                    .VGA_R(R_out3),
                    .VGA_G(G_out3),
                    .VGA_B(B_out3)
                    //.VGA_VS(vpg_vs_out3),
                    //.VGA_HS(vpg_hs_out3)
                );

    //  HDMI VIDEO   
    assign HDMI_TX_CLK = ~vpg_pclk;    
    assign HDMI_TX_DE = vpg_de_out;
    assign HDMI_TX_HS = vpg_hs_out;   //vpg_hs_out3   using hs/vs from video mixer does not work
    assign HDMI_TX_VS = vpg_vs_out;   //vpg_vs_out3
    assign HDMI_TX_D  = {R_out3,R_out3[5:4],G_out3,G_out3[5:4],B_out3,B_out3[5:4]};  	  


endmodule
