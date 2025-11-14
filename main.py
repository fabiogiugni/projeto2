import pygame

from entities.apple import Apple
from entities.snake import Snake


pygame.init()

display = pygame.display.set_mode((600, 600))

pygame.display.set_caption('Snake Game')

apple = Apple()
snake = Snake((100, 100))
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
        snake.turn(direction)
    elif keys[pygame.K_RIGHT]:
        direction = "RIGHT"
        snake.turn(direction)
    elif keys[pygame.K_UP]:
        direction = "UP"
        snake.turn(direction)
    elif keys[pygame.K_DOWN]:
        direction = "DOWN"
        snake.turn(direction)

    snake.walk()

    display.fill((255,255,255))
    snake.draw(display)
    apple.draw(display, (50, 50))
    

    pygame.display.update()
