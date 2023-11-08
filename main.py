import pygame
import random

import config
import player as player_lib
import enemy as enemy_lib

def draw_object(screen, obj):
    obj.draw(screen)

def game_over(screen, running):

    if not running:

        # Render the "Game Over" message
        game_over_text = pygame.font.SysFont(None, 100).render('Game Over', True, (255, 0, 0))
        text_rect = game_over_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2))
        screen.blit(game_over_text, text_rect)
        
        # Update the full display surface to the screen
        pygame.display.flip()
        
        # Optionally, wait for a while or until a player input before closing or restarting
        pygame.time.wait(3000)  

def main():

    # Initialize Pygame
    pygame.init()
    pygame.mixer.init()

    game_music = pygame.mixer.Sound(config.BACKGROUND_MUSIC)
    game_music.play(-1)
    
    game_over_music = pygame.mixer.Sound(config.MUSIC_GAME_OVER)

    # Set up the display
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    pygame.display.set_caption("Simple 2D Shooter")

    # Load images
    background_image = pygame.image.load(config.BACKGROUND_IMAGE)  # Make sure to provide the correct path to your images
    # Scale images to your desired size
    background_image = pygame.transform.scale(background_image, (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

    enemies = pygame.sprite.Group()
    player = player_lib.Player()

    clock = pygame.time.Clock()

    running = True
    # Main game loop
    while running:

        # Check for events

        for event in pygame.event.get():

            # quit game
            if event.type == pygame.QUIT:
                running = False

            # press key
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()

                # Player movement
                if keys[config.KEY_MOVE_LEFT]:
                    player.move_left()
                if keys[config.KEY_MOVE_RIGHT]:
                    player.move_right()
                if keys[config.KEY_MOVE_JUMP]:
                    player.jump()
                if keys[config.KEY_SHOOT]:
                    player.shoot()
                if keys[config.KEY_QUIT_GAME]:
                   running = False
            
            # add enemy
            if event.type == enemy_lib.ADDENEMY:
                enemy_lib.add_enemy(enemies)

        # Draw the background
        screen.blit(background_image, (0, 0))

        # update player    
        player.update()

        # update and draw enemies
        for enemy in enemies:
            enemy.update()
            draw_object(screen, enemy)

            # Draw the player
        draw_object(screen, player)

        # Inside your game loop, where you update all sprites
        hits = pygame.sprite.groupcollide(enemies, player.get_bullets(), False, True)
        for hit in hits:
            score_value = hit.take_damage()
            player.score += score_value  # Assuming you have a player.score attribute

        hits = pygame.sprite.spritecollide(player, enemies, True)
        if hits:
            player.reduce_life()
            if player.get_life() <= 0:
                running = False

        # Display the score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render("Score: {}".format(player.get_score()), True, (255, 255, 255))
        screen.blit(score_text, (config.SCREEN_WIDTH - 150, 10))

        # Display the lives
        lives_text = font.render("Lives: {}".format(player.get_life()), True, (255, 255, 255))
        screen.blit(lives_text, (10, 10))

        # Refresh screen
        pygame.display.flip()

        # Frame rate
        clock.tick(config.FPS)

    if not running:
        game_music.stop()
        game_over_music.play(-1)
        game_over(screen, running) 

    # Quit the game
    pygame.quit()



if __name__ == "__main__":
    main()
