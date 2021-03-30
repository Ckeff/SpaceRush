#Kevin Andor, Cole Keffel, Cole Stewart
#Final Project CSC308
#Space Raiders

LIGHTPURPLE = (153, 0, 153) #colors for wall
WALL_AMOUNT = 3 #how many walls

import pygame

def main():
    pygame.init()
    
    screen = Screen() #Inits the display screen
    
    Player_1 = Player() #Inits player 1
    Player_2 = Player() #Inits player 2
    Player_1.init_player(1) #Inits player 1 specific data
    Player_2.init_player(2) #Inits player 2 specific data

    WallList = [0] * WALL_AMOUNT #creates list for all walls based on wall amount constant
    WallList[1] = Wall(200, 200, 20, 20, LIGHTPURPLE, screen)
    WallList[2] = Wall(200, 400, 20, 20, LIGHTPURPLE, screen)
    WallList[0] = Wall(300, 400, 20, 20, LIGHTPURPLE, screen)

    clock = pygame.time.Clock() #Used for managing how fast the screen updates
    done = False #Flag for closing the game (if user presses X)
    
#Game Loop
    while not done:
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True #Sets flag for quitting the game
     
    #Game logic 

        #Movement
        Player_1.movement()#Player 1 movement function
        Player_2.movement()#Player 2 movement function

                
    #Screen wrapping
        Player_1.screen_wrap(screen.get_size()) #Screen Wrapping for P1
        Player_2.screen_wrap(screen.get_size()) #Screen wrapping for P2
        
    #Screen-clearing + Drawing
        P1_list = Player_1.get_player() #Retrieves player sprite and rectangle positions and puts them in a list
        P2_list = Player_2.get_player()
        Player_1.checkCollision(pygame.Rect(P1_list[1], P1_list[2], 64, 64), WallList, 1)
        Player_2.checkCollision(pygame.Rect(P2_list[1], P2_list[2], 64, 64), WallList, 2)
        screen.update(P1_list, P2_list, WallList) #Updates each players position on the screen
        clock.tick(60) #Limits game to 60 FPS
 

    pygame.quit() #Closes the window and quits the game

class Screen:
    def __init__(self): #Constructor
        super().__init__()
        self.size = (1152, 648) #Size of the scren (width, height)
        self.screen = pygame.display.set_mode(self.size) #Initalize the screen surface
        pygame.display.set_caption("Space Raiders") #Window title
        self.BG = pygame.image.load('BG.png').convert() #Load Background image

    def update(self, P1_list, P2_list, WallList):
        self.screen.blit(self.BG, (0,0)) #Sets the BG image on the screen
        self.screen.blit(P1_list[0], (P1_list[1], P1_list[2])) #Sets the Player sprite to the current location of the rectangle on the screen
        self.screen.blit(P2_list[0], (P2_list[1], P2_list[2])) #Sets the Player sprite to the current location of the rectangle on the screen
        for i in WallList: #draws all rectangles in list
            pygame.draw.rect(self.screen, i.color, [i.x, i.y, i.width, i.height], 0)
        pygame.display.flip() #Updates the screen
        

    def get_size(self):
        return self.size #Returns screen size

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


class Player:
    def __init__(self): #Constructor
        super().__init__()
        
        self.accx = 0 #Player acceleration in the x axis
        self.accy = 0 #Player acceleration in the y axis
        self.speed = 4.5 #Max ship speed

    def init_player(self, P_num):
        self.P_num = P_num

        #checks for the player number the class initalized with and sets the approptiate starting position and sprite
        if self.P_num == 1: 
            self.P_Sprite = pygame.image.load('P1.png').convert_alpha() #Load Player Sprite
            P_pos = (288, 100)
            self.flip = False #Flip flag for the player's sprite

        elif self.P_num == 2:
            self.P_Sprite = pygame.image.load('P2.png').convert_alpha() #Load Player Sprite
            P_pos = (864, 100)
            self.P_Sprite = pygame.transform.flip(self.P_Sprite, True, False)
            self.flip = True #Flip flag for the player's sprite
            
        self.RECT = pygame.Rect(P_pos[0], P_pos[1], 64, 64) #Player Hitbox (X, Y, Width, Height)

    def checkCollision(self, player, WallList, playernumber): #Checks collision between player and wall
        for i in WallList: #checks to see if player collides with any existing walls
            if pygame.Rect.colliderect(player, pygame.Rect(i.x, i.y, i.height, i.width)):
                self.init_player(playernumber)

