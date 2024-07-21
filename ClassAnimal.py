class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return f"{self.nombre} dice: ¡Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return f"{self.nombre} dice: ¡Miau!"

class Vaca(Animal):
    def hacer_sonido(self):
        return f"{self.nombre} dice: ¡Muu!"

# Función para hacer que un animal haga un sonido
def hacer_sonar_animal(animal):
    return animal.hacer_sonido()

# Crear instancias de diferentes animales
mi_perro = Perro("Buddy")
mi_gato = Gato("Whiskers")
mi_vaca = Vaca("Bessie")

# Llamar a la función haciendo sonar a los animales
print(hacer_sonar_animal(mi_perro))  # Salida: Buddy dice: ¡Guau!
print(hacer_sonar_animal(mi_gato))   # Salida: Whiskers dice: ¡Miau!
print(hacer_sonar_animal(mi_vaca))   # Salida: Bessie dice: ¡Muu!