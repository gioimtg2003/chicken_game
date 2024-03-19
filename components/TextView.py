import pygame

class TextView(pygame.sprite.Sprite):
    
    def __init__ (self, text, x, y, size, color):
        super(TextView, self).__init__()
        self.font = pygame.font.Font(r"data\font\FreeSansBold.ttf", size)
        self.text = text
        self.surf = self.font.render(self.text, True, color)
        self.surf_rect = self.surf.get_rect(center = (x, y) )
    
    
    
        