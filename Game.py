import pygame
from pygame import mixer

class Game:
    def __init__(self) -> None:
        self.Img=None
        self.x=0
        self.y=0
        self.x_change=0
        self.y_change=0
        
    def update(self, x, y):
        self.x=x
        self.y=y

class Player(Game):
    def __init__(self) -> None:
        super().__init__()
        self.Img= pygame.image.load(r"data\images\spaceship_6 (1).png")
        self.x=370
        self.y=500
        self.x_change=0
        self.y_change=0
        
    def update(self, x, y):
        super().update(x, y)
        screen.blit(self.Img,(self.x,self.y))
        
class Enemy(Game):
    def __init__(self) -> None:
        super().__init__()
        self.Img= pygame.image.load(r"data\images\BigChickenCI4_2.png")
        self.x=370
        self.y=5
        self.x_change=1
        self.y_change=60
        self.sound=mixer.Sound(r"data\audio\Chicken_sound.mp3")
        
    def update(self, x, y) :
        super().update(x, y)
        screen.blit(self.Img,(self.x,self.y))