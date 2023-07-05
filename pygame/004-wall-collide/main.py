import pygame
import sys

from src.config import *
from src.tilemap import *
from src.camera import Camera
from src.player import Player
from src.spritesheet import Spritesheet
from src.animation import Animation

class Game:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption("animation")

        self.clock = pygame.time.Clock()
        self.game_over = False

        self.new_game()
 

    def new_game(self):
        self.all_sprites = pygame.sprite.Group()
        self.wall_sprites = pygame.sprite.Group()

        player_idle_spritesheet = Spritesheet("assets/warrior/idle", 240, SCALE)
        player_run_spritesheet = Spritesheet("assets/warrior/run", 100, SCALE)
        
        player_anim = Animation()
        player_anim.add(PLAYER_IDLE, player_idle_spritesheet)
        player_anim.add(PLAYER_RUN, player_run_spritesheet)

        self.map = Tilemap(self, 1)
        self.player = Player(self, player_anim, 10, "assets/warrior/sprite.png", (100, 100), scale=SCALE)
        self.camera = Camera(self.player, 640, 480)

        self.all_sprites.add(self.player)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
                pygame.quit()
                sys.exit()

    def update(self):
        self.camera.scroll()
        self.map.update()
        self.all_sprites.update()
        pygame.display.flip()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.map.draw(self.screen)
        
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, (sprite.rect.topleft + self.camera.offset))

    def run(self):
        while not self.game_over:
            self.clock.tick(FPS)

            self.check_events()
            self.draw()
            self.update()

if __name__ == "__main__":
    game = Game()
    game.run()