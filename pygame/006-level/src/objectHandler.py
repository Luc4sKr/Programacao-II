import pygame

from .constants import *

from .spritesheet import Spritesheet
from .animation import Animation
from .player import Player
from .camera import Camera

class ObjectHandler:
    def __init__(self) -> None:
        self.all_sprites = pygame.sprite.Group()
        self.wall_sprites = pygame.sprite.Group()
        self.floor_sprites = pygame.sprite.Group()

        self.load_player()
        self.load_camera()


    def load_player(self):
        player_idle_spritesheet = Spritesheet("assets/characters/warrior/idle", 240, SCALE)
        player_run_spritesheet = Spritesheet("assets/characters/warrior/run", 100, SCALE)
        
        player_anim = Animation()
        player_anim.add(PLAYER_IDLE, player_idle_spritesheet)
        player_anim.add(PLAYER_RUN, player_run_spritesheet)

        self.player = Player(self, player_anim, 5, "assets/characters/warrior/sprite.png", (100, 100), scale=SCALE)
        self.all_sprites.add(self.player)


    def load_camera(self):
        self.camera = Camera(self.player, WIDTH, HEIGHT)


    def update(self):
        self.all_sprites.update()
        self.camera.scroll()


    def draw(self, screen):
        for sprite in self.all_sprites:
            screen.blit(sprite.image, (sprite.rect.topleft + self.camera.offset))

    
    