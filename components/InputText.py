import pygame

from pygame.locals import (
    RLEACCEL,
    MOUSEBUTTONDOWN,
    KEYDOWN,
    K_UP,
    K_BACKSPACE
)

class InputText(pygame.sprite.Sprite):
    
    def __init__(self, x, y, size, type = "text"):
        super(InputText, self).__init__()
        self.surf = pygame.image.load(r'data\\components\\input.png')
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.text = ''
        self.font = pygame.font.Font(None, 32)
        self.surf_rect = self.surf.get_rect(center = (x, y))
        self.focus = False
        self.size = size
        self.font = pygame.font.Font(r"data\font\FreeSansBold.ttf", 32)
        self.type = type
        self.showText = self.text if self.type == "text" else "*" * len(self.text)
        
    def handleInput(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if self.surf_rect.collidepoint(pygame.mouse.get_pos()):
                print("focus text input")
                self.focus = True
                text_surface = self.font.render(self.showText, True, (0, 0, 0))
                
                self.surf = pygame.image.load(r'data\\components\\inputFocus.png')
                self.surf.blit(text_surface, text_surface.get_rect(center = (self.surf_rect.width/2, self.surf_rect.height/2)))
                
            else:
                text_surface = self.font.render(self.showText, True, (0, 0, 0))
                self.surf = pygame.image.load(r'data\\components\\input.png')
                self.surf.blit(text_surface, text_surface.get_rect(center = (self.surf_rect.width/2, self.surf_rect.height/2)))
                self.focus = False
                print("No Hover")
            
        if event.type == KEYDOWN:
            if self.focus:
                if event.key == K_BACKSPACE:
                    if len(self.text) > 0:
                        self.text = self.text[:-1]
                    text_surface = self.font.render(self.showText, True, (0, 0, 0))
                    print(self.showText)
                    self.updateText()
                    self.surf.blit(text_surface, text_surface.get_rect(center = (self.surf_rect.width/2, self.surf_rect.height/2)))
                else:
                    
                    self.text +=  event.unicode
                    self.updateText()
                text_surface = self.font.render(self.showText, True, (0, 0, 0))
                self.surf = pygame.image.load(r'data\\components\\inputFocus.png')
                self.surf.blit(text_surface, text_surface.get_rect(center = (self.surf_rect.width/2, self.surf_rect.height/2)))
        
        
            
    def focusInput(self):
        print(pygame.mouse.get_pos())
        print(self.surf_rect)
        
            
    def updateText(self):
        self.showText = self.text if self.type == "text" else "*" * len(self.text)
        
    def getValue(self):
        return self.text    
        