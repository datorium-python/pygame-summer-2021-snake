import pygame
from pygame import constants
import constants

# ir darbības: metodes
# ir apraksts: aribūts - IR PAVEIKTS

class Snake:

    rectangle_size = 20

    def __init__(self, x, y):
        # __init__ -> initialize -> izveidot
        # __init__ metode veido jaunu objektu pēc klases apraksta

        self.rectangle_list = []

        first_rectangle = pygame.Rect(
            x,
            y,
            Snake.rectangle_size,
            Snake.rectangle_size
        )
        self.rectangle_list.append(first_rectangle)

        self.x_change = 0
        self.y_change = 0

        self.length = 1

    def show(self, window):
        
        for rectangle in self.rectangle_list:
            pygame.draw.rect(window, constants.SNAKE_COLOR, rectangle)

        pygame.draw.rect(window, constants.HEAD_COLOR, self.rectangle_list[-1])
        

    def move(self):
        # -1 ir pirmā (visjaunākais) kvadrāta indekss
        # 0 ir pēdējā (visvecākais) kvadrāta idekss

        first_x = self.rectangle_list[-1].left # left = x
        first_y = self.rectangle_list[-1].top # top = y

        new_rectangle = pygame.Rect(
            first_x + self.x_change,
            first_y + self.y_change,
            Snake.rectangle_size,
            Snake.rectangle_size
        )
        self.rectangle_list.append(new_rectangle)

        if len(self.rectangle_list) > self.length:
            self.rectangle_list.pop(0)
        
    def is_crossing_iself(self):
        
        fist_rectangle = self.rectangle_list[-1]

        if fist_rectangle.collidelist(self.rectangle_list[:-1]) == -1:
            return False

        return True

    def is_out_border(self, window):

        fist_rectangle = self.rectangle_list[-1]
        window_rectangle = window.get_rect()

        # True, ja čūska ir ekrānā
        is_in_border = window_rectangle.contains(fist_rectangle)

        # True, ja čūska ārpus ekrāna
        return not is_in_border


class Apple:

    rectangle_size = 15

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self, window):
        
        rectangle = pygame.Rect(
            self.x,
            self.y,
            Apple.rectangle_size,
            Apple.rectangle_size
        )

        pygame.draw.rect(window, constants.APPLE_COLOR, rectangle)

    def is_eaten(self, rectangle):
        
        apple_rectangle = pygame.Rect(
            self.x,
            self.y,
            Apple.rectangle_size,
            Apple.rectangle_size
        )

        # returns True or False
        return apple_rectangle.colliderect(rectangle)
