#!/usr/bin/python
# -*- coding: utf-8 -*-

from bancoDeDados import BancoDeDados


class Porta:
    BD = BancoDeDados.getInstance()

    def __init__(self, id, numero=None, descricao=None):
        self.id = id
        self.numero = numero
        self.descricao = descricao
        self.dispositivos = []
        self.buscarDados()

    def buscarDados(self):
        cursor = self.BD.cursor()

        consulta = "select num_porta, desc_sinal from portas where id_porta = %(id)s"
        cursor.execute(consulta, {'id': self.id})
        dados = cursor.fetchone()

        try:
            self.numero, self.descricao = dados
        except ValueError as e:
            print "<< classe", __name__, ">>", e
        finally:
            cursor.close()

    def getNumero(self, descricao):
        cursor = self.BD.cursor()

        consulta = "select num_porta from portas where desc_sinal = %(desc)s"
        cursor.execute(consulta, {'desc', descricao})

        try:
            return cursor.fetchone()[0]
        except ValueError as e:
            print "<< classe", __name__, ">>", e
        finally:
            cursor.close()
