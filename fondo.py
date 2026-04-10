import pygame
import random
import math
import os
import sys

#fondo
ANCHURA = 677
ALTURA = 677
BACKGROUND_COLOR = (225, 225, 225) #color de fondo

#colores
BLACK = (0, 0, 0)
RED = (255, 0, 0) 
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)

#sprites
#mangus
Mangus_size = (64, 64)
Mangus_speed = 7
ultima_direccion = "derecha"

#cargar imagenes
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
animacion_mangus = []
Mframe_1 = resource_path("assets\\imagenes\\mangus.png")
Mframe_2 = resource_path("assets\\imagenes\\mangusM1.png")
Mframe_3 = resource_path("assets\\imagenes\\mangusM2.png")
Mframe_4 = resource_path("assets\\imagenes\\mangusM1.png")
Mframe_5 = resource_path("assets\\imagenes\\mangus.png")
animacion_mangus.append(pygame.image.load(Mframe_1))
animacion_mangus.append(pygame.image.load(Mframe_2))    
animacion_mangus.append(pygame.image.load(Mframe_3))
animacion_mangus.append(pygame.image.load(Mframe_4))
animacion_mangus.append(pygame.image.load(Mframe_5))