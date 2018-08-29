#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from dataHora import DataHora
from exibirPerfil import ExibirPerfil
from telaGrafico import TelaGrafico
from threadEsperaVisializacaoWidget import ThreadWidget


class MenuSuperior(QtGui.QWidget):
    altura = 40
    larguraBotao = 50
    qtdBotoes = 0

    def __init__(self, parent):
        super(MenuSuperior, self).__init__(parent)
        '''
        chama QWidget passando o objeto QMainWindow como pai(parent = MainWindow object)
        isso permite que os botões sejam acessados pela JanelaPrincipal.
        se um widget nao tem parent, ele é considerado uma janela. Portanto é necessário passar a qual janela ele pertence
        super(subClass, instance).method(args)
        '''
        larguraJanelaPrincipal = parent.largura
        self.setGeometry(QtCore.QRect(0, 0, larguraJanelaPrincipal, self.altura))

        # Lê o arquivo externo de StyleSheet.
        with open('./MenuSuperior.css', 'r') as file:
            self.setStyleSheet(file.read())

        usuarioIcon = self.criaIcone('./icons/usuario.png', './icons/usuario-selecionado.png')
        self.usuario = self.criaBotao(usuarioIcon, larguraJanelaPrincipal - self.larguraBotao, 0, self.larguraBotao,
                                      self.altura)
        self.usuario.clicked.connect(self.exibirPerfil)

        graficoIcon = self.criaIcone('./icons/graph.png', './icons/graph-selecionado.png')
        self.grafico = self.criaBotao(graficoIcon, larguraJanelaPrincipal - 2 * self.larguraBotao, 0, self.larguraBotao,
                                      self.altura)
        self.grafico.setChecked(True)
        self.grafico.clicked.connect(self.exbirTelaGrafico)

        self.dataHora = DataHora(self)
        self.dataHora.setGeometry(
            QtCore.QRect(0, 0, larguraJanelaPrincipal - self.qtdBotoes * self.larguraBotao, self.altura))

        self.perfil = ExibirPerfil(parent)
        self.telaGrafico = TelaGrafico(parent, self.altura, parent.largura, parent.altura - self.altura)
        self.telaGrafico.show()

        self.threadWidget = ThreadWidget(self.telaGrafico)
        self.threadWidget.start()
        self.threadWidget.graficoEstaVisivel.connect(self.inicializaVisualizacao)

    def criaIcone(self, iconeNaoSelecionado, iconeSelecionado):
        icone = QtGui.QIcon()
        icone.addPixmap(QtGui.QPixmap(iconeNaoSelecionado))
        icone.addPixmap(QtGui.QPixmap(iconeSelecionado), QtGui.QIcon.Normal, QtGui.QIcon.On)
        return icone

    def criaBotao(self, icone, esquerdoCimaX, esquerdoCimaY, direitoBaixoX, direitoBaixoY):
        botao = QtGui.QPushButton(self)
        botao.setCheckable(True)
        botao.setAutoExclusive(True)
        botao.setIcon(icone)
        botao.setGeometry(QtCore.QRect(esquerdoCimaX, esquerdoCimaY, direitoBaixoX, direitoBaixoY))
        self.qtdBotoes += 1;
        return botao

    def exibirPerfil(self):
        self.threadWidget.quit()
        self.telaGrafico.hide()
        self.telaGrafico.pararTodasAsThreadsDosGraficos()
        self.telaGrafico.pararTodasAsThreadsDosDisplays()
        self.perfil.show()

    def exbirTelaGrafico(self):
        self.perfil.hide()
        self.telaGrafico.show()
        self.threadWidget.start()

    def inicializaVisualizacao(self):
        if self.telaGrafico.temperatura.isVisible():
            self.telaGrafico.temperatura.threadGrafico.start()
            if self.telaGrafico.temperatura.threadDisplay != None:
                self.telaGrafico.temperatura.threadDisplay.start()

        if self.telaGrafico.umidade.isVisible():
            self.telaGrafico.umidade.threadGrafico.start()
            if self.telaGrafico.umidade.threadDisplay != None:
                self.telaGrafico.umidade.threadDisplay.start()

        if self.telaGrafico.frequenciaCardiaca.isVisible():
            self.telaGrafico.frequenciaCardiaca.threadGrafico.start()
            if self.telaGrafico.frequenciaCardiaca.threadDisplay != None:
                self.telaGrafico.frequenciaCardiaca.threadDisplay.start()

        if self.telaGrafico.spo2.isVisible():
            self.telaGrafico.spo2.threadGrafico.start()
            if self.telaGrafico.spo2.threadDisplay != None:
                self.telaGrafico.spo2.threadDisplay.start()
