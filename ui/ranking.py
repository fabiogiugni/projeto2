import pygame
from utils.settings import WHITE, LIGHT_GREEN, BLACK, GOLDEN, SILVER, BROWN
from ui.screen import Screen
from utils.database import Database

class Ranking(Screen):
    def __init__(self, game):
        super().__init__(game)
        self.scores = []
        self.button_font = pygame.font.Font("assets/Jersey25-Regular.ttf", 45)

        # --- Scroll ---
        self.scroll_offset = 0
        self.max_scroll = 0
        self.scroll_speed = 30

        try:
            db = Database()
            self.scores = db.getHighScores()
            db.close()
        except Exception as e:
            print("Erro ao carregar ranking:", e)
            self.scores = []

        # rect temporário
        self.back_rect = pygame.Rect(0, 0, 1, 1)

    def handle_events(self, event):

        # --- SCROLL DO MOUSE ---
        if event.type == pygame.MOUSEWHEEL:
            self.scroll_offset -= event.y * self.scroll_speed
            self.scroll_offset = max(0, min(self.scroll_offset, self.max_scroll))

        # --- CLIQUE ---
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()

            # converter para coordenadas internas da list_surface
            local_y = my - 320 + self.scroll_offset  # 320 = topo da viewport

            if self.back_rect.collidepoint(mx, local_y):
                from ui.menu import Menu
                self.game.current_screen = Menu(self.game)

    def hover(self):
        pass

    def update(self):
        self.update_blinker()

    def draw(self, display):
        super().draw(display)

        # Título
        title = self.title_font.render("SNAKE GAME", False, WHITE)
        display.blit(title, (self.game.size[0]//2 - title.get_width()//2, 100))

        # Subtítulo
        subtitle_color = WHITE if not self.should_blink else LIGHT_GREEN
        subtitle = self.text_font.render("Ranking", False, subtitle_color)
        display.blit(subtitle, (self.game.size[0]//2 - subtitle.get_width()//2, 220))

        # Cabeçalho
        header = self.text_font.render("Name         Apples      Time      Score", False, WHITE)
        display.blit(header, (self.game.size[0]//2 - header.get_width()//2, 280))

        pygame.draw.line(
            display, WHITE,
            (self.game.size[0]//2 - header.get_width()//2, 310),
            (self.game.size[0]//2 + header.get_width()//2, 310),
            2
        )

        # --- ÁREA DE SCROLL ---
        viewport_rect = pygame.Rect(0, 320, self.game.size[0], 260)

        # altura total da surface, incluindo botão
        content_height = len(self.scores) * 40 + 120

        list_surface = pygame.Surface((self.game.size[0], content_height), pygame.SRCALPHA)

        start_y = 10
        line_height = 40

        # --- DESENHA TODA A LISTA ---
        for i, row in enumerate(self.scores):
            _id, name, apples, time, score = row

            name_text = f"{name:<12}"
            apples_text = f"{apples:>3}"
            time_text = f"{time:>4}"
            score_text = f"{score:>5}"

            line_text = f"{name_text}   {apples_text}        {time_text}       {score_text}"

            text_color = BLACK if i == 0 else WHITE
            text = self.text_font.render(line_text, False, text_color)

            y_pos = start_y + i * line_height

            # destaque top 1
            if i == 0:
                highlight_rect = pygame.Rect(
                    self.game.size[0]//2 - text.get_width()//2 - 10,
                    y_pos - 5,
                    text.get_width() + 20,
                    text.get_height() + 10
                )
                pygame.draw.rect(list_surface, LIGHT_GREEN, highlight_rect, border_radius=5)
                pygame.draw.rect(list_surface, WHITE, highlight_rect, 2, border_radius=5)

            # desenha linha
            list_surface.blit(text, (self.game.size[0]//2 - text.get_width()//2, y_pos))

            # medalhas top 3
            if i < 3:
                medal_colors = [GOLDEN, SILVER, BROWN]
                medal_radius = 10
                medal_x = self.game.size[0]//2 - header.get_width()//2 - 20
                medal_y = y_pos + text.get_height()//2

                pygame.draw.circle(list_surface, medal_colors[i], (medal_x, medal_y), medal_radius)

                medal_text = self.text_font.render(str(i+1), False, BLACK)
                list_surface.blit(
                    medal_text,
                    (medal_x - medal_text.get_width()//2, medal_y - medal_text.get_height()//2)
                )

        # --- BOTÃO VOLTAR DENTRO DO SCROLL ---
        back_text = self.button_font.render("Voltar", False, WHITE)
        back_x = self.game.size[0]//2 - back_text.get_width()//2
        back_y = content_height - 70

        self.back_rect = pygame.Rect(back_x, back_y, back_text.get_width(), back_text.get_height())

        pygame.draw.rect(list_surface, LIGHT_GREEN, self.back_rect.inflate(20, 20), border_radius=12)
        list_surface.blit(back_text, (back_x, back_y))

        # --- LIMITA SCROLL ---
        self.max_scroll = max(0, content_height - viewport_rect.height)

        # --- DESENHA SOMENTE A PARTE VISÍVEL ---
        display.blit(
            list_surface,
            (0, 320),
            pygame.Rect(0, self.scroll_offset, self.game.size[0], viewport_rect.height)
        )
