#!/usr/bin/python
# -*- coding: utf-8 -*-

import mysql.connector
import sys
from mysql.connector.errors import Error

class BancoDeDados():
    try:
        __instance = mysql.connector.connect(   user="root", password="123456",
                                            host="127.0.0.1",
                                            database="ProjetoNeonatal")

    except Error as e:
        print "<< classe", __name__, ">>", e
        sys.exit(1)

    def __init__(self):
        if BancoDeDados.__instance != None:
            raise Exception("Essa classe é singleton!")
        else:
            BancoDeDados.__instance = self

    @staticmethod
    def getInstance():
        if BancoDeDados.__instance == None:
            BancoDeDados()
        return BancoDeDados.__instance