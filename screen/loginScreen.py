import pygame
from components.InputText import InputText
from components.TextView import TextView
from components.Button import Button
from components.Icon import Icon
from screen.SignUpScreen import SignUpScreen
from screen.IntroScreen import IntroScreen
import json
import requests
from SingletonClass import State
class LoginScreen():
    
    def __init__(self, screen, width, height, stop):
        self.running = True
        self.clock = pygame.time.Clock()
        self.BackGround = pygame.image.load(r'data\\images\\login_background.jpg')
        self.route = "login"
        self.width = width
        self.height = height
        self.stop = stop
        self.screen = screen
        self.request = requests.session()
        
    def run(self):
        
        InputUser = InputText(self.width / 2, 180, 32, "text")
        InputPassword = InputText(self.width / 2, self.height / 2, 32, "password")
        BtnLogin = Button(self.width / 2, self.height / 2 + 200, r'data\\components\\BtnLogin.png', r'data\\components\\btnLoginHover.png')
        IconPassword = Icon(self.width / 2 - 200, self.height / 2, r'data\\components\\Password_icon.png')
        UserIcon = Icon(self.width / 2 - 200, 180, r'data\\components\\user_icon.png')
        SignUpIcon = Icon(self.width - 64, 64, r'data\\images\\sign-up.png')
        while self.running:
            self.screen.blit(self.BackGround, (0, 0))
            self.screen.blit(BtnLogin.surf, BtnLogin.surf_rect)
            self.screen.blit(InputUser.surf, InputUser.surf_rect)
            self.screen.blit(InputPassword.surf, InputPassword.surf_rect)
            self.screen.blit(IconPassword.surf, IconPassword.surf_rect)
            self.screen.blit(UserIcon.surf, UserIcon.surf_rect)
            self.screen.blit(SignUpIcon.surf, SignUpIcon.surf_rect)
            
            for event in pygame.event.get():
                loginFunc = lambda : self.handleLogin(InputUser.getValue(), InputPassword.getValue())
                BtnLogin.onClick(event, loginFunc)  
                InputUser.handleInput(event)
                InputPassword.handleInput(event)
                SignUpIcon.onClick(event, self.onClickSignUp)
                if event.type == pygame.QUIT:
                    self.stop()
                
                
            
            pygame.display.flip()
            self.clock.tick(60)
            
        return self.running
            
    def stopScreen(self):
        self.running = False
    
    def onClickSignUp(self):
        signUpScreen = SignUpScreen(self.screen, self.width, self.height, self.stop)
        signUpScreen.run()
        
    def handleLogin(self, user, password):
        login = self.request.post("http://localhost:3000/api/auth/login", data={"email": user, "password": password})
        print(login.json())
        if login.json()["code"] == 200:
            # self.stopScreen()
            introScreen = IntroScreen(self.screen, self.width, self.height, self.stop)
            state = State()
            state.user = login.json()
            return introScreen.run()
               
            
            

        
        
