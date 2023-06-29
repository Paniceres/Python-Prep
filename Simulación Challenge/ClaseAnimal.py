
class Animal:
    def __init__(self, especie, color):
        self.Edad = 0
        self.Especie = especie
        self.Color = color

    def CumplirAnios(self):
        self.Edad += 1
        return self.Edad

# Ejemplo de uso
a = Animal('perro', 'blanco')

