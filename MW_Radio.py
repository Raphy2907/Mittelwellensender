#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.5.1

from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import network




class MW_Radio(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 16000
        self.samp_rate_if = samp_rate_if = samp_rate*20
        self.samp_rate_hf = samp_rate_hf = samp_rate_if*8

        ##################################################
        # Blocks
        ##################################################

        self.rational_resampler_xxx_2 = filter.rational_resampler_fff(
                interpolation=4,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=8,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0_2 = filter.rational_resampler_fff(
                interpolation=20,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0_1 = filter.rational_resampler_fff(
                interpolation=20,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_fff(
                interpolation=20,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=20,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.network_udp_source_0_2 = network.udp_source(gr.sizeof_float, 1, 5010, 0, 1472, False, False, False)
        self.network_udp_source_0_1 = network.udp_source(gr.sizeof_float, 1, 5008, 0, 1472, False, False, False)
        self.network_udp_source_0_0 = network.udp_source(gr.sizeof_float, 1, 5006, 0, 1472, False, False, False)
        self.network_udp_source_0 = network.udp_source(gr.sizeof_float, 1, 5004, 0, 1472, False, False, False)
        self.network_tcp_sink_0 = network.tcp_sink(gr.sizeof_char, 1, '127.0.0.1', 1234,2)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_2 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(0.6)
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 128)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.blocks_add_const_vxx_0_2 = blocks.add_const_ff(1.5)
        self.blocks_add_const_vxx_0_1 = blocks.add_const_ff(1.5)
        self.blocks_add_const_vxx_0_0 = blocks.add_const_ff(1.5)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff(1.5)
        self.band_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate_hf,
                875000,
                1000000,
                50000,
                window.WIN_HAMMING,
                6.76))
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate_hf, analog.GR_COS_WAVE, 815000, 1, 0, 0)
        self.analog_sig_source_x_0_2 = analog.sig_source_f(samp_rate_if, analog.GR_COS_WAVE, 150000, 1, 0, 0)
        self.analog_sig_source_x_0_1 = analog.sig_source_f(samp_rate_if, analog.GR_COS_WAVE, 130000, 1, 0, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate_if, analog.GR_COS_WAVE, 110000, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate_if, analog.GR_COS_WAVE, 90000, 1, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_multiply_xx_0_1, 1))
        self.connect((self.analog_sig_source_x_0_2, 0), (self.blocks_multiply_xx_0_2, 1))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_add_const_vxx_0_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.blocks_add_const_vxx_0_1, 0), (self.rational_resampler_xxx_0_1, 0))
        self.connect((self.blocks_add_const_vxx_0_2, 0), (self.rational_resampler_xxx_0_2, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.blocks_float_to_char_0, 0), (self.network_tcp_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.rational_resampler_xxx_2, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_multiply_xx_0_2, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.blocks_multiply_xx_1, 0), (self.band_pass_filter_0, 0))
        self.connect((self.network_udp_source_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.network_udp_source_0_0, 0), (self.blocks_add_const_vxx_0_0, 0))
        self.connect((self.network_udp_source_0_1, 0), (self.blocks_add_const_vxx_0_1, 0))
        self.connect((self.network_udp_source_0_2, 0), (self.blocks_add_const_vxx_0_2, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_1, 0), (self.blocks_multiply_xx_0_1, 0))
        self.connect((self.rational_resampler_xxx_0_2, 0), (self.blocks_multiply_xx_0_2, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.rational_resampler_xxx_2, 0), (self.blocks_float_to_char_0, 0))


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_samp_rate_if(self.samp_rate*20)

    def get_samp_rate_if(self):
        return self.samp_rate_if

    def set_samp_rate_if(self, samp_rate_if):
        self.samp_rate_if = samp_rate_if
        self.set_samp_rate_hf(self.samp_rate_if*8)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate_if)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate_if)
        self.analog_sig_source_x_0_1.set_sampling_freq(self.samp_rate_if)
        self.analog_sig_source_x_0_2.set_sampling_freq(self.samp_rate_if)

    def get_samp_rate_hf(self):
        return self.samp_rate_hf

    def set_samp_rate_hf(self, samp_rate_hf):
        self.samp_rate_hf = samp_rate_hf
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate_hf)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate_hf, 875000, 1000000, 50000, window.WIN_HAMMING, 6.76))




def main(top_block_cls=MW_Radio, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    try:
        input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
