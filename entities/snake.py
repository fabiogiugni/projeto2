import pygame
from pygame import Surface
from .block import Block
from .snakeBlock import SnakeBlock

from utils.settings import PURPLE, CYAN, GREEN, DARK_GREEN

class Snake:
    def __init__(self, displayRange : tuple, position : tuple = (45, 45)):
        self.__position = position
        self.__size = 3
        self.__blocks = [SnakeBlock((45, 60), image_path="assets/snake.png"), SnakeBlock((45, 45)), SnakeBlock((45, 30))]
        self.__direction = "DOWN"
        for b in self.__blocks:
            b.fillColor(GREEN)
            b.turn(self.__direction)

    def draw(self, display : pygame.display):
        for b in self.__blocks:
            b.draw(display)

    def turn(self, direction : str):
        if direction == "LEFT" and self.__direction == "RIGHT":
            self.die()
        if direction == "RIGHT" and self.__direction == "LEFT":
            self.die()
        if direction == "DOWN" and self.__direction == "UP":
            self.die()
        if direction == "UP" and self.__direction == "DOWN":
            self.die()

        self.__direction = direction
          

    def walk(self):

        for i in range(1, len(self.__blocks)):
            self.__blocks[len(self.__blocks) - i].position = self.__blocks[len(self.__blocks) - i - 1].position

        self.__blocks[0].turn(self.__direction)
        self.__blocks[0].walk()

    def die(self):
        for b in self.__blocks:
            b.fillColor(CYAN)

    def grow(self):
        new_block = SnakeBlock((-15, -15))
        new_block.fillColor(GREEN)
        self.__blocks.append(new_block)

    def colide(self, block : Block):
        if block.position == self.__blocks[0].position:
            return True
        else:
            return False