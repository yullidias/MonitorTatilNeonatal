#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtCore
import numpy
from clienteSocket import ClienteSocket
from threadSocket import ThreadSocket


class ThreadGrafico(ThreadSocket):
    sinal = QtCore.Signal(numpy.ndarray)

    def __init__(self, objGrafico, host, porta, display=None, atualizaDisplay=None):
        super(ThreadGrafico, self).__init__(host, porta)
        self.quantidadeDePontosNaTela = 500
        self.cliente = ClienteSocket(host, porta)
        self.grafico = objGrafico
        self.grafico.limiteEixoX = self.quantidadeDePontosNaTela
        self.dados = numpy.zeros(self.quantidadeDePontosNaTela)
        self.contador = 0
        self.display = display
        self.atualizarGraficoEDisplay = atualizaDisplay
        self.ipServidor = self.getIpServidor()

    def run(self):
        while (self.grafico.isVisible()):
            dado = self.cliente.receber(self.ipServidor)

            if dado != None:
                self.dados[self.contador] = dado
                self.sinal.emit(self.dados)  # self.grafico.plot(self.dados)
                if self.atualizarGraficoEDisplay == True:
                    self.display.atualizaValorAtual(self.dados[self.contador])
                self.contador = (self.contador + 1) % self.quantidadeDePontosNaTela
        self.exec_()
