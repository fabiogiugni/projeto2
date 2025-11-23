import pygame
from screenInterface import ScreenInterface

class Screen(ScreenInterface):
    def __init__(self, game):
        self.game = game
        self.title_font = pygame.font.Font("assets/Jersey25-Regular.ttf", 60)
        self.text_font = pygame.font.Font("assets/Jersey25-Regular.ttf", 36)
        self.background = pygame.image.load("assets/background.jpg").convert()
        self._blink_timer = 0
        self.should_blink = False

 
    # ---------- MÉTODOS CONCRETOS ----------
    def update_blinker(self, interval=30):
        self._blink_timer += 1

        if self._blink_timer >= interval:
            self.should_blink = not self.should_blink
            self._blink_timer = 0
    
    def draw(self, display):
        display.blit(self.background, (0, 0))
