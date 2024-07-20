from AnimalClass import Animal

class Perro(Animal):
    def __init__(self, nombre, raza, pelaje):
        super().__init__(nombre, "Canino")
        self.raza = raza
        self.pelaje = pelaje

    def hacer_sonido(self):
        return "Woof"
    
perro = Perro("Rex", "Labrador", "Lacio")
print(perro.hacer_sonido())
