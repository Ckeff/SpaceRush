import pygame
import mod.SprMOD
import math
#ScrMOD.py
#Contains all classes related to displaying the game


class Screen:
    def __init__(self, lvlnum): #Constructor
        super().__init__()
        self.size = (1152, 648) #Size of the scren (width, height)
        self.screen = pygame.display.set_mode(self.size) #Initalize the screen surface
        pygame.display.set_caption("Space Raiders") #Window title
        if lvlnum == 1: #Load Background
            self.animation_speed = 10
            self.BG = [pygame.image.load('spr\BG.png').convert(), pygame.image.load('spr\BG2.png').convert(), pygame.image.load('spr\BG3.png').convert(), pygame.image.load('spr\BG4.png').convert(), pygame.image.load('spr\BG5.png').convert()]
            self.BG2 = [0]
        elif lvlnum == 2:
            self.animation_speed = 10
            self.BG = [pygame.image.load('spr\BG22_1.png').convert(), pygame.image.load('spr\BG22_1.png').convert()]
            self.BG2 = [0]
            
        elif lvlnum == 3:
            self.animation_speed = 12
            self.BG = [pygame.image.load('spr\BG31_1.png').convert_alpha(), pygame.image.load('spr\BG31_1.png').convert_alpha(), pygame.image.load('spr\BG31_2.png').convert_alpha(), pygame.image.load('spr\BG31_3.png').convert_alpha(), pygame.image.load('spr\BG32_1.png').convert_alpha(), pygame.image.load('spr\BG32_2.png').convert_alpha(), pygame.image.load('spr\BG32_3.png').convert_alpha(), pygame.image.load('spr\BG33_1.png').convert_alpha(), pygame.image.load('spr\BG33_2.png').convert_alpha(), pygame.image.load('spr\BG33_3.png').convert_alpha(), pygame.image.load('spr\BG33_3.png').convert_alpha()]
            self.BG2 = [pygame.image.load('spr\stars.png').convert(), pygame.image.load('spr\stars.png').convert(), pygame.image.load('spr\stars2.png').convert(), pygame.image.load('spr\stars3.png').convert(), pygame.image.load('spr\stars4.png').convert(), pygame.image.load('spr\stars4.png').convert()]
            
        self.BG_Frames = len(self.BG) - 1
        self.BG_Frames2 = len(self.BG2) - 1
        
        self.i = 0
        self.i2 = 0
        self.rev_flag = False
        self.rev_flag2 = False
        self.index = 0
        self.index2 = 0
        
    def update(self, P1_list, P2_list, P1_Laser, P2_Laser, WallList, ast_list, smast_list, beam_info):
 
        #print(self.i)
        #print(index)

        if self.BG2[0] != 0:
            self.index2 = math.ceil(self.i2/self.animation_speed)
            self.screen.blit(self.BG2[self.index2], (0,0))
            if self.index2 == 0:
                self.rev_flag2 = not self.rev_flag2
            elif self.index2 == self.BG_Frames2:
                self.rev_flag2 = not self.rev_flag2
            
            if self.rev_flag2 == True:
                self.i2 += 1
            elif self.rev_flag2 == False:
                self.i2 -= 1
                
        self.index = math.ceil(self.i/self.animation_speed)
        self.screen.blit(self.BG[self.index], (0,0)) #Sets the BG image on the screen
        #print(index)
        if self.index == 0:
            self.rev_flag = not self.rev_flag
        elif self.index == self.BG_Frames:
            self.rev_flag = not self.rev_flag
            
        if self.rev_flag == True:
            self.i += 1
        elif self.rev_flag == False:
            self.i -= 1
            
            
        self.screen.blit(P1_list[0], (P1_list[1], P1_list[2])) #Sets the Player sprite to the current location of the rectangle on the screen
        self.screen.blit(P2_list[0], (P2_list[1], P2_list[2])) #Sets the Player sprite to the current location of the rectangle on the screen

        if P1_Laser[0] != 0: #If laser assigned sprite
            self.screen.blit(P1_Laser[0], (P1_Laser[1], P1_Laser[2]))
        if P2_Laser[0] != 0: #If laser assigned sprite
            self.screen.blit(P2_Laser[0], (P2_Laser[1], P2_Laser[2]))
        i = 0
        j = 0

        while i < 3:
            if ast_list[i] != 0:
                self.screen.blit(ast_list[i][0], (ast_list[i][1], ast_list[i][2])) #Update big asteroids
            i += 1
            
        while j < 6:
            if smast_list[j] != 0: 
                self.screen.blit(smast_list[j][0], (smast_list[j][1], smast_list[j][2])) #Update small asteroids
            if smast_list[j+1] != 0:
                self.screen.blit(smast_list[j+1][0], (smast_list[j+1][1], smast_list[j+1][2]))                
            j += 2

        if beam_info[0] != 0:
            self.screen.blit(beam_info[0], (beam_info[1], beam_info[2])) #Update rotating beam

        if WallList[0] != 0:
            for i in WallList: #draws all rectangles in list
                self.screen.blit(i.image, (i.x, i.y))
        pygame.display.flip() #Updates the screen
        

    def get_size(self):
        return self.size #Returns screen size

