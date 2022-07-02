import pygame
from pygame import mixer
import os
from pathlib import Path
DIR = Path(__file__).resolve().parent
DIRROOT = DIR.resolve().parent

FPS = 60

pygame.init()

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Battle")

 # Load images
RED_SPACE_SHIP = pygame.transform.scale(pygame.image.load(os.path.join("assets", "empireship.png")), (40,40))
GREEN_SPACE_SHIP = pygame.transform.scale(pygame.image.load(os.path.join("assets", "empireship.png")), (40,40))
BLUE_SPACE_SHIP = pygame.transform.scale(pygame.image.load(os.path.join("assets", "empireship.png")), (40,40))

# Player player
YELLOW_SPACE_SHIP = pygame.transform.scale(pygame.image.load(os.path.join("assets", "mainship.png")), (40,50))

# Lasers
RED_LASER = pygame.transform.scale(pygame.image.load(os.path.join("assets", "pixel_laser_red.png")), (40,40))
GREEN_LASER = pygame.transform.scale(pygame.image.load(os.path.join("assets", "pixel_laser_green.png")), (40,40))
BLUE_LASER = pygame.transform.scale(pygame.image.load(os.path.join("assets", "pixel_laser_red.png")), (40,40))

# Misil
Misil = pygame.transform.scale(pygame.image.load(os.path.join("assets", "pixel_laser_blue.png")), (40,40))

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

#Colors
White = (255,255,255)
Red = (128,0,0)


# Background Sound
mixer.music.load(os.path.join("assets", "imperial_march.wav"))
mixer.music.play(-1)
