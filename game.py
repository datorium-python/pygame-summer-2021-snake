import pygame
import constants
import random

from models import Snake, Apple

pygame.init()

clock = pygame.time.Clock()
font = pygame.font.SysFont('couriernew', 24)

def show_score(window, score):
    text = font.render(f"SCORE: {score}", True, constants.FONT_COLOR)
    coordinates = (10, 10)
    window.blit(text, coordinates)


def render(window, snake, apple, score):

    window.fill(constants.BACKGROUND_COLOR)

    snake.show(window)
    apple.show(window)
    show_score(window, score)

    pygame.display.update()


def game(window):

    snake = Snake(
        x=random.randint(0, window.get_width() - Snake.rectangle_size),
        y=random.randint(0, window.get_height() - Snake.rectangle_size)
    )

    apple = Apple(
        x=random.randint(0, window.get_width() - Apple.rectangle_size),
        y=random.randint(0, window.get_height() - Apple.rectangle_size)
    )

    score = 0

    is_running = True
    while is_running:

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                is_running = False   

            if event.type == pygame.KEYDOWN:  

                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    snake.y_change = -snake.rectangle_size
                    snake.x_change = 0

                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    snake.y_change = 0
                    snake.x_change = -snake.rectangle_size

                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    snake.y_change = snake.rectangle_size
                    snake.x_change = 0

                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    snake.y_change = 0
                    snake.x_change = snake.rectangle_size

        snake.move()

        if snake.is_out_border(window) or snake.is_crossing_iself():
            is_running = False

        head = snake.rectangle_list[-1]
        if apple.is_eaten(head):
            score += 1

            snake.length += 1

            apple.x = random.randint(0, window.get_width() - Apple.rectangle_size)
            apple.y = random.randint(0, window.get_height() - Apple.rectangle_size)

        render(window, snake, apple, score)
        clock.tick(constants.FPS)
