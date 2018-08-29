#!/usr/bin/python
# -*- coding: utf-8 -*-

from bancoDeDados import BancoDeDados
from responsavel import Responsavel


class Neonato():
    BD = BancoDeDados.getInstance()

    def __init__(self, idNeonato, CPFresponsavel, nome=None, dataNascimento=None):
        self.id = idNeonato
        self.resposavel = Responsavel(CPF=CPFresponsavel)
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.buscarDados()

    def buscarDados(self):
        try:
            cursor = self.BD.cursor()

            consulta = "select nome_neonato, data_nascimento from neonatos where id_neonato = %(idNeonato)s and CPF = %(CPF)s"
            cursor.execute(consulta, {'idNeonato': self.id, 'CPF': self.resposavel.CPF})

            dadosNeonato = cursor.fetchone()

            self.nome, self.dataNascimento = dadosNeonato
        except TypeError as e:
            print "<< classe", __name__, ">>", e
        finally:
            cursor.close()
