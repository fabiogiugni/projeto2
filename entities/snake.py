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

        for b in self.__blocks:
            b.setRotation(rotation=rotation)
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

        # salva posição anterior do bloco da frente
        prev_pos = self.__blocks[0].position

        # move a cabeça
        self.__blocks[0].turn(self.__direction)
        self.__blocks[0].walk()

        # move o corpo inteiro
        for i in range(1, len(self.__blocks)):
            current_pos = self.__blocks[i].position
            self.__blocks[i].position = prev_pos
            prev_pos = current_pos

        # checar colisão com o corpo (mas de forma segura)
        head_x, head_y = self.__blocks[0].position
        for block in self.__blocks[1:]:
            if block.position == (head_x, head_y):
                self.die()

        # bordas
        if head_x < 0 or head_x >= SCREEN_WIDTH or head_y < 0 or head_y >= SCREEN_HEIGHT:
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