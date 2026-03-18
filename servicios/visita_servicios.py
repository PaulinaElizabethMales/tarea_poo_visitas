
from modelos.visitante import Visitante

class VisitaServicios:
    def __init__(self):
        self.visitantes = []

    def agregar_visitante(self, cedula, nombre, motivo):
        # Validar que no exista duplicado por cédula
        for v in self.visitantes:
            if v.cedula == cedula:
                return False
        visitante = Visitante(cedula, nombre, motivo)
        self.visitantes.append(visitante)
        return True

    def listar_visitantes(self):
        return self.visitantes

    def eliminar_visitante(self, cedula):
        cedula = str(cedula)  # asegurar que sea string
        for v in self.visitantes:
            if str(v.cedula) == cedula:
                self.visitantes.remove(v)
                return True
        return False
