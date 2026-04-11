import pygame
from fondo import *
from sprites import *
import sys
import fondo
import os
import sprites

# Iniciar el pygame
class juego:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((fondo.ANCHURA, fondo.ALTURA))
        pygame.display.set_caption("Mangus Cunulungus")
        def resource_path(relative_path):
            try:
                base_path = sys._MEIPASS
            except Exception:
                base_path = os.path.abspath(".")
                return os.path.join(base_path, relative_path)
        amon = resource_path("assets\\imagenes\\mangus.png")
        icono = pygame.image.load(amon)
        pygame.display.set_icon(icono) 
        self.clock = pygame.time.Clock()
        self.running = True
        self.gracielas = gracielas()
    def eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    def update(self):
        keys = pygame.key.get_pressed()
        dx = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT] or keys[pygame.K_d] - keys[pygame.K_a]
        dy = keys[pygame.K_DOWN] - keys[pygame.K_UP] or keys[pygame.K_s] - keys[pygame.K_w]
        self.gracielas.movimiento(dx, dy)
        
    def draw(self):
        #variables
        keys = pygame.key.get_pressed()
        self.screen.fill(fondo.BACKGROUND_COLOR)            
        #si la tecla derecha esta presionada, se voltea la imagen
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.screen.blit(pygame.transform.flip(pygame.transform.scale(pygame.image.load(resource_path("assets\\imagenes\\mangus.png")), fondo.Mangus_size), True, False), self.gracielas.rect)
            fondo.ultima_direccion = "izquierda"
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.screen.blit(pygame.transform.scale(pygame.image.load(resource_path("assets\\imagenes\\mangus.png")), fondo.Mangus_size), self.gracielas.rect)
            fondo.ultima_direccion = "derecha"
        else:
            if fondo.ultima_direccion == "izquierda":
                self.screen.blit(pygame.transform.flip(pygame.transform.scale(pygame.image.load(resource_path("assets\\imagenes\\mangus.png")), fondo.Mangus_size), True, False), self.gracielas.rect)
            else:
                self.screen.blit(pygame.transform.scale(pygame.image.load(resource_path("assets\\imagenes\\mangus.png")), fondo.Mangus_size), self.gracielas.rect)
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