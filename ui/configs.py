import pygame
from ui.screen import Screen
from utils.settings import WHITE, LIGHT_GREEN


class Configs(Screen):
    def __init__(self, game):
        super().__init__(game)

        self.volume = self.game.volume
        self.difficulty = self.game.difficulty

        self.slider_w = 220
        self.slider_h = 10

        self.volume_x = self.game.size[0]//2 - self.slider_w//2
        self.volume_y = 240

        self.diff_x = self.volume_x
        self.diff_y = 340

        self.button_font = pygame.font.Font("assets/Jersey25-Regular.ttf", 45)

        # Música
        pygame.mixer.music.load("assets/loop.ogg")
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play(-1)

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()

            # Volume slider
            if self.volume_y - 10 < my < self.volume_y + 20:
                if self.volume_x <= mx <= self.volume_x + self.slider_w:
                    self.volume = (mx - self.volume_x) / self.slider_w
                    pygame.mixer.music.set_volume(self.volume)

            # Difficulty slider
            if self.diff_y - 10 < my < self.diff_y + 20:
                if self.diff_x <= mx <= self.diff_x + self.slider_w:
                    self.difficulty = 5 + int((mx - self.diff_x) / self.slider_w * 25)

            # Botão voltar
            if self.back_rect.collidepoint(mx, my):
                self.game.volume = self.volume
                self.game.difficulty = self.difficulty

                from ui.menu import Menu
                self.game.current_screen = Menu(self.game)

    def hover(self):
        pass

    def update(self):
        self.update_blinker()

    def draw_slider(self, display, x, y, value, label):
        bar_rect = pygame.Rect(x, y, self.slider_w, self.slider_h)
        pygame.draw.rect(display, WHITE, bar_rect, 2)

        fill_width = int(self.slider_w * value)
        fill_rect = pygame.Rect(x, y, fill_width, self.slider_h)
        pygame.draw.rect(display, LIGHT_GREEN, fill_rect)

        text = self.text_font.render(f"{label}: {value}", False, WHITE)
        display.blit(text, (x + self.slider_w//2 - text.get_width()//2, y - 40))

    def draw(self, display):
        super().draw(display)

        title = self.title_font.render("CONFIGURAÇÕES", False, WHITE)
        display.blit(title, (self.game.size[0]//2 - title.get_width()//2, 100))

        # Volume slider
        self.draw_slider(display, self.volume_x, self.volume_y, self.volume, "Volume")

        # Difficulty slider normalized 0 a 1
        diff_norm = (self.difficulty - 5) / 25
        self.draw_slider(display, self.diff_x, self.diff_y, diff_norm, "Dificuldade")

        # Botão voltar
        back = self.button_font.render("Voltar", False, WHITE if not self.should_blink else LIGHT_GREEN)
        back_x = self.game.size[0]//2 - back.get_width()//2
        back_y = 440
        self.back_rect = pygame.Rect(back_x, back_y, back.get_width(), back.get_height())
        display.blit(back, (back_x, back_y))
