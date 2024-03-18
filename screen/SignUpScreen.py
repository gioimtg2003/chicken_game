import pygame
from components.InputText import InputText
from components.TextView import TextView
from components.Button import Button
from components.Icon import Icon
class SignUpScreen():
    
    def __init__(self, screen, width, height, stop):
        self.running = True
        self.clock = pygame.time.Clock()
        self.BackGround = pygame.image.load(r'data\\images\\login_background.jpg')
        self.route = "login"
        self.width = width
        self.height = height
        self.stop = stop
        self.screen = screen
        
    def run(self):
        InputUser = InputText(self.width / 2, 180, 32, "text")
        InputPassword = InputText(self.width / 2, self.height / 2, 32, "password")
        RePassword = InputText(self.width / 2, self.height / 2 + 100, 32, "password")
        BtnRegister = Button(self.width / 2, self.height / 2 + 200, r'data\\components\\btnRegister.png', r'data\\components\\btnRegisterHover.png')
        IconPassword = Icon(self.width / 2 - 200, self.height / 2, r'data\\components\\Password_icon.png')
        UserIcon = Icon(self.width / 2 - 200, 180, r'data\\components\\user_icon.png')
        RePasswordIcon = Icon(self.width / 2 - 200, self.height / 2 + 100, r'data\\components\\Password_icon.png')
        SignInIcon = Icon(64, 64, r'data\\images\\sign-in.png')
        
        while self.running:
            self.screen.blit(self.BackGround, (0, 0))
            self.screen.blit(BtnRegister.surf, BtnRegister.surf_rect)
            self.screen.blit(InputUser.surf, InputUser.surf_rect)
            self.screen.blit(InputPassword.surf, InputPassword.surf_rect)
            self.screen.blit(IconPassword.surf, IconPassword.surf_rect)
            self.screen.blit(UserIcon.surf, UserIcon.surf_rect)
            self.screen.blit(RePassword.surf, RePassword.surf_rect)
            self.screen.blit(RePasswordIcon.surf, RePasswordIcon.surf_rect)
            self.screen.blit(SignInIcon.surf, SignInIcon.surf_rect)
            
            for event in pygame.event.get():
                BtnRegister.onClick(event, lambda : print("on Press btn"))  # Fix: Replaced '=' with '=='
                InputUser.handleInput(event)
                InputPassword.handleInput(event)
                RePassword.handleInput(event)
                SignInIcon.onClick(event, self.goBack)
                
                if event.type == pygame.QUIT:
                    self.stop()            
            pygame.display.flip()
            self.clock.tick(60)
            
        return self.running
            
    def goBack(self):
        self.running = False
    

        
        
