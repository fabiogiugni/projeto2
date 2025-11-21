import pygame
from utils.settings import WHITE
from ui.screen import Screen

class MenuScreen(Screen):
    def __init__(self, game):
        super().__init__(game)

    def handle_events(self, event):
        pass

    def update(self):
        pass

    def draw(self, display):
        super().draw(display) 

        press = self.text_font.render("Funcionou", False, WHITE)
        display.blit(
            press,
            (self.game.size[0]//2 - press.get_width()//2, 330)
        )
