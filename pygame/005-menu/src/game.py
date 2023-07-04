import pygame
import sys

from src.constants import *
from src.menu import MainMenu


class Game:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption("Dungeon Warriors")
        
        self.clock = pygame.time.Clock()
        self.game_over = False
        self.main_menu = MainMenu(self)

    def start(self):
        self.main_menu.run()

    def new_game(self):
        self.game_over = False

        self.run()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
                pygame.quit()
                sys.exit()

    def update(self):
        pygame.display.flip()
        pygame.display.set_caption(f"FPS: {self.clock.get_fps()}")

    def draw(self):
        self.screen.fill(BLACK)

    def run(self):        
        while not self.game_over:
            self.clock.tick(FPS)

            self.check_events()
            self.draw()
            self.update()

