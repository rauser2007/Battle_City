import pygame
from gamesprites import *

WIDTH = 1300
HEIGHT = 800
FPS = 60

class Game:
    def __init__(self, background_filename: str = None):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        if background_filename:
            self.background = pygame.transform.scale(
                pygame.image.load(background_filename),
                (WIDTH, HEIGHT)
            )
        else:
            self.background = None

        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

    def create_player(self, coords, size):
        self.player = Player("player.png", coords, size)
        self.all_sprites.add(self.player)

    def create_enemy(self, coords, size):
        enemy = Enemy("enemy.png", coords, size)
        self.all_sprites.add(enemy)
        self.enemies.add(enemy)

    def create_wall(self, coords, size):
        wall = Wall("wall.png", coords, size)
        self.all_sprites.add(wall)
        self.walls.add(wall)

    def create_bullet(self, coords, direction):
        bullet = Bullet("bullet.png", coords, (10, 10), direction)
        self.all_sprites.add(bullet)
        self.bullets.add(bullet)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.create_bullet(self.player.rect.center, "up")

    def check_collisions(self):
        pygame.sprite.groupcollide(self.bullets, self.walls, True, False)
        hits = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)
        if hits:
            print("Enemy hit!")

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.handle_input()
            self.all_sprites.update()
            self.check_collisions()

            if self.background:
                self.window.blit(self.background, (0, 0))
            else:
                self.window.fill((0, 0, 0))

            self.all_sprites.draw(self.window)

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()

if __name__ == "__main__":
    game = Game("background.png")
    game.create_player((WIDTH // 2, HEIGHT // 2), (50, 50))
    game.create_enemy((WIDTH // 4, HEIGHT // 4), (50, 50))
    game.create_wall((WIDTH // 2, HEIGHT // 4), (50, 50))
    game.run()