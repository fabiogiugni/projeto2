import pygame
from pygame import Surface
from .block import Block

class Snake:
    def __init__(self, position : tuple):
        self.__position = position
        self.__size = 3
        self.__blocks = [Block((50, 80)), Block((50, 65)), Block((50, 50))]
        self.__direction = "DOWN"
        for b in self.__blocks:
            b.turn(self.__direction)

    def draw(self, display : pygame.display):
        for b in self.__blocks:
            b.draw(display)

    def turn(self, direction : str):
        self.__direction = direction
        
                

    def walk(self):
        stop = False
        for b in self.__blocks:
            if (not stop) and b.direction != self.__direction:
                b.turn(self.__direction)
                stop = True
        for b in self.__blocks:
            b.walk()
        
        