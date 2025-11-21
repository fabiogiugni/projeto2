import pygame
import time
from utils.settings import *
from ui.scoreBoard import ScoreBoard   # ajuste o nome do arquivo se necessário

pygame.init()

# Configuração básica da janela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ScoreBoard Test")
clock = pygame.time.Clock()


# Criar o ScoreBoard
scoreboard = ScoreBoard(screen)


# Loop principal
running = True
while running:
    dt = clock.tick(60) / 1000  # delta time (não usado, mas útil)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Teste: aperte ESPAÇO para comer maçã
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                scoreboard.increaseApple()

    # Atualizar tempo
    scoreboard.updateTime()
    # Desenhar
    screen.fill(BLACK)
    scoreboard.draw()
    pygame.display.flip()

pygame.quit()
