import pygame
from abc import ABC, abstractmethod

class GameSprite(pygame.sprite.Sprite, ABC):
    def __init__(self, image_filename: str, coords, size):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load(image_filename),
            size)
        self.rect = self.image.get_rect(center=coords)
      
    def draw(self, window: pygame.Surface):
        window.blit(self.image, self.rect)
    
    @abstractmethod
    def update(self):
        raise NotImplementedError

class Player(GameSprite):
    def __init__(self, image_filename: str, coords, size):
        super().__init__(image_filename, coords, size)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed

class Enemy(GameSprite):
    def __init__(self, image_filename: str, coords, size):
        super().__init__(image_filename, coords, size)
        self.speed = 3

    def update(self):
        pass  # Logic for enemy movement and behavior

class Wall(GameSprite):
    def __init__(self, image_filename: str, coords, size):
        super().__init__(image_filename, coords, size)

    def update(self):
        pass  # Walls are static objects

class Bullet(GameSprite):
    def __init__(self, image_filename: str, coords, size, direction):
        super().__init__(image_filename, coords, size)
        self.direction = direction
        self.speed = 10

    def update(self):
        if self.direction == "up":
            self.rect.y -= self.speed
        elif self.direction == "down":
            self.rect.y += self.speed
        elif self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction == "right":
            self.rect.x += self.speed