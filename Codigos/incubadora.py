#!/usr/bin/python
# -*- coding: utf-8 -*-
from bancoDeDados import BancoDeDados
from neonato import Neonato
from dispositivo import Dispositivo


class Incubadora():
    BD = BancoDeDados.getInstance()

    def __init__(self, id, nome=None, data_entrada=None):
        self.id = id
        self.nome = nome
        self.data_entrada = data_entrada
        self.dispositivos = []
        self.neonato = None
        self.buscarDados()

    def buscarDados(self):
        cursor = self.BD.cursor(buffered=True)
        try:
            consulta = "select I.nome_incubadora, NI.idNeonato from incubadoras I join neonatos_incubadoras NI  on I.id_incubadora = NI.id_incubadora where I.id_incubadora = %(id_incubadora)s and NI.data_saida is null order by NI.data_entrada desc"
            cursor.execute(consulta, {'id_incubadora': self.id})
            dados = cursor.fetchone()

            self.nome, idNeonato = dados
            consulta = "select CPF from neonatos where id_neonato = %(id)s"
            cursor.execute(consulta, {'id': idNeonato})
            cpf, = cursor.fetchone()

            self.neonato = Neonato(idNeonato=idNeonato, CPFresponsavel=cpf)

        except TypeError as e:
            print "<< classe", __name__, ">>", e
        finally:
            if cursor != None:
                cursor.close()

    def buscarDispositivos(self):
        cursor = self.BD.cursor(buffered=True)

        consulta = "select MAC, data_entrada from incubadoras_dispositivos where id_incubadora = %(id)s and data_saida is null order by data_entrada desc"
        cursor.execute(consulta, {'id': self.id})
        dados = cursor.fetchall()

        for dado in dados:
            if self.dispositivos.count(dado[0]) == 0:
                self.dispositivos.append(Dispositivo(MAC=dado[0], dataEntradaIncubadora=dado[1]))

        cursor.close()
