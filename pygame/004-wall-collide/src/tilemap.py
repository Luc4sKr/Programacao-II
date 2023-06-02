import pygame
import csv

from os import listdir

from .config import *
from .utils import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, scale=1) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(f"assets/tilesets/{image_path}")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale, self.image.get_height() * scale))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.hitbox = get_mask_rect(self.image, *self.rect.topleft)


class Tilemap:
    def __init__(self, game, level: int) -> None:

        self.all_sprites = game.all_sprites
        self.wall_sprites = game.wall_sprites

        self.files = f"assets/levels/{level}"
        self.floor_sprites = pygame.sprite.Group()
        self.wall_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        data = self.load_tiles()

        for file, tileset in data.items():
            for y, row in enumerate(tileset):
                for x, tile in enumerate(row):
                    if int(tile) > 0:
                        tile = Tile(f"{file}/{tile.strip()}.png", x * 16 * SCALE, y * 16 * SCALE, scale=SCALE)
                        self.all_sprites.add(tile)

                        if file == "wall":
                            self.wall_sprites.add(tile)

    def load_tiles(self):
        files = {}
        for file in listdir(self.files):
            world_data = []
            column_data = []
            with open(f"{self.files}/{file}", newline="") as csvfile:
                reader = csv.reader(csvfile, delimiter=",")
                for x, row in enumerate(reader):
                    column_data = []
                    for y, tile in enumerate(row):
                        column_data.append(tile)
                    world_data.append(column_data)
            files[file[:-4]] = world_data
        return files
    
    def draw(self, screen):
        self.floor_sprites.draw(screen)

    def update(self):
        self.floor_sprites.update()