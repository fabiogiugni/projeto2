import pygame
from .block import Block
from random import randint

class Apple(Block):
    def __init__(self, displayRange : tuple):
        super().__init__((15, 15))
        super().fill((255, 0, 0))
        self.__displayRange = displayRange
        self._position = ( randint(0, displayRange[0]), randint(0, displayRange[1]) )

    def draw(self, display : pygame.display):
        display.blit(self, self._position)

    def beEaten(self):
        super().fillColor((255, 255, 255))
        self._position = ( randint(0, self.__displayRange[0]), randint(0, self.__displayRange[1]) )
    