import pygame

from .utils import *
from .constants import *

class Button:
    def __init__(self, screen, left, top, width, height, text, font_size=20, button_color=BLACK, font_color=WHITE, border_color=WHITE):
        button_border = pygame.Rect(int(left - 2), int(top - 2), int(width + 4), int(height + 4))
        button = pygame.Rect(int(left), int(top), int(width), int(height))
        
        pygame.draw.rect(screen, border_color, button_border)
        pygame.draw.rect(screen, button_color, button)

        draw_text(screen, text, font_size, font_color, left + (width / 2), top + (height / 2))



"""

@staticmethod
def draw_button(screen, left, top, width, height, text, font_size=20, button_color=Const.BLACK, font_color=Const.WHITE, border_color=Const.WHITE):
    button_border = pygame.Rect(int(left - 2), int(top - 2), int(width + 4), int(height + 4))
    button = pygame.Rect(int(left), int(top), int(width), int(height))
    pygame.draw.rect(screen, border_color, button_border)
    pygame.draw.rect(screen, button_color, button)
    Draw_util.draw_text(screen, text, font_size, font_color, left + (width / 2), top + (height / 2))
    return button

"""