import pygame

# Game
FPS = 60

# background
BACKGROUND_IMAGE = "images/bg3.png"
BACKGROUND_MUSIC = "images/chat_melobytes.mp3"
MUSIC_GAME_OVER = "images/musice_game_over.wav"

# Screen dimensions
SCREEN_WIDTH = 1536
SCREEN_HEIGHT = 878

# Control Game
KEY_QUIT_GAME = pygame.K_ESCAPE

# Control Player
KEY_MOVE_LEFT = pygame.K_a
KEY_MOVE_RIGHT = pygame.K_d
KEY_MOVE_JUMP = pygame.K_w
KEY_SHOOT = pygame.K_SPACE


# Bullets
BULLTE_POSITION_ADJUST_RIGHT = (100, 20)
BULLTE_POSITION_ADJUST_LEFT = (-100, 20)

# Player
PLAYER_TOTAL_LIFVES = 3
PLAYER_SPEED_X = 30
SHOOT_MUSIC = "images/shoot_sound.wav"

# Enemy Configs
ENEMY_CONFIG_ADD_INTERVAL = 1000
KILLED_SOUND = "images/sound_kill_enemy.wav"

ENEMY_TYPY_ONE = 1
ENEMY_TYPY_TWO = 2
ENEMY_TYPY_THREE = 3

ENMEY_IMAGES = {
    ENEMY_TYPY_ONE : "images/spider.png",
    ENEMY_TYPY_TWO : "images/enemy_2_dinosaur.png",
    ENEMY_TYPY_THREE : "images/enemy_3_frog.png",
}





