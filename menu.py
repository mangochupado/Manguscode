import pygame
import sys
import os
import fondo
from fondo import *
class menu:
    def __init__(self):
        pygame.init()
        keys = pygame.key.get_pressed()
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
    def eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    def draw(self):
        self.screen.blit(fondo.menu_fondo, (0, 0))
        font1 = pygame.font.SysFont(None, 55)
        font2 = pygame.font.SysFont(None, 35)
        titulo = font1.render("Menu", True, (255, 255, 255))
        self.screen.blit(titulo, (ANCHURA // 2 - titulo.get_width() // 2, ALTURA // 4 - titulo.get_height() // 2 -50))
        jugar = font2.render("Jugar", True, (255, 255, 255))
        self.screen.blit(jugar, (ANCHURA // 2 - jugar.get_width() // 2, ALTURA // 2 - jugar.get_height() // 2 - 50))
        opciones = font2.render("Opciones", True, (255, 255, 255))
        self.screen.blit(opciones, (ANCHURA // 2 - opciones.get_width() // 2, ALTURA * 3//4 - opciones.get_height() // 2 - 50))
        credits = font2.render("Creditos", True, (255, 255, 255))
        self.screen.blit(credits, (ANCHURA // 2 - credits.get_width() // 2, ALTURA - credits.get_height() -50))
        pygame.display.flip()
    def aicson(self):
        while self.running == True:
            self.eventos()
            self.draw()
            self.clock.tick(60)
        pygame.quit()

if __name__ == "__main__":
    menu = menu()
    menu.aicson()
    