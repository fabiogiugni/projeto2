import pygame

from entities.apple import Apple
from entities.body import Body


pygame.init()

display = pygame.display.set_mode((600, 600))

pygame.display.set_caption('Snake Game')

apple = Apple()
snake = Body((100, 100))
direction = "DOWN"

while True:
    pygame.time.delay(100)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        direction = "LEFT"
    if keys[pygame.K_RIGHT]:
        direction = "RIGHT"
    if keys[pygame.K_UP]:
        direction = "UP"
    if keys[pygame.K_DOWN]:
        direction = "DOWN"

    snake.turn(direction)
        

    display.fill((255,255,255))
    snake.draw(display)
    apple.draw(display, (50, 50))

    snake.walk()
    

    pygame.display.update()