import pygame
from pygame import mixer
import json
import requests
from SingletonClass import State
from Entity import Player, Enemy, Bullet
import random

class GameScreen():
    
    def __init__(self, screen, width, height, stop):
        self.running = True
        self.clock = pygame.time.Clock()
        self.BackGround = pygame.image.load(r'data\\images\\chicken_invaders_2.png')
        self.route = "login"
        self.width = width
        self.height = height
        self.stop = stop
        self.screen = screen
        self.request = requests.session()
        self.addEnemy = pygame.USEREVENT + 1
        pygame.time.set_timer(self.addEnemy, random.randint(1000, 3000))
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        
    def run(self):
        
        player = Player(self.width, self.height)
        state = State()
        print(state.user)
        while self.running:
            self.screen.blit(self.BackGround, (0, 0))
            self.screen.blit(player.surf, player.rect)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()
                if event.type == self.addEnemy:
                    new_enemy = Enemy(self.width, self.height)
                    self.enemies.add(new_enemy)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.fireBullet(player)
                    
            for entity in self.enemies:
                self.screen.blit(entity.surf, entity.rect)
                
            for bullet in self.bullets:
                self.screen.blit(bullet.surf, bullet.rect)
                bullet.update()
                if pygame.sprite.spritecollideany(bullet, self.enemies):
                    mixer.Sound(r'data\\audio\\Chicken_sound.mp3').play()
                    self.enemies.remove(pygame.sprite.spritecollideany(bullet, self.enemies))
                    bullet.kill()
                
            self.enemies.update()
            pressed_keys = pygame.key.get_pressed()
            player.update(pressed_keys)
            
            pygame.display.flip()
            self.clock.tick(60)
            
        return self.running
            
    def stopScreen(self):
        self.running = False
    
    def onGoBackLoginScreen(self):
        self.running = False
        self.sound.stop()
    
    def fireBullet(self, player):
        new_bullet = Bullet(self.width, self.height, player.rect.centerx, player.rect.y - 25)  # Tạo viên đạn mới
        self.bullets.add(new_bullet)
        mixer.Sound(r'data\\audio\\IonBlasterSingle_Sound.mp3').play()

        
        
