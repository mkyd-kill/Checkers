import pygame
# Global Variables
WIDTH = 800
HEIGHT = 800
ROWS = 8
COLS = 8
SQUARE_SIZE = WIDTH//COLS
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE= (0, 0, 255)
GREY = (128, 128, 128)
GREEN = (0, 255, 0)
width = 800
height = 800
play_width = 800
play_height = 800
topleft_x = (width - play_width) // 2
topleft_y = height - play_height
CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'),(44, 25))