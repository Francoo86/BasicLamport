import socket
import pickle
from relojlogico import RelojLogico

class Cliente:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.reloj = RelojLogico()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def conectar(self):
        self.socket.connect((self.host, self.port))

    def enviar_mensaje(self, contenido):
        self.reloj.incrementar()
        mensaje = {'reloj': self.reloj.obtener_valor(), 'contenido': contenido}
        self.socket.send(pickle.dumps(mensaje))
        print(f"Cliente envió: {contenido} - Reloj: {self.reloj.obtener_valor()}")

    def recibir_mensaje(self):
        while True:
            data = self.socket.recv(1024)
            if not data:
                break
            mensaje = pickle.loads(data)
            self.reloj.actualizar(mensaje['reloj'])
            print(f"Cliente recibió: {mensaje['contenido']} - Reloj: {self.reloj.obtener_valor()}")