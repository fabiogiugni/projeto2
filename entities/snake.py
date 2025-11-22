import pygame
from pygame import Surface
from .block import Block
from .snakeBlock import SnakeBlock

from utils.settings import PURPLE, CYAN, GREEN, SNAKE_SIZE

class Snake:
    def __init__(self, displayRange : tuple, position : tuple = (45, 45)):
        self.__position = position
        self.__size = SNAKE_SIZE
        self.__blocks = [SnakeBlock((45, 60), image_path="assets/snake_head.png"), SnakeBlock((45, 45), image_path="assets/snake_body.png"), SnakeBlock((45, 30), image_path="assets/snake_body.png")]
        self.__direction = "DOWN"
        for b in self.__blocks:
            b.fillColor(GREEN)
            b.turn(self.__direction)

        self.__isAlive = True

    def draw(self, display : pygame.display):
        if self.__isAlive == False:
            return
        if self.__direction == "DOWN":
            rotation = 180
        if self.__direction == "UP":
            rotation = 0
        if self.__direction == "RIGHT":
            rotation = -90
        if self.__direction == "LEFT":
            rotation = 90

        for b in self.__blocks:
            b.setRotation(rotation=rotation)
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
        if self.__isAlive == False:
            return

        for i in range(1, len(self.__blocks)):
            self.__blocks[len(self.__blocks) - i].position = self.__blocks[len(self.__blocks) - i - 1].position

        self.__blocks[0].turn(self.__direction)
        self.__blocks[0].walk()

        for i in range(1, len(self.__blocks)):
            if self.__blocks[0].position == self.__blocks[i].position:
                self.die()

    def die(self):
        print("Cobra morta")
        self.__isAlive = False

    def grow(self):
        new_block = SnakeBlock((-15, -15), image_path="assets/snake_body.png")
        new_block.fillColor(GREEN)
        self.__blocks.append(new_block)
        self.__size += 1

    def colide(self, block : Block):
        if block.position == self.__blocks[0].position:
            return True
        else:
            return False