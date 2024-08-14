class Personaje():
    # Constructor de la clase Personaje
    def __init__(self, name, salud, nivel, energia):
        self.name = name
        self.salud = int(salud)
        self.nivel = int(nivel)
        self.energia = int(energia)

    # Método para aumentar la salud del personaje
    def aumentarSalud(self, cantidad):
        if cantidad < 0:
            print('No puedes aumentar una cantidad negativa de salud')
            return None

        self.salud += cantidad
        return self.salud

    # Método para disminuir la salud del personaje
    def disminuirSalud(self, cantidad):
        if cantidad < 0:
            print('No puedes disminuir una cantidad negativa de salud')
            return None

        self.salud -= cantidad
        if self.salud < 0:
            self.salud = 0
        return self.salud

    # Método para aumentar el nivel del personaje
    def aumentarNivel(self):
        self.nivel += 1
        return self.nivel

    # Método para aumentar la energía del personaje
    def aumentarEnergia(self, cantidad):
        if cantidad < 0:
            print('No puedes aumentar una cantidad negativa de energía')
            return None

        self.energia += cantidad
        return self.energia

    # Método para disminuir la energía del personaje
    def disminuirEnergia(self, cantidad):
        if cantidad < 0:
            print('No puedes disminuir una cantidad negativa de energía')
            return None

        self.energia -= cantidad
        if self.energia < 0:
            self.energia = 0
        return self.energia

    # Método para mostrar las estadísticas del personaje
    def mostrarEstadisticas(self):
        print(' Nombre:', self.name)
        print(' Salud:', self.salud)
        print(' Nivel:', self.nivel)
        print(' Energía:', self.energia)
        print()