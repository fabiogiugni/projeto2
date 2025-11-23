import pygame
from utils.settings import WHITE, LIGHT_GREEN
from ui.screen import Screen

class Configs(Screen):
    def __init__(self, game):
        super().__init__(game)

    def handle_events(self, event):
        pass
    
    def update(self):
        self.update_blinker()

    def hover(self):
        pass

    def draw(self, display):
        super().draw(display) 

        title = self.title_font.render("SNAKE GAME", False, WHITE)
        display.blit(
            title,
            (self.game.size[0]//2 - title.get_width()//2, 100)
        )

        if (not self.should_blink):
            press = self.text_font.render("Configs", False, WHITE)
            display.blit(
                press,
                (self.game.size[0]//2 - press.get_width()//2, 260)
            )
        else:
            press = self.text_font.render("Configs", False, LIGHT_GREEN)
            display.blit(
                press,
                (self.game.size[0]//2 - press.get_width()//2, 260)
            )
