import pygame

#PlrMOD.py
#Contains all classes related to player functionality (including lasers)



class Laser:
    def __init__(self): #Constructor
        super().__init__()
        self.speed = 45 #Limits how fast the laser moves when shot
        
    def make_laser(self, P_num, P_RECT_x, P_RECT_y, flip): #Using the current players positional information, creates a new laser and returns information about it in a list
        self.P_num = P_num
        self.flip = flip
        if self.P_num == 1: #Checks to see which sprite index to use
            Laser_name = 'spr\P1_Laser.png'
        elif self.P_num == 2:
            Laser_name = 'spr\P2_Laser.png'

        if self.flip != True: #Checks to see which direction the laser should start at
            P_RECT_x = P_RECT_x+64

        L_Sprite = pygame.image.load(Laser_name).convert_alpha()
        L_pos = (P_RECT_x, P_RECT_y+16)
        self.Laser_RECT = pygame.Rect(L_pos[0], L_pos[1], 32, 16)
        laserInfo = [L_Sprite, self.Laser_RECT.x, self.Laser_RECT.y, self.Laser_RECT.w, self.Laser_RECT.h] #laserInfo = [Sprite index, X, Y, WIDTH, HEIGHT]
        return laserInfo

    def laser_movement(self, Laser_RECT_in): #Using the latest positional information stored in laserInfo, checks to see which direction the laser should move in and increases/decreases the position by the speed set.
                                            #Returns the new positional value for the laser's hitbox
        if self.flip == True: #If ship is facing left when shot, move laser left
            Laser_RECT_in -= self.speed

        else: #If ship is facing right when shot, move laser right
            Laser_RECT_in += self.speed
            
        self.Laser_RECT.x = Laser_RECT_in #Update the position of the laser hitbox
        return self.Laser_RECT.x



class Player:
    def __init__(self): #Constructor
        super().__init__()
        
        self.accx = 0 #Player acceleration in the x axis
        self.accy = 0 #Player acceleration in the y axis
        self.speed = 4.5 #Max ship speed
        
        self.laserShot = Laser() #Creates a laser class for the player to allow them to shoot
        self.laserInfo = [0]*5 #Inits a list to store information about the laser shot
        self.laserActive = False #Flag for if a player's laser is active
        self.laserEndLife = 45 #Sets the max time a laser can be out for
        self.laserCurLife = 0 #Counts the current time a laser has been active
        self.lives = 3 #Counts how many lives the player has left
        
    def init_player(self, P_num):
        self.P_num = P_num

        #checks for the player number the class initalized with and sets the approptiate starting position and sprite
        if self.P_num == 1: 
            self.P_Sprite = pygame.image.load('spr\P1.png').convert_alpha() #Load Player Sprite
            P_pos = (288, 100)
            self.flip = False #Flip flag for the player's sprite

        elif self.P_num == 2:
            self.P_Sprite = pygame.image.load('spr\P2.png').convert_alpha() #Load Player Sprite
            P_pos = (864, 100)
            self.P_Sprite = pygame.transform.flip(self.P_Sprite, True, False)
            self.flip = True #Flip flag for the player's sprite
            
        self.RECT = pygame.Rect(P_pos[0], P_pos[1], 64, 64) #Player Hitbox (X, Y, Width, Height)

    def checkHit(self, P_Laser): #Checks collision between player and laser
        if pygame.Rect.colliderect(self.RECT, pygame.Rect(P_Laser[1], P_Laser[2], P_Laser[3], P_Laser[4])):
            self.init_player(self.P_num)

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

    def shoot_laser(self): #Checks to see if either player shot a laser and activates the appropriate creation and movement functions of the laser
                            #Returns information about the laser
        key = pygame.key.get_pressed()
        if self.laserActive == False: #If the player has not shot a laser
            if self.P_num == 1 and key[pygame.K_LSHIFT]: #If player 1 and left shift is pressed
                self.laserInfo = self.laserShot.make_laser(self.P_num, self.RECT.x, self.RECT.y, self.flip) #Creates a new laser
                self.laserActive = True #Sets the active laser flag to true

            if self.P_num == 2 and key[pygame.K_KP0]: #If player 2 and Num0 is pressed
                self.laserInfo = self.laserShot.make_laser(self.P_num, self.RECT.x, self.RECT.y, self.flip) #Creates a new laser
                self.laserActive = True #Sets the active laser flag to true

        if self.laserActive == True: #If the laser is active
                if self.laserCurLife < self.laserEndLife: #If the laser has not reached it's end of life yet
                    self.laserInfo[1] = self.laserShot.laser_movement(self.laserInfo[1])#Move the laser
                    self.laserCurLife += 1 #Increase life count by 1

                else: #If the laser has reached it's end of life
                    self.laserCurLife = 0 #Reset the lasers current life to 0
                    self.laserInfo = [0]*5 #Clear any information about the laser
                    self.laserActive = False #Sets the laser to inactive, allows the player to shoot next frame
                    
        return self.laserInfo 