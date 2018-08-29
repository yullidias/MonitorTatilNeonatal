#!/usr/bin/python
# -*- coding: utf-8 -*-

import pyqtgraph
from PySide.QtCore import Slot
import numpy

class Grafico(pyqtgraph.PlotWidget):
    limiteEixoX = 500
    contador = 0
    def __init__(self, parent, cor, nome, unidade, Ymin=None, Ymax=None):
        pyqtgraph.setConfigOption('foreground', cor)
        tituloGrafico = nome + " (" + unidade + ")"

        super(Grafico, self).__init__(parent=parent, title=tituloGrafico, background=(120,120,120), enableMenu=False)
        self.hideAxis('bottom')

        self.Ymin = Ymin
        self.Ymax = Ymax
        self.cor = cor
        self.titulo = nome

        self.setMouseEnabled(False, False) #desabilita interação do mouse com os eixos
        self.setLimits(xMin=0, minXRange=self.limiteEixoX, maxXRange=self.limiteEixoX, yMin=self.Ymin, yMax=self.Ymax, minYRange=self.Ymax, maxYRange=self.Ymax)

        self.curva = self.plot(pen=pyqtgraph.mkPen(self.cor, width=1), antialias=True, clear=True)

    @Slot(numpy.ndarray)
    def myplot(self, vetor):
        self.curva.setData(vetor[:self.contador])
        if self.contador  < self.limiteEixoX:
            self.contador += 1

