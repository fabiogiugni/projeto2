import pygame
from entities.apple import Apple
from entities.snake import Snake
from ui.screen import Screen
from utils.settings import SCREEN_HEIGHT, SCREEN_WIDTH

class Game(Screen):
    def __init__(self, game):
        super().__init__(game)

        SCREEN_RANGE = (SCREEN_WIDTH, SCREEN_HEIGHT)

        self.apple = Apple(SCREEN_RANGE, image_path="assets/apple.png")
        self.snake = Snake(SCREEN_RANGE)

        self.clock = pygame.time.Clock()

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.snake.turn("LEFT")
            elif event.key == pygame.K_RIGHT:
                self.snake.turn("RIGHT")
            elif event.key == pygame.K_UP:
                self.snake.turn("UP")
            elif event.key == pygame.K_DOWN:
                self.snake.turn("DOWN")

    def hover(self):
        pass

    def update(self):
        self.snake.walk()

        if self.snake.colide(self.apple):
            self.snake.grow()
            self.apple.beEaten()

    def draw(self, display):
        super().draw(display)
        self.clock.tick(20)


        self.apple.draw(display)
        self.snake.draw(display)
