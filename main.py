import pygame
import constants
import menu
import game

pygame.init()

window = pygame.display.set_mode(constants.SIZE)
pygame.display.set_caption("čūskai garšo āboli :p")


while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            game.game(window)

    menu.menu(window)