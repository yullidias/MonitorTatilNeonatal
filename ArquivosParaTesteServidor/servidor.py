import socket, datetime, time, random

class Servidor:
    def __init__(self, host, porta):
        self.port = porta
        self.host = host
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind(("", 0))

    def enviar(self,msg):
            self.s.sendto(msg, (self.host, int(self.port)))
