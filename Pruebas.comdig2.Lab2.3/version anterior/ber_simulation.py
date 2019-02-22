#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: BER Simulation
# Author: Example
# Description: Adjust the noise and constellation... see what happens!
# Generated: Wed Feb 20 19:01:26 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import math
import numpy
import sip
import sys
import wform  # embedded python module
from gnuradio import qtgui


class ber_simulation(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "BER Simulation")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("BER Simulation")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "ber_simulation")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.const = const = [(1+1.j)/4.24,(3+1.j)/4.24,(3+3.j)/4.24,(1+3.j)/4.24,(-1+1.j)/4.24,(-3+1.j)/4.24,(-3+3.j)/4.24,(-1+3.j)/4.24,(-1-1.j)/4.24,(-3-1.j)/4.24,(-3-3.j)/4.24,(-1-3.j)/4.24,(1-1.j)/4.24,(3-1.j)/4.24,(3-3.j)/4.24,(1-3.j)/4.24]
        self.samp_rate = samp_rate = 100e3
        self.Sps = Sps = 16
        self.M = M = len(const)
        self.rolloff = rolloff = 0.35
        self.ntaps = ntaps = 128
        self.Rs = Rs = samp_rate/Sps
        self.Bps = Bps = int(math.log(M,2))
        self.hrc = hrc = wform.rcos(Sps,ntaps,rolloff)
        self.hr = hr = wform.rect(Sps,ntaps)
        self.hn = hn = wform.nyq(Sps,ntaps)
        self.Rb = Rb = Rs*Bps

        self.MiconstellationObject = MiconstellationObject = digital.constellation_calcdist((const), (), 4, 1).base()

        self.EbN0 = EbN0 = 14.

        ##################################################
        # Blocks
        ##################################################
        self._EbN0_range = Range(-10, 40, 1, 14., 200)
        self._EbN0_win = RangeWidget(self._EbN0_range, self.set_EbN0, 'Eb / N0 (dB)', "counter_slider", float)
        self.top_grid_layout.addWidget(self._EbN0_win)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("")

        labels = ['BER', '', '', '', '',
                  '', '', '', '', '']
        units = ['x10^-6', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1e6, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, 0)
            self.qtgui_number_sink_0.set_max(i, 1)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(True)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"foo", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [0.6, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.interp_fir_filter_xxx_0_0_0 = filter.interp_fir_filter_ccc(Sps, (hr))
        self.interp_fir_filter_xxx_0_0_0.declare_sample_delay(0)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(MiconstellationObject)
        self.digital_chunks_to_symbols_xx = digital.chunks_to_symbols_bc((const), 1)
        self.blocks_throttle = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_add_xx = blocks.add_vcc(1)
        self.blks2_error_rate = grc_blks2.error_rate(
        	type='BER',
        	win_size=int(1e7),
        	bits_per_symbol=Bps,
        )
        self.analog_random_source_x = blocks.vector_source_b(map(int, numpy.random.randint(0, M, 10000000)), True)
        self.analog_noise_source_x = analog.noise_source_c(analog.GR_GAUSSIAN, 1.0 / math.sqrt(2.0 * Bps * 10**(EbN0/10)), 42)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x, 0), (self.blocks_add_xx, 1))
        self.connect((self.analog_random_source_x, 0), (self.blocks_throttle, 0))
        self.connect((self.blks2_error_rate, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.blocks_add_xx, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.blocks_add_xx, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.blocks_throttle, 0), (self.blks2_error_rate, 0))
        self.connect((self.blocks_throttle, 0), (self.digital_chunks_to_symbols_xx, 0))
        self.connect((self.digital_chunks_to_symbols_xx, 0), (self.blocks_add_xx, 0))
        self.connect((self.digital_chunks_to_symbols_xx, 0), (self.interp_fir_filter_xxx_0_0_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.blks2_error_rate, 1))
        self.connect((self.interp_fir_filter_xxx_0_0_0, 0), (self.blocks_null_sink_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ber_simulation")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_const(self):
        return self.const

    def set_const(self, const):
        self.const = const
        self.set_M(len(self.const))
        self.digital_chunks_to_symbols_xx.set_symbol_table((self.const))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle.set_sample_rate(self.samp_rate)
        self.set_Rs(self.samp_rate/self.Sps)

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_hr(wform.rect(self.Sps,self.ntaps))
        self.set_hrc(wform.rcos(self.Sps,self.ntaps,self.rolloff))
        self.set_hn(wform.nyq(self.Sps,self.ntaps))
        self.set_Rs(self.samp_rate/self.Sps)

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.set_Bps(int(math.log(self.M,2)))

    def get_rolloff(self):
        return self.rolloff

    def set_rolloff(self, rolloff):
        self.rolloff = rolloff
        self.set_hrc(wform.rcos(self.Sps,self.ntaps,self.rolloff))

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.set_hr(wform.rect(self.Sps,self.ntaps))
        self.set_hrc(wform.rcos(self.Sps,self.ntaps,self.rolloff))
        self.set_hn(wform.nyq(self.Sps,self.ntaps))

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs
        self.set_Rb(self.Rs*self.Bps)

    def get_Bps(self):
        return self.Bps

    def set_Bps(self, Bps):
        self.Bps = Bps
        self.analog_noise_source_x.set_amplitude(1.0 / math.sqrt(2.0 * self.Bps * 10**(self.EbN0/10)))
        self.set_Rb(self.Rs*self.Bps)

    def get_hrc(self):
        return self.hrc

    def set_hrc(self, hrc):
        self.hrc = hrc

    def get_hr(self):
        return self.hr

    def set_hr(self, hr):
        self.hr = hr
        self.interp_fir_filter_xxx_0_0_0.set_taps((self.hr))

    def get_hn(self):
        return self.hn

    def set_hn(self, hn):
        self.hn = hn

    def get_Rb(self):
        return self.Rb

    def set_Rb(self, Rb):
        self.Rb = Rb

    def get_MiconstellationObject(self):
        return self.MiconstellationObject

    def set_MiconstellationObject(self, MiconstellationObject):
        self.MiconstellationObject = MiconstellationObject

    def get_EbN0(self):
        return self.EbN0

    def set_EbN0(self, EbN0):
        self.EbN0 = EbN0
        self.analog_noise_source_x.set_amplitude(1.0 / math.sqrt(2.0 * self.Bps * 10**(self.EbN0/10)))


def main(top_block_cls=ber_simulation, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
