#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
from bancoDeDados import BancoDeDados

class ClienteSocket():
    BD = BancoDeDados.getInstance()
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socketReceber = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socketReceber.bind(("",port))
        self.mensagemDeErroJaExibida = False

    def receber(self, ipEscritor):
        data, addr = self.socketReceber.recvfrom(2000)
        try:
            if ipEscritor == addr[0]:
                return data
            elif not self.mensagemDeErroJaExibida:
                self.mensagemDeErroJaExibida = True
                raise ImportError("ip Escritor é diferente do cadastrado")
        except ImportError as e:
            print "<< classe", __name__, ">>", e
        return None

    def test_Socket(self):
        while True:
            print self.receber("10.0.122.26")

