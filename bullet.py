import pygame
import config

class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, direction):
        super().__init__()
        self.image = pygame.image.load("images/bullet.png")  # A simple bullet represented by a small rectangle
        self.rect = self.image.get_rect(center=position)
        self.speed = 10 if direction == 'right' else -10

    def update(self):
        self.rect.x += self.speed  # Move the bullet
        # Remove the bullet if it goes off-screen
        if self.rect.right < 0 or self.rect.left > config.SCREEN_WIDTH:
            self.kill()

