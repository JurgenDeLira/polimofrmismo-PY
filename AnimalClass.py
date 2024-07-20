class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def obtener_informacion(self):
        return f"Nombre: {self.nombre}, Especie: {self.especie}"
    
    def hacer_sonido(self):
        pass