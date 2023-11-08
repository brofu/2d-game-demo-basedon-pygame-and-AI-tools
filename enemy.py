import random
import pygame
import config

pygame.init()
pygame.mixer.init()

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, config.ENEMY_CONFIG_ADD_INTERVAL)  # Adjust the time to your needs


def add_enemy(enemies):
        enemy_type = random.randint(config.ENEMY_TYPY_ONE, config.ENEMY_TYPY_THREE)
        enemy_position = (random.randrange(0, config.SCREEN_WIDTH), random.randrange(0, config.SCREEN_HEIGHT))  # Random y position
        new_enemy = Enemy(enemy_type, enemy_position)
        enemies.add(new_enemy)

class Enemy(pygame.sprite.Sprite):
    def __init__(self,  enemy_type, position):
        super().__init__()
        self.__kill_sound = pygame.mixer.Sound(config.KILLED_SOUND)
        self.image = pygame.image.load(config.ENMEY_IMAGES[enemy_type]).convert_alpha()
        self.rect = self.image.get_rect(center=position)
        self.type = enemy_type
        self.health = enemy_type  # Where type is also the health/hits it can take

        self.gravity = 0.5  # You can adjust this value as needed
        self.vertical_velocity = 0

    def update(self):

        # Apply gravity
        self.vertical_velocity += self.gravity
        self.rect.y += self.vertical_velocity

        # Check if the enemy has reached the ground level
        ground_level = config.SCREEN_HEIGHT # Replace with the actual ground height
        if self.rect.bottom >= ground_level:
            self.rect.bottom = ground_level
            self.vertical_velocity = 0  # Stop falling once on the ground

        # move the enemy horizontally
        self.rect.x -= 2  # Example movement speed, you can change this as needed
        if self.rect.right < 0:
            self.kill()  # Remove the enemy when it goes off-screen

    def take_damage(self):
        self.health -= 1
        if self.health <= 0:
            self.__kill_sound.play()
            self.kill()
            return self.type  # Return the score value
        return 0

    def draw(self, screen):
        screen.blit(self.image, [self.rect.x, self.rect.y])


