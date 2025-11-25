import pygame
from pygame import Surface
from .block import Block
from .snakeBlock import SnakeBlock
from .walkInterface import WalkInterface

from utils.settings import PURPLE, CYAN, GREEN, SNAKE_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH

class Snake(WalkInterface):
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

        self.__blocks[0].setRotation(rotation=rotation)

        for b in self.__blocks:
            b.draw(display)

    def turn(self, direction : str):
        if direction == "LEFT" and self.__direction == "RIGHT":
            return
        if direction == "RIGHT" and self.__direction == "LEFT":
            return
        if direction == "DOWN" and self.__direction == "UP":
            return
        if direction == "UP" and self.__direction == "DOWN":
            return

        self.__direction = direction
         

    def walk(self):
        if not self.__isAlive:
            return

        for i in range(1, len(self.__blocks)):
            self.__blocks[len(self.__blocks) - i].position = self.__blocks[len(self.__blocks) - i - 1].position

        self.__blocks[0].turn(self.__direction)
        self.__blocks[0].walk()
        
        for i in range(1, len(self.__blocks)):
            if self.__blocks[0].position == self.__blocks[i].position:
                self.die()

        x, y = self.__blocks[0].position
        if x < 0 or x >= SCREEN_WIDTH or y < 0 or y >= SCREEN_HEIGHT:
            self.die()


    def die(self):
        print("Cobra morta")
        self.__isAlive = False

    def grow(self):
        new_block = SnakeBlock((-100, -100), image_path="assets/snake_body.png")
        new_block.fillColor(GREEN)
        self.__blocks.append(new_block)
        self.__size += 1

    def colide(self, block : Block):
        delta_x = block.position[0] - self.__blocks[0].position[0]
        delta_y = block.position[1] - self.__blocks[0].position[1]

        if abs(delta_x) <= 15 and abs(delta_y) <= 15:
            return True
        else:
            return False
    
    def getIsAlive(self):
        return self.__isAlive
    
    @property
    def size(self):
        return self.__size