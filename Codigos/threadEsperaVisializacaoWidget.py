#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtCore


class ThreadWidget(QtCore.QThread):
    graficoEstaVisivel = QtCore.Signal()

    def __init__(self, widget):
        QtCore.QThread.__init__(self)
        self.widget = widget

    def run(self):
        while (not self.widget.isVisible):  # entra em uma espera ocupada até que a tela seja exibida
            pass
        self.graficoEstaVisivel.emit()
