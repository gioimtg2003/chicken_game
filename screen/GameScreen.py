import pygame
from pygame import mixer
import json
import requests
from SingletonClass import State
from Entity import Player, Enemy, Bullet
import random
from components.Icon import Icon
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
        pygame.time.set_timer(self.addEnemy, random.randint(800, 2500))
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.score = 0
        self.player = Player(self.width, self.height)

        
    def run(self):
        
        textScoreFont = pygame.font.Font(r"data\font\FreeSansBold.ttf", 28)
        ResetIcon = Icon(self.width - 64, 32, r'data\\components\\reset.png')
        ResetText = textScoreFont.render("R: reload", True, (255, 244, 85))
        state = State()
        print(state.user)
        while self.running:
            self.screen.blit(self.BackGround, (0, 0))
            self.screen.blit(self.player.surf, self.player.rect)
            textScore = textScoreFont.render("Score: " + str(self.score), True, (255, 244, 85))
            self.screen.blit(textScore, textScore.get_rect(topleft=(48, 15)))
            self.screen.blit(ResetIcon.surf, ResetIcon.surf_rect)
            self.screen.blit(ResetText, ResetText.get_rect(topleft=(self.width - 64 * 3.5, 16)))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()
                if event.type == self.addEnemy:
                    new_enemy = Enemy(self.width, self.height)
                    if self.score >= 5: # level 2
                        new_enemy.speed = random.randint(7, 12)
                    elif self.score >= 10: # level 3
                        new_enemy.speed = random.randint(10, 15)
                    elif self.score >= 15: # level 4
                        new_enemy.speed = random.randint(12, 17)
                    elif self.score >= 20: # level 5
                        new_enemy.speed = random.randint(15, 20)
                    if len(self.enemies) <= 10:
                        self.enemies.add(new_enemy)
                        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.fireBullet()
                    if event.key == pygame.K_r:
                        self.reloadGame()
                    
            for entity in self.enemies:
                
                self.screen.blit(entity.surf, entity.rect)
                if pygame.sprite.spritecollideany(self.player, self.enemies):
                    mixer.music.pause()
                    mixer.Sound(r'data\\audio\\Linda.mp3').play()
                    print("Game Over")
                
            for bullet in self.bullets:
                self.screen.blit(bullet.surf, bullet.rect)
                bullet.update()
                if pygame.sprite.spritecollideany(bullet, self.enemies):
                    mixer.Sound(r'data\\audio\\Chicken_sound.mp3').play()
                    self.enemies.remove(pygame.sprite.spritecollideany(bullet, self.enemies))
                    bullet.kill()
                    self.score += 1
                
            self.enemies.update()
            pressed_keys = pygame.key.get_pressed()
            self.player.update(pressed_keys)
            self.player.updateAnimation()
            pygame.display.flip()
            self.clock.tick(60)
            
        return self.running
            
    def stopScreen(self):
        self.running = False
    
    def onGoBackLoginScreen(self):
        self.running = False
        self.sound.stop()
    
    def fireBullet(self):
        new_bullet = Bullet(self.width, self.height, self.player.rect.centerx, self.player.rect.y - 25)
        if len(self.bullets) <= 1:
            self.bullets.add(new_bullet)
        mixer.Sound(r'data\\audio\\IonBlasterSingle_Sound.mp3').play()
        
    def reloadGame(self):
        self.bullets.empty()
        self.enemies.empty()
        self.score = 0

        
        
