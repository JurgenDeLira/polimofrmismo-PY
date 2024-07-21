class Vehiculo:
    def acelerar(self):
        pass

class Coche(Vehiculo):
    def acelerar(self):
        return "Coche acelerando"

class Moto(Vehiculo):
    def acelerar(self):
        return "Moto acelerando"

class Bicicleta(Vehiculo):
    def acelerar(self):
        return "Bicicleta acelerando"

class Conductor:
    def conducir(self, vehiculo):
        return vehiculo.acelerar()

coche = Coche()
moto = Moto()
bicicleta = Bicicleta()
conductor = Conductor()

print(conductor.conducir(coche))       # Salida: Coche acelerando
print(conductor.conducir(moto))        # Salida: Moto acelerando
print(conductor.conducir(bicicleta))   # Salida: Bicicleta acelerando