from pygame import mixer
from pygame.transform import  scale
import pygame
import json
from components.InputText import InputText
from components.TextView import TextView
from screen.loginScreen import LoginScreen
from screen.IntroScreen import IntroScreen
with open('setting.json') as f:
    data = json.load(f)

SCREEN_WIDTH = data['SCREEN_WIDTH']
SCREEN_HEIGHT = data['SCREEN_HEIGHT']
FPS = data['FPS']
BACKGROUND = data['BACKGROUND_COLOR']

pygame.init()


pygame.display.set_caption("Intro Screen")
INTRO_BACKGROUND = pygame.image.load(r'data\\images\\background_intro.jpg')
BUTTON = pygame.image.load(r'data\\images\\startButton.png')
FONT = pygame.font.Font(r"data\font\FreeSansBold.ttf", 32)
# mixer.music.load(r"data\audio\Super Smash Bros. Melee Music_ Menu 1.mp3")
# mixer.music.play(-1)
font = pygame.font.Font(None, 32)
ROUTE_INIT = ["intro", "login", "game", "setting"]
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
class MainScreen():
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.start = False
        self.exit = pygame.image.load(r'data\images\exit.png')
        self.exit_rect = self.exit.get_rect(x=SCREEN_WIDTH-90, y=10)
        mixer.music.load(r'data\\audio\\LolSound.mp3')
        mixer.music.play(-1)
        
    def run(self):
        loginScreen = LoginScreen(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, stop=self.stop)
        introScreen = IntroScreen(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, self.stop)
            
        while self.running:
            introScreen.run()
            # if not loginScreen.run():
            #     SCREEN.fill(BACKGROUND)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.stop()
            SCREEN.fill(BACKGROUND)
            pygame.display.flip()
            self.clock.tick(FPS)
        return self.start
    
    
    
    def stop(self):
        self.running = False
        mixer.music.stop()
        pygame.quit()
        quit()
        
    def is_mouse_over_button(self, mouse_pos, button_rect):
        return button_rect.collidepoint(mouse_pos)
        

