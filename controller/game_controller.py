import pygame

from ui.start_screen import StartScreen

# Essa classe é o controller geral. Ele vai gerenciar todas as páginas do projeto
# Ela não recebe nada no init e chama todas as outras páginas
class GameController:
    def __init__(self):
        pygame.init()

        self.size = (600, 600)
        self.display = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Snake Game")

        self.clock = pygame.time.Clock()

        self.current_screen = StartScreen(self)

    def run(self):
        while True:
            self.current_screen.update()
            self.current_screen.draw(self.display)

            pygame.display.update()
            self.clock.tick(60)
