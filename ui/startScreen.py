import pygame
from utils.settings import WHITE
from ui.screen import Screen
from ui.menu import MenuScreen

class StartScreen(Screen):
    def __init__(self, game):
        super().__init__(game)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    super().game.current_screen = MenuScreen(self.game)

    def update(self):
        pass

    def draw(self, display):
        super().draw(display) 

        title = self.title_font.render("SNAKE GAME", True, WHITE)
        display.blit(
            title,
            (self.game.size[0]//2 - title.get_width()//2, 180)
        )

        press = self.text_font.render("Aperte ESPAÇO para iniciar", True, WHITE)
        display.blit(
            press,
            (self.game.size[0]//2 - press.get_width()//2, 330)
        )
