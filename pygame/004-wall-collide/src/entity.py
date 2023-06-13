import pygame

from .utils import *


class Entity(pygame.sprite.Sprite):
    def __init__(self, game, image_path, pos: tuple, speed, scale=1) -> None:
        super().__init__()

        self.game = game

        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale, self.image.get_height() * scale))

        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = speed
        self.dead = False

        self.direction = pygame.math.Vector2(0, 0)

        self.hitbox = get_mask_rect(self.image, *self.rect.topleft)

    def wall_collision(self):
        collide_points = (self.rect.midbottom, self.rect.bottomleft, self.rect.bottomright)
        for wall in self.game.map.wall_sprites:
            for point in collide_points:
                if wall.rect.collidepoint(point):
                    if self.direction.x > 0: # moving right
                        self.rect.right = wall.rect.left
                    if self.direction.x < 0: # moving left
                        self.rect.left = wall.rect.right
                    
                    if self.direction.y > 0: # moving down
                        self.rect.bottom = wall.rect.top
                    if self.direction.y < 0: # moving up
                        self.rect.bottom = wall.rect.bottom
            


class AnimatedEntity(Entity):
    def __init__(self, game, animation, image_path, pos: tuple, speed, scale=1) -> None:
        super().__init__(game, image_path, pos, speed, scale)

        self.animation = animation
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()