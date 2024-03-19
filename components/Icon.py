import pygame

class Icon(pygame.sprite.Sprite):
    
    def __init__ (self, x, y, src):
        super(Icon, self).__init__()
        self.surf = pygame.image.load(src)
        self.surf_rect = self.surf.get_rect(center = (x, y))
    
    def onClick(self, event, action, *args, **kwargs):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.surf_rect.collidepoint(mouse_pos):
                action()  
        
    
        