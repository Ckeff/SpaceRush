import pygame
import mod.SprMOD
#ScrMOD.py
#Contains all classes related to displaying the game


class Screen:
    def __init__(self): #Constructor
        super().__init__()
        self.size = (1152, 648) #Size of the scren (width, height)
        self.screen = pygame.display.set_mode(self.size) #Initalize the screen surface
        pygame.display.set_caption("Space Raiders") #Window title
        self.BG = pygame.image.load('spr\BG.png').convert() #Load Background image

    def update(self, P1_list, P2_list, P1_Laser, P2_Laser, WallList, ast_list, smast_list, beam_info, color):
        self.screen.blit(self.BG, (0,0)) #Sets the BG image on the screen
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

        #for i in WallList: #draws all rectangles in list
            #pygame.draw.rect(self.screen, i.color, [i.x, i.y, i.width, i.height], 0)
        pygame.display.flip() #Updates the screen
        

    def get_size(self):
        return self.size #Returns screen size

