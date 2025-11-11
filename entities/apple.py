import pygame
from pygame import Surface

class Apple(Surface):
    def __init__(self):
        super().__init__((15, 15))
        super().fill((255, 0, 0))

    def draw(self, display : pygame.display, position : tuple):
        display.blit(self, position)
    