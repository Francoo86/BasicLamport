from cliente import Cliente
import time

cliente = Cliente('localhost', 5000)
cliente.conectar()

while True:
    cliente.enviar_mensaje("Mensaje desde Cliente 1")
    time.sleep(2)