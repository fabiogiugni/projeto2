import pygame
from utils.settings import WHITE, LIGHT_GREEN
from ui.screen import Screen
from ui.menuScreen import MenuScreen

class StartScreen(Screen):
    def __init__(self, game):
        super().__init__(game)
        self.press_text_rect = None  

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.game.current_screen = MenuScreen(self.game)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.press_text_rect and self.press_text_rect.collidepoint(pygame.mouse.get_pos()):
                self.game.current_screen = MenuScreen(self.game)

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

        color = LIGHT_GREEN if self.should_blink else WHITE
        press = self.text_font.render("Aperte ESPAÇO para iniciar", False, color)

        x = self.game.size[0]//2 - press.get_width()//2
        y = 260

        self.press_text_rect = pygame.Rect(x, y, press.get_width(), press.get_height())

        display.blit(press, (x, y))
