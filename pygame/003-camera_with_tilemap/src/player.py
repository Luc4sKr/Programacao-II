import pygame

from .config import *
from .object import AnimatedObject

class Player(AnimatedObject):
    def __init__(self, animation, speed, image, pos: tuple, scale=1) -> None:
        super().__init__(animation, image, pos, scale)

        self.speed = speed
        self.speed_vector = pygame.math.Vector2()
        self.pos = pygame.math.Vector2()

        self.is_running = False
        self.invert_sprite = False

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.speed_vector = (0, -1)
            self.move()
        if keys[pygame.K_s]:
            self.speed_vector = (0, 1)
            self.move()

        if keys[pygame.K_d]:
            self.speed_vector = (1, 0)
            self.move()
        if keys[pygame.K_a]:
            self.speed_vector = (-1, 0)
            self.move()

        
        

    def move(self):
        self.is_running = False
        if self.pos.magnitude() != 0:
            self.is_running = True
        
        self.pos.x += self.speed_vector[0] * self.speed
        self.pos.y += self.speed_vector[1] * self.speed

        self.rect.center = self.pos
    
    def animation_control(self):
        self.animation.select(PLAYER_IDLE)
        if self.is_running:
            self.animation.select(PLAYER_RUN)

        self.image = self.animation.update_animation()
        self.image = pygame.transform.flip(self.image, self.invert_sprite, False)


    def update(self):
        self.input()
        self.animation_control()
