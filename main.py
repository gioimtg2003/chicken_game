import pygame
import os
import random
import time
import math
from pygame import mixer
import tkinter as tk
from tkinter import messagebox
"___________________________________________"

"1_Creating Our First Game Window"
pygame.init()
screen=pygame.display.set_mode((800, 600))    #(x,y)
"2_Chagging title, Logo, Backgound color"
pygame.display.set_caption("Chicken Invader Z")
"9_Adding a Background Image"
intro_image = pygame.image.load(r"data\\images\\background_intro.jpg")
background=pygame.image.load(r"data\images\chicken_invaders_2.png")
#Score
"Add font for pygame"
font=pygame.font.Font(r"data\font\FreeSansBold.ttf", 32)
#Game over text
over_font=pygame.font.Font(r"data\font\FreeSansBold.ttf", 64)
"15_1_Adding Sounds and Background Music"
#Background sound
mixer.music.load(r"data\audio\Super Smash Bros. Melee Music_ Menu 1.mp3")
mixer.music.play(-1)

"16_Game over"
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
        
"3_Adding images into Our Space Invader Game"
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
        
"7_Creating the Enemy"
class Enemy(Game):
    def __init__(self) -> None:
        super().__init__()
        self.Img= pygame.image.load(r"data\images\BigChickenCI4_2.png")
        self.x=370
        self.y=5
        self.x_change=1
        self.y_change=60
        self.sound=mixer.Sound(r"data\audio\Chicken_sound.mp3")
    def update(self, x, y):
        super().update(x, y)
        screen.blit(self.Img,(self.x,self.y))
        
"10_1 Creating Bullets for Shooting"
class Bullet(Game):
    def __init__(self) -> None:
        super().__init__()
        self.Img= pygame.image.load(r"data\images\IonBlasterSingle.png")
        self.x=370
        self.y=500
        self.y_change=3
        self.state="ready"
        self.sound=mixer.Sound(r"data\audio\IonBlasterSingle_Sound.mp3")
    def update(self, x, y):
        super().update(x, y)
        #Ready - You can't see the bullet on the screen
        #Fire - The bullet is currently moving
        self.state="fire"
        screen.blit(self.Img,(self.x+15,self.y-50))
        
"14_1 Adding Text and Displaying Score"
class Score(Game):
    def __init__(self) -> None:
        super().__init__()
        self.value=0
        self.x=10
        self.y=10
    def update(self, x, y):
        self.Img=font.render("Score : "+str(self.value),True, (255,255,255))
        screen.blit(self.Img,(self.x+15,self.y-10))
        
class Restart(Game):
    def __init__(self) -> None:
        super().__init__()
        self.value=0
        self.x=600
        self.y=0
    def update(self, x, y):
        self.Img=font.render("R: RESTART",True, (255,255,255))
        screen.blit(self.Img,(self.x,self.y+6))
        
class Game_over(Game):
    def __init__(self) -> None:
        super().__init__()
        self.value=0
        self.x=290
        self.y=250
        self.sound=mixer.Sound(r"data\audio\Linda.mp3")
    def update(self, x, y):
        self.Img=font.render("GAME OVER",True, (255,255,255))
        screen.blit(self.Img,(self.x+15,self.y-10))
        
# Define a new class for the gift box
class Game_win(Game):
    def __init__(self) -> None:
        super().__init__()
        self.Img1=font.render("GAME WIN",True, (255,255,255))
        self.Img2 = pygame.image.load(r"data\images\gift_box.png")
        self.sound=mixer.Sound(r"data\audio\Linda.mp3")
        self.x = 300
        self.y = 200
    def update(self):
        screen.blit(self.Img1, (self.x, self.y))
        screen.blit(self.Img2, (self.x+50, self.y+50))
        
"12_Collision Detection"
def is_Collision(bulletX, bulletY, enemyX, enemyY):
    #"formula for calculating the distance between two coordinate points"
    distance=math.sqrt( pow((bulletX-enemyX),2)+pow((bulletY-enemyY),2) )
    if distance<26:
        return True
    return False

def game_intro():
    global intro_image
    intro = True
    exit=True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.QUIT:
                intro = False
            if event.type == pygame.QUIT:
                exit = False
        # Display the game interface
        screen.fill((0, 30, 0))
        screen.blit(pygame.transform.scale(intro_image, (800, 600)), (0, 0))
        start_button_image = pygame.image.load(r"data\images\startButton.png")
        screen.blit(pygame.transform.scale(start_button_image, (150,100)), (330, 390))
        # intro_text = over_font.render("Chicken Invader Z", True, (255, 255, 255))
        # start_text = font.render("Press any key or click to start", True, (255, 255, 255))
        # screen.blit(intro_text, (150, 250))
        # screen.blit(start_text, (200, 350))
        pygame.display.update()
    return exit

