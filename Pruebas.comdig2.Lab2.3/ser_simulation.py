#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: SER Simulation
# Author: Homero Ortega Boada
# Description: Dale un valor a Es/No, corre el flujograma y obten la SER. Puedes sacar tantos valores como para construir una curva de SER
# Generated: Thu Feb 21 16:46:25 2019
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

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from b_SERTool_Channel import b_SERTool_Channel  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import math
import numpy
from gnuradio import qtgui


class ser_simulation(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "SER Simulation")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("SER Simulation")
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

        self.settings = Qt.QSettings("GNU Radio", "ser_simulation")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.const = const = [(1.+0.j),(0.+1.j),(-1.+0.j),(0.-1.j)]
        self.samp_rate = samp_rate = 100e3
        self.Sps = Sps = 16
        self.M = M = len(const)
        self.Rs = Rs = samp_rate/Sps
        self.Bps = Bps = int(math.log(M,2))
        self.run_stop = run_stop = True
        self.Rb = Rb = Rs*Bps
        self.N_snr = N_snr = 128

        self.MiconstellationObject = MiconstellationObject = digital.constellation_calcdist((const), (), 4, 1).base()

        self.MaxErrors = MaxErrors = 1000
        self.MaxCount = MaxCount = int(1e7)
        self.EsN0min = EsN0min = 0.
        self.EsN0max = EsN0max = 20.

        ##################################################
        # Blocks
        ##################################################
        _run_stop_check_box = Qt.QCheckBox('Inicial/Parar')
        self._run_stop_choices = {True: True, False: False}
        self._run_stop_choices_inv = dict((v,k) for k,v in self._run_stop_choices.iteritems())
        self._run_stop_callback = lambda i: Qt.QMetaObject.invokeMethod(_run_stop_check_box, "setChecked", Qt.Q_ARG("bool", self._run_stop_choices_inv[i]))
        self._run_stop_callback(self.run_stop)
        _run_stop_check_box.stateChanged.connect(lambda i: self.set_run_stop(self._run_stop_choices[bool(i)]))
        self.top_grid_layout.addWidget(_run_stop_check_box, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(MiconstellationObject)
        self.digital_chunks_to_symbols_xx = digital.chunks_to_symbols_bc((const), 1)
        self.blocks_throttle = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.b_SERTool_Channel_0 = b_SERTool_Channel(
            B=samp_rate,
            EsN0max=EsN0max,
            EsN0min=EsN0min,
            N_snr=N_snr,
            Rs=Rs,
        )
        self.top_grid_layout.addWidget(self.b_SERTool_Channel_0)
        (self.b_SERTool_Channel_0).set_block_alias("QPSK")
        self.analog_random_source_x = blocks.vector_source_b(map(int, numpy.random.randint(0, M, 10000000)), True)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x, 0), (self.blocks_throttle, 0))
        self.connect((self.b_SERTool_Channel_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.blocks_throttle, 0), (self.b_SERTool_Channel_0, 1))
        self.connect((self.blocks_throttle, 0), (self.digital_chunks_to_symbols_xx, 0))
        self.connect((self.digital_chunks_to_symbols_xx, 0), (self.b_SERTool_Channel_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.b_SERTool_Channel_0, 2))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ser_simulation")
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
        self.set_Rs(self.samp_rate/self.Sps)
        self.blocks_throttle.set_sample_rate(self.samp_rate)
        self.b_SERTool_Channel_0.set_B(self.samp_rate)

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_Rs(self.samp_rate/self.Sps)

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.set_Bps(int(math.log(self.M,2)))

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs
        self.b_SERTool_Channel_0.set_Rs(self.Rs)
        self.set_Rb(self.Rs*self.Bps)

    def get_Bps(self):
        return self.Bps

    def set_Bps(self, Bps):
        self.Bps = Bps
        self.set_Rb(self.Rs*self.Bps)

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        if self.run_stop: self.start()
        else: self.stop(); self.wait()
        self._run_stop_callback(self.run_stop)

    def get_Rb(self):
        return self.Rb

    def set_Rb(self, Rb):
        self.Rb = Rb

    def get_N_snr(self):
        return self.N_snr

    def set_N_snr(self, N_snr):
        self.N_snr = N_snr
        self.b_SERTool_Channel_0.set_N_snr(self.N_snr)

    def get_MiconstellationObject(self):
        return self.MiconstellationObject

    def set_MiconstellationObject(self, MiconstellationObject):
        self.MiconstellationObject = MiconstellationObject

    def get_MaxErrors(self):
        return self.MaxErrors

    def set_MaxErrors(self, MaxErrors):
        self.MaxErrors = MaxErrors

    def get_MaxCount(self):
        return self.MaxCount

    def set_MaxCount(self, MaxCount):
        self.MaxCount = MaxCount

    def get_EsN0min(self):
        return self.EsN0min

    def set_EsN0min(self, EsN0min):
        self.EsN0min = EsN0min
        self.b_SERTool_Channel_0.set_EsN0min(self.EsN0min)

    def get_EsN0max(self):
        return self.EsN0max

    def set_EsN0max(self, EsN0max):
        self.EsN0max = EsN0max
        self.b_SERTool_Channel_0.set_EsN0max(self.EsN0max)


def main(top_block_cls=ser_simulation, options=None):

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
