import math

class Fraccion:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("El denominador no puede ser 0")
        self.numerador = numerador
        self.denominador = denominador
        self.valor_decimal = numerador / denominador
        self.simplificar()

    def simplificar(self):
        gcd = math.gcd(self.numerador, self.denominador)
        self.numerador //= gcd
        self.denominador //= gcd

    def __str__(self):
        return f"{self.numerador}/{self.denominador} = {self.valor_decimal}"

    def __eq__(self, other):
        return self.numerador == other.numerador and self.denominador == other.denominador

    def __add__(self, other):
        nuevo_numerador = self.numerador * other.denominador + other.numerador * self.denominador
        nuevo_denominador = self.denominador * other.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

# Ejemplos de uso:
# Crear fracciones
fraccion1 = Fraccion(1, 2)
fraccion2 = Fraccion(3, 4)

# Imprimir fracciones
print(fraccion1)  # 1/2 = 0.5
print(fraccion2)  # 3/4 = 0.75

# Comparar fracciones
print(fraccion1 == fraccion2)  # False

# Sumar fracciones
suma = fraccion1 + fraccion2
print(suma)  # 5/4 = 1.25
