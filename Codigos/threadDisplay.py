#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtCore
import numpy
from clienteSocket import ClienteSocket
from threadSocket import ThreadSocket


class ThreadDisplay(ThreadSocket):
    sinalDadoRecebido = QtCore.Signal(numpy.ndarray)

    def __init__(self, objDisplay, host, porta):
        super(ThreadDisplay, self).__init__(host, porta)
        self.display = objDisplay
        self.cliente = ClienteSocket(host, porta)

    def run(self):
        while (self.display.isVisible()):
            dado = self.cliente.receber(self.ipServidor)
            if dado != None:
                self.display.atualizaValorAtual(dado)
        self.exec_()
