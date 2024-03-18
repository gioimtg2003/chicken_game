import pygame
from pygame import mixer
from components.InputText import InputText
from components.TextView import TextView
from components.Button import Button
from components.Icon import Icon
from screen.GameScreen import GameScreen

import json
import requests
from SingletonClass import State

class IntroScreen():
    
    def __init__(self, screen, width, height, stop):
        self.running = True
        self.clock = pygame.time.Clock()
        self.BackGround = pygame.image.load(r'data\\images\\background_intro.jpg')
        self.route = "login"
        self.width = width
        self.height = height
        self.stop = stop
        self.screen = screen
        self.request = requests.session()
        self.sound = mixer.Sound(r'data\\audio\\Super Smash Bros. Melee Music_ Menu 1.mp3')
        mixer.music.pause()
        
    def run(self):
        HgihtScore = pygame.font.Font(r"data\font\FreeSansBold.ttf", 32).render("High Score: 0", True, (255, 244, 85))
        # HighScores = TextView("High Score: 0", 30, 20,  32, (255, 244, 85))
        btnStart = Button(self.width / 2, self.height / 2 + 200, r'data\\images\\startButton.png', r'data\\images\\startButtonHover.png')
        ExitIcon = Icon(self.width - 64, 32, r'data\\images\\exit.png')
        ScoreIcon = Icon(32, 32, r'data\\components\\Score_Iconpng.png')
        UserNameIcon = Icon(64 * (3/4), 84, r'data\\components\\usernameicon.png')
        UserName = pygame.font.Font(r"data\font\FreeSansBold.ttf", 32).render("Admin", True, (255, 244, 85))
        self.sound.play(-1)
        state = State()
        print(state.user)
        while self.running:
            self.screen.blit(self.BackGround, (0, 0))
            self.screen.blit(btnStart.surf, btnStart.surf_rect)
            self.screen.blit(ExitIcon.surf, ExitIcon.surf_rect)
            self.screen.blit(HgihtScore, HgihtScore.get_rect(topleft=(48, 15)))
            self.screen.blit(ScoreIcon.surf, ScoreIcon.surf_rect)
            self.screen.blit(UserNameIcon.surf, UserNameIcon.surf_rect)
            self.screen.blit(UserName, UserName.get_rect(topleft=(64 * (5/4), 64)))
            for event in pygame.event.get():
                btnStart.onClick(event, self.openGameScreen ) 
                ExitIcon.onClick(event, self.onGoBackLoginScreen)
                if event.type == pygame.QUIT:
                    self.stop()

            
            pygame.display.flip()
            self.clock.tick(60)
        print("out of loop intro screen")
        return self.running
            
    def stopScreen(self):
        self.running = False
    
    def onGoBackLoginScreen(self):
        self.running = False
        self.sound.stop()
        
    def openGameScreen(self):
        gameScreen = GameScreen(self.screen, self.width, self.height, self.stop)
        gameScreen.run()
        
        
