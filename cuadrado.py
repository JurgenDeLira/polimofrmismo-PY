import pygame
import random
import math

# Fijamos los colores
ROJO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)

# Definimos la clase para el cuadrado
class Cuadrado():

  def __init__ (self, window, maxWidth, maxHeight):
    self.window = window
    self.widthAndHeight = random.randrange(10,100)
    self.color = random.choice((ROJO,VERDE,AZUL))
    self.x = random.randrange(1,maxWidth-100)
    self.y = random.randrange(25,maxHeight-100)
    self.rect = pygame.Rect(self.x,self.y,self.widthAndHeight,self.widthAndHeight)
    self.shapeType = 'cuadrado'

  def clickedInside(self, mousePoint):
    click = self.rect.collidepoint(mousePoint)
    return click

  def obtenerTipo(self):
    return self.shapeType

  def obtenerArea(self):
    elArea = self.widthAndHeight*self.widthAndHeight
    return elArea

  def draw(self):
    pygame.draw.rect(self.window, self.color, (self.x, self.y, self.widthAndHeight, self.widthAndHeigth))

#Definimos la clase para el círculo
class Circulo():

  def __init__ (self, window, maxWidth, maxHeight):
    self.window = window
    self.color = random.choice((ROJO,VERDE,AZUL))
    self.x = random.randrange(1,maxWidth-100)
    self.y = random.randrange(25,maxHeight-100)
    self.radio = random.randrange(10,50)
    self.centroX = self.x + self.radio
    self.centroY = self.y + self.radio
    self.rect = pygame.Rect(self.x,self.y,self.radio*2,self.radio*2)
    self.shapeType = 'círculo'

  def clickedInside(self, mousePoint):
    distancia = math.sqrt((mousePoint[0]-self.centroX)**2+((mousePoint[1]-self.centroY)**2))
    if distancia <= self.radio:
      return True
    else:
      return False

  def obtenerTipo(self):
    return self.shapeType

  def obtenerArea(self):
    elArea = math.pi*(self.radio**2)
    return elArea

  def draw(self):
    pygame.draw.circle(self.window, self.color, (self.centroX, self.centroY), self.radio, 0)

# Definimos la clase para el triángulo
class Triangulo():

  def __init__ (self, window, maxWidth, maxHeight):
    self.window = window
    self.width = random.randrange(10,100)
    self.height = random.randrange(10,100)
    self.pendienteTriangulo = -1*(self.height/self.width)
    self.color = random.choice((ROJO,VERDE,AZUL))
    self.x = random.randrange(1,maxWidth-100)
    self.y = random.randrange(25,maxHeight-100)
    self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
    self.shapeType = 'triángulo'

  def clickedInside(self, mousePoint):
    inRect = self.rect.collidepoint(mousePoint)
    if not inRect:
      return False
    # Hacemos algunas cuentas para ver si el punto está adentro del triángulo
    xOffset = mousePoint[0] - self.x
    yOffset = mousePoint[1] - self.y
    if xOffset == 0:
      return True
    # Calculamos la pendiente
    pendienteDelPuntoDesdeY = (yOffset-self.height)/xOffset
    if pendienteDelPuntoDesdeY < self.pendienteTriangulo:
      return True
    else:
      return False

  def obtenerTipo(self):
    return self.shapeType

  def obtenerArea(self):
    elArea = 0.5*self.width*self.height
    return elArea

  def draw(self):
    pygame.draw.polygon(self.window, self.color, ((self.x, self.y+self.height), (self.x, self.y), (self.x+self.width,self.y)))