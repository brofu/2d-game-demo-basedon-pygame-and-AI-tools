import pygame
import bullet
import config

pygame.mixer.init()

def PrintReact(flag, react):
   print(flag, react.center, react.x, react.y, react.left, react.right, react.bottom) 

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.__shoot_sound = pygame.mixer.Sound(config.SHOOT_MUSIC)
        self.images = {
            "left": pygame.image.load('images/player1_left.png').convert_alpha(),
            "right": pygame.image.load('images/player1_right.png').convert_alpha(),
        }
        self.image = self.images["right"]
        self.rect = self.image.get_rect()
        self.size = self.image.get_size()
        self.rect.center = [config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT - self.size[1] // 2]

        self.speed_x = config.PLAYER_SPEED_X
        self.on_ground = True  # To check if the player is able to jump
        self.jump_speed = 10
        self.gravity = 0.5 
        self.speed_y = 0

        self.score = 0
        self.life = config.PLAYER_TOTAL_LIFVES

        self.bullets = pygame.sprite.Group()

    def move_left(self):
        self.image = self.images["left"]
        self.rect.x -= self.speed_x
        if self.rect.left < 0:
            self.rect.left = 0

    def move_right(self):
        self.image = self.images["right"]
        self.rect.x += self.speed_x
        if self.rect.right > config.SCREEN_WIDTH:
            self.rect.right = config.SCREEN_WIDTH

    def jump(self):
        # Only jump if on the ground
        if self.on_ground:
            self.speed_y -= self.jump_speed
            self.on_ground = False

    def update(self):

        # Update the player's position and apply gravity if jumping
        self.rect.y += self.speed_y

        if not self.on_ground:
            self.speed_y += self.gravity

            if self.rect.bottom >= config.SCREEN_HEIGHT:  # Assuming the bottom of the screen is the ground
                self.rect.bottom = config.SCREEN_HEIGHT
                self.on_ground = True
                self.speed_y = 0

        if self.life <= 0:
            self.kill()
        
        # update the bullets
        for bullet in self.bullets:
            bullet.update()

    def shoot(self):
        # The bullet will be spawned slightly ahead of the player's current direction
        bullet_position = self.__calculate_bullet_position()
        new_bullet = bullet.Bullet(bullet_position, 'right' if self.image == self.images['right'] else 'left')
        self.bullets.add(new_bullet)
        self.__play_shoot_music()

    def __play_shoot_music(self):
        self.__shoot_sound.play()

    def draw(self, screen):

        screen.blit(self.image, [self.rect.x, self.rect.y])
        for bullet in self.bullets:
            screen.blit(bullet.image, bullet.rect)

    def __calculate_bullet_position(self):
        adjust = config.BULLTE_POSITION_ADJUST_LEFT
        if self.image == self.images["right"]:
            adjust = config.BULLTE_POSITION_ADJUST_RIGHT
        bullet_position = (self.rect.centerx+adjust[0], self.rect.centery+adjust[1])
        return bullet_position

    def get_bullets(self):
        return self.bullets
    
    def add_score(self, score):
        self.score += score

    def get_score(self):
        return self.score

    def reduce_life(self):
        if self.life > 0:
            self.life -= 1

    def get_life(self):
        return self.life


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('path_to_bullet_image.png').convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 10

    def update(self):
        # Update the bullet's position
        self.rect.y -= self.speed
        # Kill the bullet if it moves off the screen
        if self.rect.bottom < 0:
            self.kill()

