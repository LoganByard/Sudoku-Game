import pygame

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
LIGHT_BLUE = (176, 224, 230)
BLUE = (135, 206, 235)
DARKER_BLUE = (100, 149, 237)
RED = (255, 0, 0)

# Initialize Pygame and create screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sudoku")