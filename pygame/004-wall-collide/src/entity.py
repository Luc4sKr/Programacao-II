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

        self.hitbox = get_mask_rect(self.image, *self.rect.topleft)

    def wall_collision(self):
        #self.hitbox = get_mask_rect(self.image, *self.rect.topleft)
        #self.hitbox.midbottom = self.rect.midbottom

        #test_rect = self.hitbox.move(*(self.speed, self.speed))  # Position after moving, change name later
        collide_points = (self.rect.midbottom, self.rect.bottomleft, self.rect.bottomright)
        for wall in self.game.map.wall_sprites:
            for point in collide_points:
                if wall.rect.collidepoint(point):
                    self.pos.x = point[0]
                    self.pos.y = point[1] - 30
            

        #print(f"{self.rect.center}, {self.hitbox.center}")


class AnimatedEntity(Entity):
    def __init__(self, game, animation, image_path, pos: tuple, speed, scale=1) -> None:
        super().__init__(game, image_path, pos, speed, scale)

        self.animation = animation
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()