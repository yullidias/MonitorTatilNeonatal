#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui


class DataHora(QtGui.QLabel):
    def __init__(self, parent):
        super(DataHora, self).__init__(parent)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.showDataHora()

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showDataHora)
        timer.start(500)

    @QtCore.Slot()
    def showDataHora(self):
        data_hora = QtCore.QDateTime.currentDateTime()
        string = data_hora.toString('d MMMM yyyy, hh:mm').title()
        self.setText(string)
