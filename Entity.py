import pygame
import json
import random
from pygame.locals import (
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    RLEACCEL,
)

with open('setting.json') as f:
    data = json.load(f)

SCREEN_WIDTH = data['SCREEN_WIDTH']
SCREEN_HEIGHT = data['SCREEN_HEIGHT']

class Player(pygame.sprite.Sprite):
    
    def __init__(self, width, height):
        super(Player, self).__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load(r"data\\images\\space_action1.png"))
        self.sprites.append(pygame.image.load(r"data\\images\\space_action1.png"))
        self.sprites.append(pygame.image.load(r"data\\images\\space_action1.png"))
        self.sprites.append(pygame.image.load(r"data\\images\\space_action1.png"))
        self.sprites.append(pygame.image.load(r"data\\images\\space_action2.png"))
        self.sprites.append(pygame.image.load(r"data\\images\\space_action2.png"))
        self.sprites.append(pygame.image.load(r"data\\images\\space_action2.png"))
        self.sprites.append(pygame.image.load(r"data\\images\\space_action2.png"))
        self.sprites.append(pygame.image.load(r"data\\images\\space_action3.png"))
        self.sprites.append(pygame.image.load(r"data\\images\\space_action4.png"))
        self.sprites.append(pygame.image.load(r"data\\images\\space_action4.png"))
        self.sprites.append(pygame.image.load(r"data\\images\\space_action4.png"))
        self.sprites.append(pygame.image.load(r"data\\images\\space_action4.png"))
        self.sprites.append(pygame.image.load(r"data\\images\\space_action5.png"))
        self.sprites.append(pygame.image.load(r"data\\images\\space_action6.png"))
        self.sprites.append(pygame.image.load(r"data\\images\\space_action6.png"))
        self.sprites.append(pygame.image.load(r"data\\images\\space_action6.png"))
        self.sprites.append(pygame.image.load(r"data\\images\\space_action6.png"))
        self.sprites.append(pygame.image.load(r"data\\images\\space_action7.png"))
        self.sprites.append(pygame.image.load(r"data\\images\\space_action7.png"))
        self.sprites.append(pygame.image.load(r"data\\images\\space_action7.png"))
        self.sprites.append(pygame.image.load(r"data\\images\\space_action8.png"))
        self.sprites.append(pygame.image.load(r"data\\images\\space_action8.png"))
        self.sprites.append(pygame.image.load(r"data\\images\\space_action8.png"))
        self.sprites.append(pygame.image.load(r"data\\images\\space_action8.png"))
        self.current_sprite = 0
        self.surf = self.sprites[self.current_sprite]
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center = (width / 2, height - 25))
        self.speed = 8
        self.width = width
        self.height = height
    
    def updateAnimation(self):
        self.current_sprite += 1
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.surf = self.sprites[self.current_sprite]
        self.rect = self.surf.get_rect(center = (self.rect.centerx, self.rect.centery))
    
    def update(self, pressed_keys):
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.width:
            self.rect.right = self.width


class Enemy(pygame.sprite.Sprite):
    
    def __init__(self, width, height):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load(r"data\\images\\BigChickenCI4_2.png")
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center = (
                random.randint(10, width - 10),
                random.randint(30, 45)))
        self.speed = random.randint(5, 10)
        self.width = width
        self.height = height
    
    def update(self):
        if self.rect.right >= self.width :
            self.speed = -self.speed
            self.rect.move_ip(0, random.randint(10, 20))
            print("right")
            
        if self.rect.left <= 0:
            self.speed = abs(self.speed)
            self.rect.move_ip(0, random.randint(10, 20))
            print("left")
        self.rect.move_ip(self.speed, 0)

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, width, height, x, y):
        super(Bullet, self).__init__()
        self.surf = pygame.image.load(r"data\\images\\IonBlasterSingle.png")
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center = (x, y))
        self.speed = 6
        self.width = width
        self.height = height
    
    def update(self):
        self.rect.move_ip(0, -self.speed)
        if self.rect.bottom <= 0:
            self.kill()
        
            
            
        