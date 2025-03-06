import pygame
import random
from core.config import Config
from entities.player import Player

pygame.init()

#Configuration
config = Config()
WIDTH, HEIGHT = config.get('WIDTH'), config.get('HEIGHT')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader")

#Jugador
player = Player(WIDTH//2, HEIGHT -80)

#