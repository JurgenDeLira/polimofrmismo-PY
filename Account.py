from main import *
# Programa principal utilizando diccionario para almacenar personajes
# Diccionario para almacenar personajes con identificadores únicos
diccionario_personajes = {}
nextCharacterID = 0

while True:
    print()
    print('Presiona a para aumentar la salud')
    print('Presiona d para disminuir la salud')
    print('Presiona n para aumentar el nivel')
    print('Presiona e para aumentar la energía')
    print('Presiona r para reducir la energía')
    print('Presiona o para crear un nuevo personaje')
    print('Presiona s para mostrar todos los personajes')
    print('Presiona q para salir')
    print()
    accion = input('¿Qué deseas hacer? ')
    accion = accion.lower()
    print()

    if accion == 'a':
        print('*** Aumentar Salud ***')
        characterID = int(input('Por favor, ingresa el ID del personaje: '))
        cantidad = int(input('Por favor, ingresa la cantidad a aumentar: '))
        personaje = diccionario_personajes.get(characterID)
        if personaje:
            saludActual = personaje.aumentarSalud(cantidad)
            if saludActual is not None:
                print('La nueva salud es:', saludActual)
        else:
            print('Personaje no encontrado.')

    elif accion == 'd':
        print('*** Disminuir Salud ***')
        characterID = int(input('Por favor, ingresa el ID del personaje: '))
        cantidad = int(input('Por favor, ingresa la cantidad a disminuir: '))
        personaje = diccionario_personajes.get(characterID)
        if personaje:
            saludActual = personaje.disminuirSalud(cantidad)
            if saludActual is not None:
                print('La nueva salud es:', saludActual)
        else:
            print('Personaje no encontrado.')

    elif accion == 'n':
        print('*** Aumentar Nivel ***')
        characterID = int(input('Por favor, ingresa el ID del personaje: '))
        personaje = diccionario_personajes.get(characterID)
        if personaje:
            nivelActual = personaje.aumentarNivel()
            print('El nuevo nivel es:', nivelActual)
        else:
            print('Personaje no encontrado.')

    elif accion == 'e':
        print('*** Aumentar Energía ***')
        characterID = int(input('Por favor, ingresa el ID del personaje: '))
        cantidad = int(input('Por favor, ingresa la cantidad a aumentar: '))
        personaje = diccionario_personajes.get(characterID)
        if personaje:
            energiaActual = personaje.aumentarEnergia(cantidad)
            if energiaActual is not None:
                print('La nueva energía es:', energiaActual)
        else:
            print('Personaje no encontrado.')

    elif accion == 'r':
        print('*** Reducir Energía ***')
        characterID = int(input('Por favor, ingresa el ID del personaje: '))
        cantidad = int(input('Por favor, ingresa la cantidad a reducir: '))
        personaje = diccionario_personajes.get(characterID)
        if personaje:
            energiaActual = personaje.disminuirEnergia(cantidad)
            if energiaActual is not None:
                print('La nueva energía es:', energiaActual)
        else:
            print('Personaje no encontrado.')

    elif accion == 'o':
        print('*** Crear Nuevo Personaje ***')
        nombre = input('¿Cuál es el nombre del nuevo personaje? ')
        salud = int(input('¿Cuál es la salud inicial del personaje? '))
        nivel = int(input('¿Cuál es el nivel inicial del personaje? '))
        energia = int(input('¿Cuál es la energía inicial del personaje? '))
        personaje = Personaje(nombre, salud, nivel, energia)
        diccionario_personajes[nextCharacterID] = personaje
        print('Se ha creado un nuevo personaje, el ID del personaje es:', nextCharacterID)
        nextCharacterID += 1
        print()

    elif accion == 's':
        print('Mostrar:')
        for characterID in diccionario_personajes:
            personaje = diccionario_personajes[characterID]
            print('    ID del personaje:', characterID)
            personaje.mostrarEstadisticas()

    elif accion == 'q':
        break

    else:
        print('Lo siento, esa no es una acción válida. Por favor, intenta nuevamente.')

print('Hecho')