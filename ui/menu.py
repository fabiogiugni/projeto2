import pygame
from utils.settings import WHITE, LIGHT_GREEN
from ui.screen import Screen
from ui.game import Game
from ui.ranking import Ranking
from ui.configs import Configs

class Menu(Screen):
    def __init__(self, game):
        super().__init__(game)

        self.__base_options = [
            "Iniciar Jogo",
            "Ranking",
            "Configurações",
        ]
        
        self.__start_Y_position = 260
        self.__gap = 80
        self.__positions=[]
        self.__hover_index = None

        # Input de nome
        self.input_active = False
        self.input_text = ""
        self.input_rect = pygame.Rect(self.game.size[0]//2 - 150, 170, 300, 50)
        self.input_font = pygame.font.Font("assets/Jersey25-Regular.ttf", 35)

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_rect.collidepoint(event.pos):
                self.input_active = True
            else:
                self.input_active = False

            if event.button == 1 and self.__hover_index is not None:
                self.handle_click(self.__hover_index)

        if event.type == pygame.KEYDOWN and self.input_active:
            if event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
            elif len(self.input_text) < 12:  
                self.input_text += event.unicode

    def handle_click(self, index):
        if index == 0:  # Iniciar jogo
            if self.input_text.strip() == "":
                return  # Não deixa iniciar sem nome
            self.game.player_name = self.input_text
            self.game.current_screen = Game(self.game)

        elif index == 1:
            self.game.current_screen = Ranking(self.game)

        elif index == 2:
            self.game.current_screen = Configs(self.game)

    def update(self):
        self.hover()
        self.update_blinker()

    def hover(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.__hover_index = None

        for i, (x, y, w, h) in enumerate(self.__positions):
            rect = pygame.Rect(x, y, w, h)
            if rect.collidepoint(mouse_x, mouse_y):
                self.__hover_index = i
                break

    def draw(self, display):
        super().draw(display)
        self.__positions.clear()

        # Título
        title = self.title_font.render("SNAKE GAME", False, WHITE)
        display.blit(title, (self.game.size[0]//2 - title.get_width()//2, 80))

        # Input box
        pygame.draw.rect(display, LIGHT_GREEN if self.input_active else WHITE, self.input_rect, 2)
        text_surface = self.input_font.render(self.input_text or "Digite seu nome...", True, WHITE)
        display.blit(text_surface, (self.input_rect.x + 10, self.input_rect.y + 10))

        # Opções do menu
        for index, item in enumerate(self.__base_options):
            text = self.text_font.render(item, False, WHITE)
            self.__positions.append((
                self.game.size[0]//2 - text.get_width()//2,
                self.__start_Y_position + self.__gap * index,
                text.get_width(),
                text.get_height()
            ))

            color = LIGHT_GREEN if self.__hover_index == index and self.should_blink else WHITE
            text = self.text_font.render(item, False, color)

            display.blit(
                text,
                (self.game.size[0]//2 - text.get_width()//2, self.__start_Y_position + self.__gap*index)
            )
