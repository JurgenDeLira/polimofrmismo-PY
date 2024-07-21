class Figura:
    def calcular_area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14159265359 * self.radio ** 2

def calcular_area_figura(figura):
    return figura.calcular_area()

cuadrado = Cuadrado(5)
circulo = Circulo(3)

print(calcular_area_figura(cuadrado))  # Salida: 25
print(calcular_area_figura(circulo))   # Salida: 28.274333882308138