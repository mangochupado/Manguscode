import pygame
from fondo import *
from sprites import *
import random
import sprites
import math
import sys
import os
import fondo

# Iniciar el pygame
class juego:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((fondo.ANCHURA, fondo.ALTURA))
        pygame.display.set_caption("Mangus Cunulungus")
        #reloj para controlar los fps
        self.clock = pygame.time.Clock()
        self.running = True
        self.gracielas = gracielas()
    def eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    def update(self):
        keys = pygame.key.get_pressed()
        dx = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        dy = keys[pygame.K_DOWN] - keys[pygame.K_UP]
        self.gracielas.movimiento(dx, dy)
        
    def draw(self):
        self.screen.fill(fondo.BACKGROUND_COLOR)
        self.gracielas.draw(self.screen)
        pygame.display.flip()
    def aicson(self):
        while self.running == True:
            self.eventos()
            self.update()
            self.draw()
            self.clock.tick(60)
        pygame.quit()
        sys.exit()
if __name__ == "__main__": #esto es para que el juego se ejecute solo si se ejecuta este archivo, no si se importa como modulo
    juego = juego() #creamos una instancia de la clase juego
    juego.aicson() #iniciamos el juego