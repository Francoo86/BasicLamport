import socket
import threading
import pickle
from relojlogico import RelojLogico

class Servidor:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.reloj = RelojLogico()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))

    def iniciar(self):
        self.socket.listen()
        print(f"Servidor escuchando en {self.host}:{self.port}")
        while True:
            conn, addr = self.socket.accept()
            threading.Thread(target=self.manejar_cliente, args=(conn,)).start()

    def manejar_cliente(self, conn):
        while True:
            data = conn.recv(1024)
            if not data:
                break
            mensaje = pickle.loads(data)
            self.reloj.actualizar(mensaje['reloj'])
            print(f"Servidor recibió: {mensaje['contenido']} - Reloj: {self.reloj.obtener_valor()}")
