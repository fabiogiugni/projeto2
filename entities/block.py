import pygame.display
from pygame import Surface

class Block(Surface):
    def __init__(self, size : tuple = (15, 15), position : tuple = (50, 50)):
        super().__init__(size)
        
        self._position = position
        

    def fillColor(self, color : tuple):
        super().fill(color)

    def draw(self, display : pygame.display):
        display.blit(self, self._position)

    