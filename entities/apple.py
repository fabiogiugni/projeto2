import pygame
from .block import Block
from random import randint

from utils.settings import RED, APPLE_SIZE, SNAKE_SPEED

class Apple(Block):
    def __init__(self, displayRange : tuple,  image_path: str = None):
        super().__init__((APPLE_SIZE, APPLE_SIZE), image_path=image_path)
        super().fill(RED)
        self.__displayRange = displayRange
        self.__changePosition()

    def __changePosition(self):
        max_x = self.__displayRange[0] // SNAKE_SPEED - 1
        max_y = self.__displayRange[1] // SNAKE_SPEED - 1

        self._position = (
            randint(0, max_x - SNAKE_SPEED) * SNAKE_SPEED,
            randint(0, max_y - SNAKE_SPEED) * SNAKE_SPEED
        )

    def beEaten(self):
        self.__changePosition()