import pygame
from abc import ABC, abstractmethod

class Screen(ABC):
    def __init__(self, game):
        self.game = game
        self.title_font = pygame.font.Font("assets/Jersey25-Regular.ttf", 10)
        self.text_font = pygame.font.Font("assets/Jersey25-Regular.ttf", 36)
        self.background = pygame.image.load("assets/background.jpg").convert()
        self.background = pygame.transform.scale(
            self.background, self.game.size
        )

    @abstractmethod
    def handle_events(self, events):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self, display):
        display.blit(self.background, (0, 0))
