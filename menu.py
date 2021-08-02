import pygame
import constants

pygame.init()
font = pygame.font.SysFont('couriernew', 24)


def menu(window):

    window.fill(constants.BACKGROUND_COLOR)

    message = 'PRESS ANY KEY TO PLAY'
    text = font.render(message, True, constants.FONT_COLOR)

    x = window.get_width() / 2 - text.get_width() / 2
    y = window.get_height() / 2 - text.get_height() / 2
    coordinates = (x, y)

    window.blit(text, coordinates)
    pygame.display.update()