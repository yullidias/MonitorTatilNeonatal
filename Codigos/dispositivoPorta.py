#!/usr/bin/python
# -*- coding: utf-8 -*-

from bancoDeDados import BancoDeDados
from dispositivo import Dispositivo
from porta import Porta


class DispositivoPorta():
    BD = BancoDeDados.getInstance()

    def __init__(self, MAC, idPorta, envia=None, recebe=None):
        self.dispositivo = Dispositivo(MAC=MAC)
        self.porta = Porta(id=idPorta)
        self.envia = envia
        self.recebe = recebe
        self.buscarDados()

    def buscarDados(self):
        try:
            cursor = self.BD.cursor()

            consulta = "select envia, recebe from dispositivos_portas where MAC = %(MAC) and id_porta = %(porta)"
            cursor.execute(consulta, {'MAC': self.dispositivo.MAC, 'porta': self.porta.id})
            dados = cursor.fetchone()

            self.envia, self.porta = dados
        except ValueError as e:
            print "<< classe", __name__, ">>", e
        finally:
            cursor.close()
