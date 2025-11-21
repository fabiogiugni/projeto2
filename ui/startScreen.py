import pygame
from utils.settings import WHITE, GREEN_WHITE
from ui.screen import Screen
from ui.menuScreen import MenuScreen

class StartScreen(Screen):
    def __init__(self, game):
        super().__init__(game)

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.game.current_screen = MenuScreen(self.game)

    def update(self):
        self.update_blinker()

    def draw(self, display):
        super().draw(display) 

        title = self.title_font.render("SNAKE GAME", False, WHITE)
        display.blit(
            title,
            (self.game.size[0]//2 - title.get_width()//2, 100)
        )

        if (self.should_blink):
            press = self.text_font.render("Aperte ESPAÇO para iniciar", False, WHITE)
            display.blit(
                press,
                (self.game.size[0]//2 - press.get_width()//2, 330)
            )
        else:
            press = self.text_font.render("Aperte ESPAÇO para iniciar", False, GREEN_WHITE)
            display.blit(
                press,
                (self.game.size[0]//2 - press.get_width()//2, 330)
            )
