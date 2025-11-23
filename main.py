import pygame

from entities.apple import Apple
from entities.snake import Snake

from utils.settings import SCREEN_HEIGHT, SCREEN_WIDTH, CYAN, PURPLE

pygame.init()

SCREEN_RANGE = (SCREEN_WIDTH, SCREEN_HEIGHT)

display = pygame.display.set_mode(SCREEN_RANGE)

pygame.display.set_caption('Snake Game')

apple = Apple(SCREEN_RANGE, image_path="assets/apple.png")
snake = Snake(SCREEN_RANGE)
direction = "DOWN"

while True:
    pygame.time.delay(60)
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

    display.fill(CYAN)
    snake.draw(display)
    apple.draw(display)

    if snake.colide(apple):
        snake.grow()
        apple.beEaten()    

    pygame.display.update()