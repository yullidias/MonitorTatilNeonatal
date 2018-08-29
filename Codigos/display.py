#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui


class Display(QtGui.QWidget):
    laguraMaximaLineEdit = 40

    def __init__(self, parent, cor):
        super(Display, self).__init__(parent)
        self.setStyleSheet('color: {0};'.format(cor))
        self.setFixedSize(QtCore.QSize(200, 90))

        self.valorMaximo = ""
        self.valorMinimo = ""

        self.labelMaximo = QtGui.QLineEdit(str(self.valorMaximo))
        self.labelMaximo.setMaximumWidth(self.laguraMaximaLineEdit)

        self.labelMinimo = QtGui.QLineEdit(str(self.valorMinimo))
        self.labelMinimo.setMaximumWidth(self.laguraMaximaLineEdit)

        self.Central = QtGui.QLabel('000')
        self.Central.setFont(QtGui.QFont('Ubuntu', 45))
        self.Central.setMaximumWidth(130)

        limites_layout = QtGui.QVBoxLayout()
        limites_layout.addWidget(self.labelMaximo)
        limites_layout.addWidget(self.labelMinimo)

        layout = QtGui.QHBoxLayout(self)
        layout.addWidget(self.Central)
        layout.addLayout(limites_layout)

        self.labelMaximo.editingFinished.connect(
            self.atualizaValorMaximo)  # atualiza o valor máximo quando o usuário retira o cursor do campo
        self.labelMinimo.editingFinished.connect(
            self.atualizaValorMinimo)  # atualiza o valor minimo quando o usuário retira o cursor do campo

    def atualizaValorAtual(self, valor):
        self.Central.setText(str(valor))

    def atualizaValorMaximo(self):
        self.valorMaximo = self.labelMaximo.text()

    def atualizaValorMinimo(self):
        self.valorMinimo = self.labelMinimo.text()
