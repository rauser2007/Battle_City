import pygame
from abc import ABC, abstractmethod

class GameSprite(pygame.sprite.Sprite, ABC):
    def __init__(self, image_filename: str, coords, size):
        self.image =   pygame.transform.scale(
                        pygame.image.load(image_filename),
                        size) 
        self.rect = self.image.get_rect(center=coords)
      
    def draw(self, window:pygame.Surface):
        window.blit(self.image, self.rect)
    
    @abstractmethod
    def update(self):
        raise NotImplementedError
    
class Player(GameSprite):
    def __init__(self, image_filename: str, coords, size):
        super().__init__(image_filename, coords, size)
        self.__speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= self.__speed

    


class Enemy(GameSprite):
    pass

class Wall(GameSprite):
    pass

class Bullet(GameSprite):
    pass