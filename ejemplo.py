class Persona:
    def __init__(self, nombre, edad_ejemplo, ciudad):
        self.nombre = nombre
        self.edad = edad_ejemplo
        self.ciudad = ciudad

    def caminar(self):
        print(self.nombre + " está caminando")

          # Usamos la clase o sea Persona con mayuscula
          #Persona(nombre, edad, ciudad)
persona1 = Persona("Daniel", 22, "CDMX")
persona2 = Persona("Fabiola", 28, "Mérida")
persona3 = Persona("Joaquín", 24, "CDMX")

persona3.caminar()
persona1.caminar()
persona2.caminar()