#--------Movement--------
    def movement(self):
        key = pygame.key.get_pressed()
        if self.P_num == 1: #Player 1 controls
            if key[pygame.K_w]: #Move Up
                self.acc_up()
            if key[pygame.K_s]: #Move Down
                self.acc_down()
            if key[pygame.K_a]: #Move Left
                self.acc_left()
            if key[pygame.K_d]: #Move Right
                self.acc_right()
            
            if not key[pygame.K_w] or key[pygame.K_s]: #Decelerate Up
                self.dec_up()
            if not key[pygame.K_s] or key[pygame.K_w]: #Decelerate Down
                self.dec_down()
            if not key[pygame.K_a] or key[pygame.K_d]: #Decelerate Left
                self.dec_left()
            if not key[pygame.K_d] or key[pygame.K_a]: #Decelerate Right
                self.dec_right()
                    
        elif self.P_num == 2: #Player 2 controls
            if key[pygame.K_UP]: #Move Up
                self.acc_up()
            if key[pygame.K_DOWN]: #Move Down
                self.acc_down()
            if key[pygame.K_LEFT]: #Move Left
                self.acc_left()
            if key[pygame.K_RIGHT]: #Move Right
                self.acc_right()
                
            if not key[pygame.K_UP] or key[pygame.K_DOWN]: #Decelerate Up
                self.dec_up()
            if not key[pygame.K_DOWN] or key[pygame.K_UP]: #Decelerate Down
                self.dec_down()
            if not key[pygame.K_LEFT] or key[pygame.K_RIGHT]: #Decelerate Left
                self.dec_left()
            if not key[pygame.K_RIGHT] or key[pygame.K_LEFT]: #Decelerate Right
                self.dec_right()
                
 #-------Acceleration Functions--------
    def acc_up(self):
        if self.accy > self.speed*-1:
            self.accy -= .1
        self.RECT.y += self.accy
            
    def acc_down(self):
        if self.accy < self.speed:
            self.accy += .1
        self.RECT.y += self.accy
            
    def acc_left(self):
        if self.flip == False: #Flips the player sprite
            self.flip = True
            self.P_Sprite = pygame.transform.flip(self.P_Sprite, True, False)
                    
        if self.accx > self.speed*-1:
            self.accx -= .1
        self.RECT.x += self.accx
        
    def acc_right(self):
        if self.flip == True: #Flips the player sprite
            self.flip = False
            self.P_Sprite = pygame.transform.flip(self.P_Sprite, True, False)
                    
        if self.accx < self.speed:
            self.accx += .1
        self.RECT.x += self.accx

 #-------Deceleration Functions--------
    def dec_up(self):
        if self.accy < 0:
            self.accy += .1
        if self.accy < 0.09 and self.accy > -0.09:
            self.accy = 0
        self.RECT.y += self.accy

    def dec_down(self):
        if self.accy > 0:
            self.accy -= .1
        if self.accy < 0.09 and self.accy > -0.09:
            self.accy = 0
        self.RECT.y += self.accy
                
    def dec_left(self):
        if self.accx < 0:
            self.accx += .1
        if self.accx < 0.09 and self.accx > -0.09:
            self.accx = 0
        self.RECT.x += self.accx
        
    def dec_right(self):
        if self.accx > 0:
            self.accx -= .1
        if self.accx < 0.09 and self.accx > -0.09:
            self.accx = 0
        self.RECT.x += self.accx

#-------------------------------------
        
    def screen_wrap(self, screen_size): #Screen Wrapping
        #If player exits screen to the right, wrap around to the left
        if self.RECT.x > screen_size[0]:
            self.RECT.x = -64
            
        #If player exits screen to the left, wrap around to the right    
        if self.RECT.x < -64:
            self.RECT.x = screen_size[0]

        #If player exits screen downward, wrap around to the top
        if self.RECT.y > screen_size[1]:
            self.RECT.y = -64
            
        #If player exits screen upward, wrap around to the bottom
        if self.RECT.y < -64:
            self.RECT.y = screen_size[1]

    def get_player(self): #Returns a list containing the player sprite to be used and the position of the hitbox (RECT) 
        P_list = [self.P_Sprite, self.RECT.x, self.RECT.y]
        return P_list

    #def projectile(self):
        

main() #Calls the main function
