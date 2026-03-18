class Visitante:
    def __init__(self, cedula, nombre, motivo):
        self.cedula = cedula
        self.nombre = nombre
        self.motivo = motivo

    def __str__(self):
        return f"{self.cedula} - {self.nombre} - {self.motivo}"