import fondo
import pygame

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
        pygame.draw.rect(screen, fondo.ORANGE, self.rect)