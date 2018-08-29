#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
import uuid
from incubadora import Incubadora
from dispositivo import Dispositivo


class ExibirPerfil(QtGui.QWidget):
    MAC = (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
                     for ele in range(0, 8 * 6, 8)][::-1]))

    def __init__(self, parent):
        super(ExibirPerfil, self).__init__(parent)
        self.setGeometry(QtCore.QRect(100, 50, 700, 370))

        with open('./exibirPerfil.css', 'r') as file:
            self.setStyleSheet(file.read())

        try:
            dispositivo = Dispositivo(MAC=self.MAC)
            incubadora = Incubadora(id=dispositivo.buscarIncubadoraAtual())

            secaoNeonato = QtGui.QVBoxLayout()
            secaoNeonato.addWidget(self.criarTitulo("Neonato"))
            secaoNeonato.addLayout(self.criarLayoutLinha("Nome",
                                                         "" if incubadora.neonato.nome is None else incubadora.neonato.nome))
            secaoNeonato.addLayout(self.criarLayoutLinha("Data Nascimento",
                                                         "" if incubadora.neonato.dataNascimento is None else unicode(
                                                             incubadora.neonato.dataNascimento)))

            secaoIncubadora = QtGui.QVBoxLayout()
            secaoIncubadora.addLayout(
                self.criarLayoutLinha("Incubadora", "" if incubadora.nome is None else incubadora.nome))

            secaoResponsavel = QtGui.QVBoxLayout()
            secaoResponsavel.addWidget(self.criarTitulo(self.trUtf8("Responsável")))
            secaoResponsavel.addLayout(self.criarLayoutLinha("CPF",
                                                             "" if incubadora.neonato.resposavel.CPF is None else incubadora.neonato.resposavel.CPF))
            secaoResponsavel.addLayout(self.criarLayoutLinha("Identidade",
                                                             "" if incubadora.neonato.resposavel.RG is None else incubadora.neonato.resposavel.RG))

            layout = QtGui.QVBoxLayout(self)
            layout.addLayout(secaoNeonato)
            layout.addLayout(secaoIncubadora)
            layout.addLayout(secaoResponsavel)

            self.hide()
        except TypeError as e:
            print "<< classe", __name__, ">>", e

    def criarTitulo(self, texto):
        tituloLabel = QtGui.QLabel()
        tituloLabel.setFrameStyle(QtGui.QFrame.StyledPanel | QtGui.QFrame.Sunken)
        tituloLabel.setText(texto)
        tituloLabel.setFont(QtGui.QFont('Georgia', 22, QtGui.QFont.Bold))
        tituloLabel.setStyleSheet('color:rgb(0, 255, 255)')
        tituloLabel.setMaximumWidth(200)
        return tituloLabel

    def criarLayoutLinha(self, campo, texto):
        campoLabel = QtGui.QLabel()
        campoLabel.setFrameStyle(QtGui.QFrame.StyledPanel | QtGui.QFrame.Sunken)
        campoLabel.setText(campo)
        campoLabel.setFont(QtGui.QFont('Ubuntu', 12, QtGui.QFont.Bold))
        campoLabel.setMaximumHeight(40)
        campoLabel.setMaximumWidth(200)

        textoLabel = QtGui.QLabel()
        textoLabel.setFrameStyle(QtGui.QFrame.StyledPanel | QtGui.QFrame.Sunken)
        textoLabel.setText(texto)
        textoLabel.setFont(QtGui.QFont('Ubuntu', 12))
        textoLabel.setMaximumHeight(40)
        textoLabel.setMaximumWidth(200)

        linha = QtGui.QHBoxLayout()
        linha.addWidget(campoLabel)
        linha.addWidget(textoLabel)
        return linha
