import pygame

class StartScreen():
    def __init__(self, game):
        self.font = pygame.font.SysFont(None, 48)

    def update(self):
        pass

    def draw(self, display):
        display.fill((0, 0, 0))
        text = self.font.render("APERTE ESPAÇO PARA INICIAR", True, (255, 255, 255))
        display.blit(text, (60, 280))
