#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
from grafico import Grafico
from threadGrafico import ThreadGrafico
from display import Display
from threadDisplay import ThreadDisplay


class Pagina(QtGui.QWidget):
    def __init__(self, parent, cor, tituloGrafico, unidade, host, porta, Ymin=None, Ymax=None, hostDisplay=None,
                 portaDisplay=None, atualizaDisplay=None):
        super(Pagina, self).__init__(parent)
        self.cor = cor

        self.grafico = Grafico(self, cor, tituloGrafico, unidade, Ymin, Ymax)
        self.display = Display(self, cor)

        botaoesquerda = QtGui.QPushButton('<', self)
        botaoesquerda.setStyleSheet('color: {0}'.format(cor))
        botaoesquerda.setGeometry(QtCore.QRect(240, 0, 40, 25))
        botaoesquerda.clicked.connect(self.graficoAnterior)

        botaodireita = QtGui.QPushButton('>', self)
        botaodireita.setStyleSheet('color: {0}'.format(cor))
        botaodireita.setGeometry(QtCore.QRect(425, 0, 40, 25))
        botaodireita.clicked.connect(self.proximoGrafico)

        layout = QtGui.QHBoxLayout(self)
        layout.addWidget(self.grafico)
        layout.addWidget(self.display)
        layout.setContentsMargins(QtCore.QMargins(0, 0, 0, 0))

        self.threadGrafico = ThreadGrafico(self.grafico, host, porta, display=self.display,
                                           atualizaDisplay=atualizaDisplay)
        self.threadGrafico.sinal.connect(self.grafico.myplot)

        if hostDisplay != None and portaDisplay != None:
            self.threadDisplay = ThreadDisplay(self.display, hostDisplay, portaDisplay)
        else:
            self.threadDisplay = None

    def proximoGrafico(self):
        self.parent().currentWidget().setHidden(True)  # tentativa para otimizar o botão
        # escondo o gráfico para que o loop da threads finalize, precisa arrumar
        # mas parace que melhorou o tempo de resposta
        self.parent().currentWidget().threadGrafico.quit()  # encerra thread atual
        if self.parent().currentWidget().threadDisplay != None:
            self.parent().currentWidget().threadDisplay.quit()  # encerra thread atual
        self.parent().setCurrentIndex((self.parent().currentIndex() + 1) % self.parent().count())  # muda grafico
        self.parent().currentWidget().setHidden(False)
        self.parent().currentWidget().threadGrafico.start()  # inicia thread atual
        if self.parent().currentWidget().threadDisplay != None:
            self.parent().currentWidget().threadDisplay.start()  # inicia thread atual

    def graficoAnterior(self):
        self.parent().currentWidget().setHidden(True)
        self.parent().currentWidget().threadGrafico.quit()
        if self.parent().currentWidget().threadDisplay != None:
            self.parent().currentWidget().threadDisplay.quit()  # encerra thread atual
        self.parent().setCurrentIndex((self.parent().currentIndex() - 1) % self.parent().count())
        self.parent().currentWidget().setHidden(False)
        self.parent().currentWidget().threadGrafico.start()
        if self.parent().currentWidget().threadDisplay != None:
            self.parent().currentWidget().threadDisplay.start()  # inicia thread atual
