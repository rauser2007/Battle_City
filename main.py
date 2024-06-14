import pygame
from gamesprites import *

WIDTH = 1300
HEIGHT = 800
FPS = 60 

class Game: 
    def __init__(self, background_filename:str = None):
        self.window = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()
        if background_filename:
            self.background = pygame.transform.scale(
                                pygame.image.load(background_filename), 
                                (WIDTH,HEIGHT)
                                )
        
        
        
    def create_player(self,coords, size):
        self.player = Player("player.png", coords, size)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.player.draw(self.window)
            
            pygame.display.flip()
            self.clock.tick(FPS)

game = Game()
game.create_player((WIDTH//2, HEIGHT//2), (50,50))
game.run()