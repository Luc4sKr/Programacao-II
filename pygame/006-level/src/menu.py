import pygame, sys
from abc import ABC

from .ui.button import Button

from .constants import * 
from .utils import *


class Menu(ABC):
    def __init__(self, game) -> None:
        self.game = game
        self.show_menu = True

    def run(self):
        while self.show_menu:
            self.game.clock.tick(FPS)

            self.check_events()
            self.draw()
            self.update()

    def draw(self):
        self.game.screen.fill(BLACK)

    def update(self):
        pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.show_menu = False
                self.game.game_over = True
                pygame.quit()
                sys.exit()
            self.menu_events(event)


class MainMenu(Menu):
    def __init__(self, game) -> None:
        super().__init__(game)

        self.play_btn = Button("PLAY", HALF_WIDTH - 100, PLAY_BTN_TOP, 200, 50, callback_function=self.play)
        self.options_btn = Button("OPTIONS", HALF_WIDTH - 100, OPTIONS_BTN_TOP, 200, 50)
        self.exit_btn = Button("EXIT", HALF_WIDTH - 100, EXIT_BTN_TOP, 200, 50, callback_function=self.exit)


    def draw(self):
        super().draw()

        draw_text(self.game.screen, "Dungeon Warriors", TITLE_FONT, WHITE, HALF_WIDTH, 50)

        self.play_btn.draw(self.game.screen)
        self.options_btn.draw(self.game.screen)
        self.exit_btn.draw(self.game.screen)

    def update(self):
        super().update()

        self.play_btn.update()
        self.options_btn.update()
        self.exit_btn.update()

    def menu_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.show = False
                self.game.new_game()

    
    def play(self):
        self.game.new_game()

    
    def options(self):
        pass

    def exit(self):
        self.show_menu = False
        self.game.game_over = True
        pygame.quit()
        sys.exit()
