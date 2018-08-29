#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
from pagina import Pagina
from PySide.QtNetwork import QHostAddress


class TelaGrafico(QtGui.QWidget):
    iniciaThread = QtCore.Signal()

    def __init__(self, parent, alturaMenuSuperior, larguraJanelaPrincipal, altura):
        super(TelaGrafico, self).__init__(parent)
        self.setGeometry(QtCore.QRect(0, alturaMenuSuperior, larguraJanelaPrincipal, altura))

        with open('./Corpo.css', 'r') as file:
            self.setStyleSheet(file.read())

        self.cima = QtGui.QStackedWidget()
        self.baixo = QtGui.QStackedWidget()

        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.cima)
        layout.addWidget(self.baixo)
        print "numero ideal de Threads que podem estar rodando", QtCore.QThread.idealThreadCount()

        self.temperatura = Pagina(parent, '#7cfc00', self.trUtf8('Temperatura'), self.trUtf8('ºC'),
                                  QHostAddress.LocalHost, 8081, Ymin=0, Ymax=50, atualizaDisplay=True)
        self.umidade = Pagina(parent, '#00ffff', self.trUtf8('Umidade'), self.trUtf8('%'), QHostAddress.LocalHost, 8082,
                              hostDisplay=QHostAddress.LocalHost, portaDisplay=8085)
        self.frequenciaCardiaca = Pagina(parent, '#ffff00', self.trUtf8('Frequência'), self.trUtf8('Hz'),
                                         QHostAddress.LocalHost, 8083, atualizaDisplay=False)
        self.spo2 = Pagina(parent, '#ffc9ff', self.trUtf8('SpO2'), self.trUtf8('%'), QHostAddress.LocalHost, 8084,
                           atualizaDisplay=False)

        self.cima.addWidget(self.temperatura)
        self.cima.addWidget(self.frequenciaCardiaca)

        self.baixo.addWidget(self.umidade)
        self.baixo.addWidget(self.spo2)

    def iniciarTodasAsThreadsDosGraficos(self):
        self.temperatura.threadGrafico.start()
        self.umidade.threadGrafico.start()
        self.frequenciaCardiaca.threadGrafico.start()
        self.spo2.threadGrafico.start()

    def pararTodasAsThreadsDosGraficos(self):
        self.temperatura.threadGrafico.quit()
        self.umidade.threadGrafico.quit()
        self.frequenciaCardiaca.threadGrafico.quit()
        self.spo2.threadGrafico.quit()

    def iniciarTodasAsThreadsDosDisplays(self):
        if self.temperatura.threadDisplay != None:
            self.temperatura.threadDisplay.start()
        if self.umidade.threadDisplay != None:
            self.umidade.threadDisplay.start()
        if self.frequenciaCardiaca.threadDisplay != None:
            self.frequenciaCardiaca.threadDisplay.start()
        if self.spo2.threadDisplay != None:
            self.spo2.threadDisplay.start()

    def pararTodasAsThreadsDosDisplays(self):
        if self.temperatura.threadDisplay != None:
            self.temperatura.threadDisplay.quit()
        if self.umidade.threadDisplay != None:
            self.umidade.threadDisplay.quit()
        if self.frequenciaCardiaca.threadDisplay != None:
            self.frequenciaCardiaca.threadDisplay.quit()
        if self.spo2.threadDisplay != None:
            self.spo2.threadDisplay.quit()
