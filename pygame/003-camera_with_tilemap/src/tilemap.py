import pygame
import csv

from .config import *
from .object import Object

class Tilemap:
    def __init__(self, group) -> None:

        self.all_sprites = group

        self.csv_file = "assets/levels/level-1.csv"
        self.floor_sprites = pygame.sprite.Group()
        self.wall_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        data = self.open_file()
        print(data)

        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if int(tile) == 1:
                    img_obj = Object(f"assets/tilesets/floor/{int(tile)}.png", ( x * 16, y * 16))
                    self.all_sprites.add(img_obj)

    def open_file(self):
        world_data = []
        column_data = []
        with open(self.csv_file, newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            for x, row in enumerate(reader):
                for y, tile in enumerate(row):
                    column_data.append(tile)
                world_data.append(column_data)
        return world_data
    
    def draw(self, screen):
        self.floor_sprites.draw(screen)

    def update(self):
        self.floor_sprites.update()