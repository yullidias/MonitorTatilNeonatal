#!/usr/bin/python
# -*- coding: utf-8 -*-

from bancoDeDados import BancoDeDados
from porta import Porta
from mysql.connector.errors import Error


class Dispositivo:
    BD = BancoDeDados.getInstance()

    def __init__(self, MAC, nome=None, descricao=None, ip_dispositivo=None):
        self.MAC = MAC
        self.nome = nome
        self.descricao = descricao,
        self.ip = ip_dispositivo
        self.portas = []
        self.buscarDados()

    def buscarDados(self):
        try:
            cursor = self.BD.cursor()

            try:
                consulta = "select nome_dispositivo, ip_dispositivo from dispositivos d natural join incubadoras_dispositivos i where mac= %(MAC)s and data_remocao is null order by data_conexao desc"
                cursor.execute(consulta, {'MAC': self.MAC})
                dados = cursor.fetchone()
                self.nome, self.ip = dados
            except TypeError as e:
                print "<< classe", __name__, ">>", "Esse dispositivo não está cadastrado e/ou dispositivo nao esta conectado em nenhuma incubadora.", e
            except ValueError as e:
                print "<< classe", __name__, ">>", e
            except Error as e:
                print "<< classe", __name__, ">>", e

        finally:
            cursor.close()

    def buscarMinhasPortas(self):
        cursor = self.BD.cursor(buffered=True)

        consulta = "select id_porta from portas WHERE mac = %(MAC)s"
        cursor.execute(consulta, {'MAC': self.MAC})
        dados = cursor.fetchall()

        for id in dados:
            if self.dispositivos.count(id[0]) == 0:
                self.dispositivos.append(Porta(id=id[0]))

        cursor.close()

    def buscarIncubadoraAtual(self):
        try:
            cursor = self.BD.cursor()

            consulta = "select id_incubadora from incubadoras_dispositivos where mac= %(MAC)s and data_remocao is null order by data_conexao desc"
            cursor.execute(consulta, {'MAC': self.MAC})
            idIncubadora = cursor.fetchone()
        except TypeError as e:
            print "<< classe", __name__, ">>", e
        finally:
            cursor.close()
        return idIncubadora[0]
