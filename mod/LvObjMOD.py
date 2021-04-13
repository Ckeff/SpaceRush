import pygame

#LvObjMOD.py
#Contains all the classes relating to hazards and walls in in levels
#(Will probably be mostly used in LvlMOD.py)

class Wall:
    def __init__(self, x, y, width, height, color, screen): #Constructor
        #Initializes rectangle
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.screen = screen
        #Creates rectangle
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
