class Auto():
    def __init__(self, marca, modelo, anio, color):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.encendido = False #este no esta en el listado de arriba por que no nos interesa asignarlo
        # Tu ya sabes que el auto siempre va a inicializar apagado
    
    def encender(self):
        
        if not self.encendido: # es lo mismo que if self.encendido == False
            print("El auto se ha encendido")
            self.encendido = True

        else:
            print("El auto ya está encendido")

    def apagar(self):
        if self.encendido: ## if self.encendido == True
            print("Se ha apagado el auto")
            self.encendido = False
        else:
            print("El auto ya está apagado")
    
    def info(self):
        estado = "encendido" if self.encendido else "apagado"
        return f"Auto: {self.marca} {self.modelo} ({self.anio}), Color: {self.color} estado: {estado}"
    
auto1 = Auto("Toyota", "Corolla", 2022, "Azul")

auto1.apagar()
auto1.encender()
auto1.apagar()
auto1.encender()
auto1.encender()

print(auto1.info())