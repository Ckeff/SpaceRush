import pygame
import random
import os
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


class Asteroid:
    def __init__(self, screen_size, P1_list, P2_list): #Constructor, takes screen size and info about P1 and P2 to spawn asteroids
        super().__init__()
        self.screen_size = screen_size #Stores screen size
        self.spawn_flag = False #Controlls when an asteroid can spawn
        while self.spawn_flag == False: #Loops until asteroids do not spawn on top of player
            P1_RECT = pygame.Rect(P1_list[1],P1_list[2],P1_list[3],P1_list[4])
            P2_RECT = pygame.Rect(P2_list[1],P2_list[2],P2_list[3],P2_list[4])
            self.Ast_RECT = pygame.Rect(random.randrange(screen_size[0]), random.randrange(screen_size[1]), 256, 256)
            if not pygame.Rect.colliderect(self.Ast_RECT, P1_RECT) and not pygame.Rect.colliderect(self.Ast_RECT, P2_RECT):
                self.spawn_flag = True
        self.astr_sprite = pygame.image.load(os.path.join('spr','ast.png')).convert_alpha() #Grabs the location of the sprite
        rand_max = 3 #Max possible movement speed of the asteroids
        self.move_x = random.randrange(rand_max*-1, rand_max)
        while self.move_x == 0:
            self.move_x = random.randrange(rand_max*-1, rand_max)

        self.move_y = random.randrange(rand_max*-1, rand_max)
        while self.move_y == 0:
            self.move_y = random.randrange(rand_max*-1, rand_max)
            
        self.scw_dist = -256
        self.ast_info = [0] * 5
        
    def movement(self):
        self.Ast_RECT.x += self.move_x #Move at generated speed
        self.Ast_RECT.y += self.move_y #Move at generated speed

    def get_ast(self): #Grab info about the asteroid for the update function 
        ast_info = [self.astr_sprite, self.Ast_RECT.x, self.Ast_RECT.y, self.Ast_RECT.w, self.Ast_RECT.h]
        return ast_info
        
    def hit(self, P_laser): #Checks to see if a laser hit the asteroid, returns a boolean
        flag = False
        P_LRECT = pygame.Rect(P_laser[1],P_laser[2],P_laser[3],P_laser[4])
        if pygame.Rect.colliderect(self.Ast_RECT, P_LRECT):
            flag = True
        return flag
        
    def screen_wrap(self): #Screen Wrapping
        #If object exits screen to the right, wrap around to the left
        if self.Ast_RECT.x > self.screen_size[0]:
            self.Ast_RECT.x = self.scw_dist
            
        #If object exits screen to the left, wrap around to the right    
        if self.Ast_RECT.x < self.scw_dist:
            self.Ast_RECT.x = self.screen_size[0]

        #If object exits screen downward, wrap around to the top
        if self.Ast_RECT.y > self.screen_size[1]:
            self.Ast_RECT.y = self.scw_dist
            
        #If object exits screen upward, wrap around to the bottom
        if self.Ast_RECT.y < self.scw_dist:
            self.Ast_RECT.y = self.screen_size[1]
            
class sm_Asteroid(Asteroid):
    def __init__(self, screen_size, ast_x, ast_y):
        self.screen_size = screen_size
        self.Ast_RECT = pygame.Rect(ast_x, ast_y, 128, 128)
        self.scw_dist = -128
        rand_max = 3
        self.move_x = random.randrange(rand_max*-1, rand_max)
        while self.move_x == 0:
            self.move_x = random.randrange(rand_max*-1, rand_max)

        self.move_y = random.randrange(rand_max*-1, rand_max)
        while self.move_y == 0:
            self.move_y = random.randrange(rand_max*-1, rand_max)
            
        self.astr_sprite = pygame.image.load(os.path.join('spr','sm_ast.png')).convert_alpha()
        
