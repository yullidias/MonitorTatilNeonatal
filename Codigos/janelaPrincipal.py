#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui, QtCore
from menuSuperior import MenuSuperior
from threadEsperaVisializacaoWidget import ThreadWidget


class JanelaPrincipal(QtGui.QMainWindow):
    largura = 880
    altura = 425

    def __init__(self):
        super(JanelaPrincipal, self).__init__()

        self.setStyleSheet('background-color: rgb(120,120,120);')
        self.setWindowTitle('Neonato')
        self.setFixedSize(QtCore.QSize(self.largura, self.altura))
        self.setFocus()  # coloca a entrada do teclado na janela atual

        self.menuSuperior = MenuSuperior(self)

        self.threadWidget = ThreadWidget(self.menuSuperior.telaGrafico)
        self.threadWidget.start()
        self.threadWidget.graficoEstaVisivel.connect(self.inicializaVisualizacao)

    def inicializaVisualizacao(self):
        self.menuSuperior.telaGrafico.temperatura.threadGrafico.start()
        self.menuSuperior.telaGrafico.umidade.threadGrafico.start()
        if self.menuSuperior.telaGrafico.temperatura.threadDisplay != None:
            self.menuSuperior.telaGrafico.temperatura.threadDisplay.start()
        if self.menuSuperior.telaGrafico.umidade.threadDisplay != None:
            self.menuSuperior.telaGrafico.umidade.threadDisplay.start()

    def closeEvent(self, event):
        self.menuSuperior.telaGrafico.pararTodasAsThreadsDosGraficos()
        self.menuSuperior.telaGrafico.pararTodasAsThreadsDosDisplays()


if __name__ == '__main__':
    qApp = QtGui.QApplication(sys.argv)
    qApp.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))

    program = JanelaPrincipal()
    program.show()

    sair = qApp.exec_()
    sys.exit(sair)
