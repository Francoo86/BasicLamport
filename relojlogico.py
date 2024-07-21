class RelojLogico:
    def __init__(self):
        self.valor = 0

    def incrementar(self):
        self.valor += 1

    def actualizar(self, valor_recibido):
        self.valor = max(self.valor, valor_recibido) + 1

    def obtener_valor(self):
        return self.valor