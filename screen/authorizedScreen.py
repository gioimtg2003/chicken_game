from pygame import mixer
import pygame
import json

with open('setting.json') as f:
    data = json.load(f)

SCREEN_WIDTH = data['SCREEN_WIDTH']
SCREEN_HEIGHT = data['SCREEN_HEIGHT']
FPS = data['FPS']
BACKGROUND = data['BACKGROUND_COLOR']

pygame.init()

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Login")