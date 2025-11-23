import pygame
from entities.apple import Apple
from entities.snake import Snake
from ui.screen import Screen
from utils.settings import SCREEN_HEIGHT, SCREEN_WIDTH, WHITE, GREY, LIGHT_GREEN

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


    def draw_border(self, display):
      tile = 5  # tamanho do serrilhado

      # Topo
      for x in range(0, SCREEN_WIDTH, tile):
          pygame.draw.polygon(display, LIGHT_GREEN, [
              (x, 0),
              (x + tile // 2, tile),
              (x + tile, 0)
          ])

      # Base
      for x in range(0, SCREEN_WIDTH, tile):
          pygame.draw.polygon(display, LIGHT_GREEN, [
              (x, SCREEN_HEIGHT),
              (x + tile // 2, SCREEN_HEIGHT - tile),
              (x + tile, SCREEN_HEIGHT)
          ])

      # Esquerda
      for y in range(0, SCREEN_HEIGHT, tile):
          pygame.draw.polygon(display, LIGHT_GREEN, [
              (0, y),
              (tile, y + tile // 2),
              (0, y + tile)
          ])

      # Direita
      for y in range(0, SCREEN_HEIGHT, tile):
          pygame.draw.polygon(display, LIGHT_GREEN, [
              (SCREEN_WIDTH, y),
              (SCREEN_WIDTH - tile, y + tile // 2),
              (SCREEN_WIDTH, y + tile)
          ])

    def draw(self, display):
        super().draw(display)
        self.draw_border(display)

        self.clock.tick(20)
        self.apple.draw(display)
        self.snake.draw(display)

        
