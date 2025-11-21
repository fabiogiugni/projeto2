import pygame
from utils.settings import WHITE, LIGHT_GREEN
from ui.screen import Screen

class MenuScreen(Screen):
    def __init__(self, game):
        super().__init__(game)
        
        self.__base_options = [
            "Iniciar Jogo",
            "Ranking",
            "Configurações",
        ]
        self.__startYPosition = 220
        self.__gap = 80
        self.__positions=[]
        self.__hover_index = None

        
    def handle_events(self, event):
        pass

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
        title = self.title_font.render("SNAKE GAME", False, WHITE)
        display.blit(
            title,
            (self.game.size[0]//2 - title.get_width()//2, 100)
        )

        for index, item in enumerate(self.__base_options):   
            text = self.text_font.render(item, False, WHITE)
            self.__positions.append((
                self.game.size[0]//2 - text.get_width()//2,
                self.__startYPosition + self.__gap * index,
                text.get_width(),
                text.get_height()
            ))
            if self.__hover_index == index and self.should_blink:
                text = self.text_font.render(item, False, LIGHT_GREEN)

            else:
                text = self.text_font.render(item, False, WHITE)

            display.blit(
                text,
                (self.game.size[0]//2 - text.get_width()//2, self.__startYPosition + self.__gap*index)
            )