def game_loop():
    player=Player()
    bullet=Bullet()
    score=Score()
    restart=Restart()
    game_over=Game_over()
    game_win = Game_win()
    global quit
    "13_1 Creating multiple enemies"
    enemy=[]
    num_of_enemies=6
    for i in range(num_of_enemies):
        e=Enemy()
        e.x=random.randint(0,736)
        e.y=random.randint(5, 69)
        enemy.append(e)
    game_won=False
    running=True
    while running:
        #Add RGB
        screen.fill((0,30,0))
        #background Image
        screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                return running
            "5_Ketboard Input Controls & Key Pressed Event"
            
            #print("Keystroke is press")
            if event.type == pygame.KEYDOWN:
                #print("Left arrow is pressed")
                if event.key==pygame.K_r:
                    return True
                
                #print("Left arrow is pressed")
                if event.key==pygame.K_LEFT:
                    player.x_change=-1
                    
                #print("Right arrow is pressed")
                if event.key==pygame.K_RIGHT: 
                    player.x_change=1
                    
                "10.2 Creating Bullets for Shooting"
                if event.key==pygame.K_SPACE:
                    "15_Adding Sounds and Background Music"
                    bullet.sound.play()
                    "11_2 shooting Multiple Bullets at Space Invaders"
                    if bullet.state=="ready":
                        bullet.update(player.x, player.y)
                        
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:#print("Keystroke has been released")
                    player.x_change=0
        "6_Adding Boundaries to Our Game"
        #Set movement of player
        player.x+=player.x_change
        if player.x<=0: player.x=0
        elif player.x>=736:  player.x=736
        "4_Movement mechanics in Game Development"
        if player.y<0: player.y=550
        "8_Movement Mechanics of the Enemy Space Invader"
        #Set movemt of enemy
        "13_2 Creating multiple enemies"
        for i in range(num_of_enemies):
            "16_Game over"
            if game_won==True: break
            if enemy[i].y>=450:
                mixer.music.pause()
                # pygame.mixer.pause()
                game_over.sound.play(-1)
                for j in range(num_of_enemies):
                    enemy[j].y=999#Select number > y
                game_over.update(game_over.x, game_over.y)
                break
            enemy[i].x+=enemy[i].x_change
            
            if enemy[i].x>=736:
                enemy[i].x_change=-0.4
                enemy[i].y+=enemy[i].y_change
                
            elif enemy[i].x<=0: 
                enemy[i].x_change=0.4
                enemy[i].y+=enemy[i].y_change
                
            if enemy[i].y>=536: enemy[i].y=100
            
            collision=is_Collision(bullet.x,bullet.y,enemy[i].x,enemy[i].y)
            if collision==True:
                enemy[i].sound.play()
                bullet.y=500
                bullet.state="ready"
                score.value+=1 #"14_2 Adding Text and Displaying Score"
                enemy[i].x=random.randint(0,736)
                enemy[i].y=random.randint(5, 6)
            enemy[i].update(enemy[i].x, enemy[i].y)
        #Set movent of bullet
        if bullet.state=="fire":
            bullet.update(bullet.x, bullet.y)
            bullet.y-=bullet.y_change
        "11_1 shooting Multiple Bullets at Space Invaders"
        if bullet.y<=0:
            bullet.y=500
            bullet.state="ready"
        player.update(player.x,player.y)
        score.update(score.x,score.y)
        restart.update(restart.x,restart.y)
        if score.value >= 40:
            # Stop the game loop
            game_won=True
            for j in range(num_of_enemies):
                enemy[j].y=999#Select number > y
            game_win.update()
        pygame.display.update()


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("300x150")

        self.label_username = tk.Label(root, text="Username")
        self.label_password = tk.Label(root, text="Password")

        self.entry_username = tk.Entry(root)
        self.entry_password = tk.Entry(root, show="*")

        self.label_username.grid(row=0, sticky=tk.E)
        self.label_password.grid(row=1, sticky=tk.E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "admin" and password == "admin":
            self.root.destroy()
            start_game()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
            
def redirect_to_current_directory():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)    
    
def start_game():
    redirect_to_current_directory()
    if  game_intro():
        Continue = True
        while Continue:
            Continue = game_loop()


if __name__ == "__main__":
    root = tk.Tk()
    login_window = LoginWindow(root)
    root.mainloop()
"15_Adding Sounds and Background Music"
"16_Game over"

