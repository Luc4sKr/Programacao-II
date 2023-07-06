import pygame, csv
from os import listdir

from pygame.sprite import AbstractGroup

from .constants import *
from .utils import *


class Map:
    def __init__(self) -> None:
        pass


class Tile(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, scale=SCALE) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(f"assets/tilesets/{image_path}")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale, self.image.get_height() * scale))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y