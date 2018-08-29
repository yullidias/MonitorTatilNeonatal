#!/usr/bin/python
# -*- coding: utf-8 -*-

from bancoDeDados import BancoDeDados


class Responsavel():
    BD = BancoDeDados.getInstance()

    def __init__(self, CPF, RG=None, nome=None):
        self.CPF = CPF
        self.RG = RG
        self.nome = nome
        self.buscarDados()

    def buscarDados(self):
        try:
            cursor = self.BD.cursor()

            consulta = "select RG, nome_responsavel from responsaveis where CPF= %(CPF)s";
            parametros = {'CPF': self.CPF}

            cursor.execute(consulta, parametros)

            dadosResponsavel = cursor.fetchone()  # fetchone retorna a próxima linha da consulta

            self.RG, self.nome = dadosResponsavel
        except TypeError as e:
            print "<< classe", __name__, ">>", e
        finally:
            cursor.close()

        return self
