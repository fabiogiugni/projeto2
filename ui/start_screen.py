import pygame
class StartScreen:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.SysFont('Arial', 30) 

    def update(self):
        pass

    def draw(self, display):
        display.fill((0, 0, 0))
        text = self.font.render("Aperte Espaço Para Iniciar", True, (255, 255, 255))
        display.blit(text, (60, 280))
