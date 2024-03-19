import pygame

class Button(pygame.sprite.Sprite):
    
    def __init__(self, x, y, src, hover = None):
        super(Button, self).__init__()
        self.surf = pygame.image.load(src)
        self.hover = hover
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.surf_rect = self.surf.get_rect(center = (x, y))
        self.src = src
        
    def onClick(self, event, action ):
        if self.hover != None:
            if self.surf_rect.collidepoint(pygame.mouse.get_pos()):
                self.surf = pygame.image.load(self.hover)
                self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
                self.surf_rect = self.surf.get_rect(center = self.surf_rect.center)
            else:
                self.surf = pygame.image.load(self.src)
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.surf_rect.collidepoint(mouse_pos):
                action()
    