import pygame
import sys
from pygame.locals import *
from Cuadrado import *
from Circulo import *
from Triangulo import *
import pygwidgets

# Declaramos las constantes
BLANCO = (255,255,255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CUADROS_POR_SEGUNDO = 30
N_FIGURAS = 10

# Fijamos la ventana
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
clock = pygame.time.Clock()

listaDeFiguras = []
tuplaClasesDeFiguras = (Cuadrado, Circulo, Triangulo)

for i in range (0, N_FIGURAS):
  claseEscogidaAlAzar = random.choice(tuplaClasesDeFiguras)
  oFigura = claseEscogidaAlAzar(window, WINDOW_WIDTH, WINDOW_HEIGHT)
  listaDeFiguras.append(oFigura)

oStatusLine = pygwidgets.DisplayText(window, (4,4), 'Presiona sobre las figuras', fontSize=28)

# Loop principal
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

    if event.type == MOUSEBUTTONDOWN:
      # Invertimos el orden para revisar primero la última figura dibujada
      for oFigura in reversed(listaDeFiguras):
        if oFigura.clickedInside(event.pos):
          area = oFigura.obtenerArea()
          area = str(area)
          elTipo = oFigura.obtenerTipo()
          nuevoTexto = 'Presionaste sobre un ' + elTipo + ' cuya área es ' + area
          oStatusLine.setValue(nuevoTexto)
          break # Solo trata con la figura de hasta arriba.

# Le decimos a cada figura que se dibuje
window.fill(BLANCO)
for oFigura in listaDeFiguras:
  oFigura.draw()
oStatusLine.draw()

pygame.display.update()
clock.tick(CUADROS_POR_SEGUNDO)