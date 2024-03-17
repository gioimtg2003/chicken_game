import pygame

from pygame.locals import (
    RLEACCEL,
    MOUSEBUTTONDOWN,
    KEYDOWN,
)

class InputText(pygame.sprite.Sprite):
    
    def __init__(self, width, height, x, y, size):
        super(InputText, self).__init__()
        self.surf = pygame.image.load(r'data\\components\\input.png')
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.text = ''
        self.font = pygame.font.Font(None, 32)
        self.surf_rect = self.surf.get_rect(x=x, y=y)
        self.focus = False
        self.size = size
        font = pygame.font.Font(r"data\font\FreeSansBold.ttf", 32)
        print(pygame.mouse.get_pos())

        
        
    def handleChange(self, pressed_keys):

        if pressed_keys[MOUSEBUTTONDOWN]:
            if self.surf_rect.collidepoint(pygame.mouse.get_pos()):
                self.focus = True
            else:
                self.focus = False
        if pressed_keys[KEYDOWN]:
            if self.focus:
                if pressed_keys.unicode == '\x08':
                    self.text = self.text[:-1]
                else:
                    self.text += pressed_keys.unicode
                    # draw text
                    text_surface = self.font.render(self.text, True, (0, 0, 0))
                    self.surf.blit(text_surface, (self.surf_rect.x + 10, self.surf_rect.y + 10))
        print(pressed_keys)
                    

            
    def hoverInput(self):
        if self.surf_rect.collidepoint(pygame.mouse.get_pos()):
            self.focus = True
            self.surf = pygame.image.load(r'data\\components\\inputHover.png')
        else:
            self.surf = pygame.image.load(r'data\\components\\input.png')
            print("No Hover")
        