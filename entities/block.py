import pygame.display
from pygame import Surface

class Block(Surface):
    def __init__(self, position : tuple = (50, 50)):
        super().__init__((15, 15))
        super().fill((0, 255, 0))
        self.__position = position
        self.__direction = "DOWN"

    @property
    def direction(self):
        return self.__direction

    def draw(self, display : pygame.display):
        display.blit(self, self.__position)

    def turn(self, direction : str):
        self.__direction = direction

    def walk(self):
        if self.__direction == "LEFT":
            self.__position = (self.__position[0]-15, self.__position[1])
        if self.__direction == "RIGHT":
            self.__position = (self.__position[0]+15, self.__position[1])
        if self.__direction == "UP":
            self.__position = (self.__position[0], self.__position[1]-15)
        if self.__direction == "DOWN":
            self.__position = (self.__position[0], self.__position[1]+15)