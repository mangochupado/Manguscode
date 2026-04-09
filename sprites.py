import fondo
from fondo import *
import pygame
import pygame
import os
import sys

class gracielas:
    def __init__(self):
        self.x = fondo.ANCHURA // 2
        self.y = fondo.ALTURA // 2
        
        self.rect = pygame.Rect(self.x, self.y, fondo.Mangus_size[0], fondo.Mangus_size[1])
    def movimiento (self, dx, dy):
        self.x += dx * fondo.Mangus_speed
        self.y += dy * fondo.Mangus_speed
        self.rect.center = (self.x, self.y)
    def draw(self, screen):
        mangus_image = []
        def resource_path(relative_path):
            try:
                base_path = sys._MEIPASS
            except Exception:
                base_path = os.path.abspath(".")
                return os.path.join(base_path, relative_path)

        mangus = resource_path("assets\\imagenes\\mangus.png")
        mangus_image.append(pygame.image.load(mangus))
        screen.blit(mangus_image[0], self.rect) #dibujar el sprite en la pantalla usando su rectangulo para posicionarlo
        
        