class Sismografo:
    def __init__(self, identificador, modelo):
        self.identificador = identificador
        self.modelo = modelo
        self.estado_actual = None
        self.estacion = None