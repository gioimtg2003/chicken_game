import pygame
import random
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    RLEACCEL,
)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True
 
class Player(pygame.sprite.Sprite):
    def __init__ (self):
        super(Player, self).__init__()
        self.surf = pygame.image.load(r"data\images\spaceship_6 (1).png")
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center = (0, 0))
        self.speed = 8
    
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -self.speed)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, self.speed)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__ (self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load(r"data\images\IonBlasterSingle.png")
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center = (
                random.randint(SCREEN_WIDTH + 40, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),))
        self.speed = random.randint(5, 20)
        
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

player = Player()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
ADDENEMY  = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
clock = pygame.time.Clock()

while running:
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
        elif event.type == K_DOWN:
            if event.key == K_ESCAPE:
                running = False
        
        elif event.type == ADDENEMY:
            new = Enemy()
            enemies.add(new)
            all_sprites.add(new)
            
    screen.fill((255, 255, 255))
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        running = False
        
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    pygame.display.flip()
    
    enemies.update()
pygame.quit()