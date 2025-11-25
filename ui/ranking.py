import pygame
from utils.settings import WHITE, LIGHT_GREEN, BLACK, GOLDEN, SILVER, BROWN
from ui.screen import Screen
from utils.database import Database

class Ranking(Screen):
    def __init__(self, game):
        super().__init__(game)
        self.scores = []
        self.button_font = pygame.font.Font("assets/Jersey25-Regular.ttf", 45)

        try:
            db = Database()
            self.scores = db.getHighScores()  # Lista de tuplas: (id, name, apples, time, score)
            db.close()
        except Exception as e:
            print("Erro ao carregar ranking:", e)
            self.scores = []

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()

            if self.back_rect.collidepoint(mx, my):
                from ui.menu import Menu
                self.game.current_screen = Menu(self.game)

    def hover(self):
        pass

    def update(self):
        self.update_blinker()

    def draw(self, display):
        super().draw(display)

        title = self.title_font.render("SNAKE GAME", False, WHITE)
        display.blit(
            title,
            (self.game.size[0]//2 - title.get_width()//2, 100)
        )

        # Subtítulo "Ranking"
        subtitle_color = WHITE if not self.should_blink else LIGHT_GREEN
        subtitle = self.text_font.render("Ranking", False, subtitle_color)
        display.blit(
            subtitle,
            (self.game.size[0]//2 - subtitle.get_width()//2, 220)
        )

        # Cabeçalho
        header = self.text_font.render("Name         Apples      Time      Score", False, WHITE)
        display.blit(
            header,
            (self.game.size[0]//2 - header.get_width()//2, 280)
        )

        pygame.draw.line(
            display, WHITE,
            (self.game.size[0]//2 - header.get_width()//2, 310),
            (self.game.size[0]//2 + header.get_width()//2, 310),
            2
        )

        start_y = 330
        line_height = 40

        # Desenhar ranking REAL vindo do banco
        for i, row in enumerate(self.scores):
            _id, name, apples, time, score = row

            name_text = f"{name:<12}"
            apples_text = f"{apples:>3}"
            time_text = f"{time:>4}"
            score_text = f"{score:>5}"

            line_text = f"{name_text}   {apples_text}        {time_text}       {score_text}"

            text_color = BLACK if i == 0 else WHITE
            text = self.text_font.render(line_text, False, text_color)

            y_pos = start_y + (i * line_height)

            # Destaque primeiro lugar
            if i == 0:
                highlight_rect = pygame.Rect(
                    self.game.size[0]//2 - text.get_width()//2 - 10,
                    y_pos - 5,
                    text.get_width() + 20,
                    text.get_height() + 10
                )
                pygame.draw.rect(display, LIGHT_GREEN, highlight_rect, border_radius=5)
                pygame.draw.rect(display, WHITE, highlight_rect, 2, border_radius=5)

            # Desenhar linha
            display.blit(
                text,
                (self.game.size[0]//2 - text.get_width()//2, y_pos)
            )

            # Medalhas top 3
            if i < 3:
                medal_colors = [GOLDEN, SILVER, BROWN]
                medal_radius = 10
                medal_x = self.game.size[0]//2 - header.get_width()//2 - 20
                medal_y = y_pos + text.get_height()//2

                pygame.draw.circle(display, medal_colors[i], (medal_x, medal_y), medal_radius)

                medal_text = self.text_font.render(str(i+1), False, BLACK)
                display.blit(
                    medal_text,
                    (medal_x - medal_text.get_width()//2, medal_y - medal_text.get_height()//2)
                )

        # Botão VOLTAR
        back_text = self.button_font.render("Voltar", False, WHITE if not self.should_blink else LIGHT_GREEN)
        back_x = self.game.size[0]//2 - back_text.get_width()//2
        back_y = 500

        self.back_rect = pygame.Rect(back_x, back_y, back_text.get_width(), back_text.get_height())
        display.blit(back_text, (back_x, back_y))
