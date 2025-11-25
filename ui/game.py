import pygame
from entities.apple import Apple
from entities.snake import Snake
from ui.screen import Screen
from utils.settings import SCREEN_HEIGHT, SCREEN_WIDTH, WHITE, LIGHT_GREEN, LIGHT_RED
from ui.scoreBoard import ScoreBoard


class Game(Screen):
    def __init__(self, game):
        super().__init__(game)

        SCREEN_RANGE = (SCREEN_WIDTH, SCREEN_HEIGHT)
        self.apple = Apple(SCREEN_RANGE, image_path="assets/apple.png")
        self.snake = Snake(SCREEN_RANGE)

        self.press_text_rect = None

        self.clock = pygame.time.Clock()
        self.scoreboard = ScoreBoard(self.game.display)
        self.player_name = self.game.player_name
        print(self.player_name)
        self.death_sound_played = False
        pygame.mixer.music.load("assets/loop.ogg")
        pygame.mixer.music.set_volume(self.game.volume) 
        pygame.mixer.music.play(-1)

        self.saved = False




    def handle_events(self, event):
        if self.snake.getIsAlive():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.snake.turn("LEFT")
                elif event.key == pygame.K_RIGHT:
                    self.snake.turn("RIGHT")
                elif event.key == pygame.K_UP:
                    self.snake.turn("UP")
                elif event.key == pygame.K_DOWN:
                    self.snake.turn("DOWN")

        else:
            pygame.mixer.music.stop()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    from ui.start import Start
                    self.game.current_screen = Start(self.game)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.press_text_rect and self.press_text_rect.collidepoint(pygame.mouse.get_pos()):
                    from ui.start import Start
                    self.game.current_screen = Start(self.game)

    def hover(self):
        pass

    def update(self):
        if self.snake.getIsAlive():
            self.snake.walk()

            if self.snake.colide(self.apple):
                self.snake.grow()
                self.apple.beEaten()
                self.scoreboard.increase_apple()

            self.scoreboard.update_time()

        else:
            self.update_blinker()
            self.scoreboard.freeze()

    def draw_border(self, display):
        tile = 5

        for x in range(0, SCREEN_WIDTH, tile):
            pygame.draw.polygon(display, LIGHT_GREEN, [(x, 0), (x + tile // 2, tile), (x + tile, 0)])

        for x in range(0, SCREEN_WIDTH, tile):
            pygame.draw.polygon(display, LIGHT_GREEN, [(x, SCREEN_HEIGHT), (x + tile // 2, SCREEN_HEIGHT - tile), (x + tile, SCREEN_HEIGHT)])

        for y in range(0, SCREEN_HEIGHT, tile):
            pygame.draw.polygon(display, LIGHT_GREEN, [(0, y), (tile, y + tile // 2), (0, y + tile)])

        for y in range(0, SCREEN_HEIGHT, tile):
            pygame.draw.polygon(display, LIGHT_GREEN, [(SCREEN_WIDTH, y), (SCREEN_WIDTH - tile, y + tile // 2), (SCREEN_WIDTH, y + tile)])

    def draw_bloody_border(self, display):
        tile = 12
        radius = 7

        for x in range(0, SCREEN_WIDTH, tile):
            pygame.draw.circle(display, LIGHT_RED, (x, radius), radius)

        for x in range(0, SCREEN_WIDTH, tile):
            pygame.draw.circle(display, LIGHT_RED, (x, SCREEN_HEIGHT - radius), radius)

        for y in range(0, SCREEN_HEIGHT, tile):
            pygame.draw.circle(display, LIGHT_RED, (radius, y), radius)

        for y in range(0, SCREEN_HEIGHT, tile):
            pygame.draw.circle(display, LIGHT_RED, (SCREEN_WIDTH - radius, y), radius)

    def draw(self, display):
        super().draw(display)

        if self.snake.getIsAlive():
            self.clock.tick(self.game.difficulty)
            self.draw_border(display)
            self.apple.draw(display)
            self.snake.draw(display)

        else:
            self.draw_bloody_border(display)

            color_main = WHITE if self.should_blink else LIGHT_RED
            title = self.title_font.render("VOCÊ MORREU!", False, color_main)
            display.blit(title, (self.game.size[0] // 2 - title.get_width() // 2, 120))

            color = LIGHT_RED if self.should_blink else WHITE
            press = self.text_font.render("Aperte ESPAÇO para retornar", False, color)

            x = self.game.size[0] // 2 - press.get_width() // 2
            y = 260

            self.press_text_rect = pygame.Rect(x, y, press.get_width(), press.get_height())
            display.blit(press, (x, y))
            if (not self.death_sound_played):
              pygame.mixer.music.stop()
              pygame.mixer.music.load("assets/sad.mp3")
              pygame.mixer.music.set_volume(self.game.volume) 
              pygame.mixer.music.play(-1)
              self.death_sound_played = True
            
            if not self.saved:
                from utils.database import Database
                try:
                    db = Database()
                    db.insertScore(self.player_name, self.scoreboard.apples, self.scoreboard.time, self.scoreboard.score)
                    db.close()
                    self.saved = True
                except Exception as e:
                    print(f"Erro ao salvar score no DB: {e}")
                    self.saved = True

        self.scoreboard.draw()
