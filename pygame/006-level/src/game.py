import pygame, sys

from .constants import *
from .menu import MainMenu

class Game:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption("Dungeon Warriors")
        
        self.clock = pygame.time.Clock()
        self.main_menu = MainMenu(self)
        self.game_over = False


    def start(self):
        self.main_menu.run()


    def new_game(self):
        self.game_over = False
        
        # carregar as sprites, grupos, objetos, player, camera, level...
        # object handler

        self.run()

    def run(self):        
        while not self.game_over:
            self.clock.tick(FPS)
            self.check_events()
            self.draw()
            self.update()


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
                pygame.quit()
                sys.exit()


    def update(self):
        pygame.display.flip()


    def draw(self):
        self.screen.fill(BLACK) 