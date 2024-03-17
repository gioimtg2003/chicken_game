from pygame import mixer
import pygame
import json
from InputText import InputText

with open('setting.json') as f:
    data = json.load(f)

SCREEN_WIDTH = data['SCREEN_WIDTH']
SCREEN_HEIGHT = data['SCREEN_HEIGHT']
FPS = data['FPS']
BACKGROUND = data['BACKGROUND_COLOR']

pygame.init()

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Intro Screen")
INTRO_BACKGROUND = pygame.image.load(r'data\\images\\background_intro.jpg')
BUTTON = pygame.image.load(r'data\\images\\startButton.png')
FONT = pygame.font.Font(r"data\font\FreeSansBold.ttf", 32)
mixer.music.load(r"data\audio\Super Smash Bros. Melee Music_ Menu 1.mp3")
mixer.music.play(-1)
font = pygame.font.Font(None, 32)
ROUTE_INIT = ["intro", "login", "game", "setting"]

class Intro():
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.start = False
        self.exit = pygame.image.load(r'data\images\exit.png')
        self.exit_rect = self.exit.get_rect(x=SCREEN_WIDTH-90, y=10)
        self.route = "intro" #route handle to change screen
        
    def run(self):
        InputUser = InputText(100, 80, 200, 200, 32)
        
        while self.running:
            SCREEN.fill((255, 255, 255))
            if ROUTE_INIT[0] != "intro":
                self.running = False
                SCREEN.blit(pygame.transform.scale(INTRO_BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))
                
            SCREEN.blit(pygame.transform.scale(InputUser.surf, (200, 50)), InputUser.surf_rect);
            
            SCREEN.blit(pygame.transform.scale(BUTTON, (150, 100)), (SCREEN_WIDTH/2-75, SCREEN_HEIGHT - 150))
            SCREEN.blit(pygame.transform.scale(self.exit, (50, 50)), self.exit_rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    InputUser.hoverInput()
                    if self.is_mouse_over_button(pygame.mouse.get_pos(), pygame.Rect(SCREEN_WIDTH/2-75, SCREEN_HEIGHT/2 + 50, 150, 100)) or self.is_mouse_over_button(pygame.mouse.get_pos(), self.exit_rect):   
                        self.start = True
                        self.running = False
            
            
            pressed_keys = pygame.key.get_pressed()
            InputUser.update(pressed_keys)
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
        

if __name__ == "__main__":
    intro = Intro()
    start = intro.run()
    if start:
        print("Game Started")
    else:
        print("Game Stopped")
    intro.stop()
