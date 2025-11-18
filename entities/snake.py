import pygame
from pygame import Surface
from .snakeBlock import SnakeBlock

class Snake:
    def __init__(self, displayRange : tuple, position : tuple = (100, 100)):
        self.__position = position
        self.__size = 3
        self.__blocks = [SnakeBlock((50, 80)), SnakeBlock((50, 65)), SnakeBlock((50, 50))]
        self.__direction = "DOWN"
        for b in self.__blocks:
            b.turn(self.__direction)

    def draw(self, display : pygame.display):
        for b in self.__blocks:
            b.fillColor((0, 255, 0))
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

    def die(self):
        pass
        
        