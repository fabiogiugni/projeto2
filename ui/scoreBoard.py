import pygame
from utils.settings import LIGHT_GREEN

class ScoreBoard:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.apples = 0
        self.start_time = pygame.time.get_ticks()
        self.time = 0
        self.score = 0

        self.font = pygame.font.Font("assets/Jersey25-Regular.ttf", 28)

        # Criar apenas UMA VEZ
        self.overlay_surface = pygame.Surface((500, 50), pygame.SRCALPHA)
        self.overlay_surface.set_alpha(180)  # NÃO chamar no draw()

        self.frozen = False
        self.frozen_time = 0

    def update_score(self):
        self.score = (self.apples * 10) + (self.time * 1)

    def increase_apple(self):
        self.apples += 1
        self.update_score()

    def update_time(self):
        if self.frozen:
            return

        now = pygame.time.get_ticks()
        self.time = (now - self.start_time) // 1000
        self.update_score()

    def freeze(self):
        """Congela o tempo após morrer."""
        if not self.frozen:
            self.frozen = True
            self.frozen_time = self.time

    def draw(self):
        # limpar a surface sem recriar
        self.overlay_surface.fill((0, 0, 0, 0))

        apples_text = self.font.render(f"Maçãs: {self.apples}", True, LIGHT_GREEN)
        time_text   = self.font.render(f"Tempo: {self.time}", True, LIGHT_GREEN)
        score_text  = self.font.render(f"Nota: {self.score}", True, LIGHT_GREEN)

        spacing = 40 
        total_width = apples_text.get_width() + time_text.get_width() + score_text.get_width() + spacing * 2

        start_x = (self.overlay_surface.get_width() - total_width) // 2
        y = 0

        self.overlay_surface.blit(apples_text, (start_x, y))
        self.overlay_surface.blit(time_text, (start_x + apples_text.get_width() + spacing, y))
        self.overlay_surface.blit(score_text, (start_x + apples_text.get_width() + time_text.get_width() + spacing * 2, y))

        rect = self.overlay_surface.get_rect(center=(self.screen.get_width() // 2, 80))
        self.screen.blit(self.overlay_surface, rect)
