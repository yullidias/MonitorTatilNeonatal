#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtCore
from bancoDeDados import BancoDeDados


class ThreadSocket(QtCore.QThread):
    def __init__(self, host, porta):
        QtCore.QThread.__init__(self)
        self.BD = BancoDeDados.getInstance()
        self.host = host
        self.porta = porta
        self.ipServidor = self.getIpServidor()

    def getIpServidor(self):
        cursor = self.BD.cursor(buffered=True)
        try:
            consulta = "select ip_dispositivo from dispositivos D join dispositivos_portas DP on D.mac = DP.mac where num_porta= %(porta)s and envia=TRUE"
            cursor.execute(consulta, {'porta': self.porta})
            dado = cursor.fetchone()
            return dado[0]
        except TypeError as e:
            print "<< classe", __name__, ">>", e
        finally:
            if cursor != None:
                cursor.close()
