import pygame
import os
import random
import math
#SprMOD.py
#Loads sprites and applies necessary attributes (mostly needed for mask collisions)

class spr_BEAM(pygame.sprite.Sprite): #Sprite class for the big laser on level 3 (ironically also houses the functionality for some reason)
    def __init__(self, screen_size): #Constructor for the beam's sprite class, takes screen size as a parameter to determine where the center of the screen is
        pygame.sprite.Sprite.__init__(self)
        self.image_old = [pygame.image.load(os.path.join('spr','beam.png')).convert_alpha(), pygame.image.load(os.path.join('spr','beam2.png')).convert_alpha(), pygame.image.load(os.path.join('spr','beam3.png')).convert_alpha(), pygame.image.load(os.path.join('spr','beam4.png')).convert_alpha(), pygame.image.load(os.path.join('spr','beam5.png')).convert_alpha(), pygame.image.load(os.path.join('spr','beam6.png')).convert_alpha(), pygame.image.load(os.path.join('spr','beam2.png')).convert_alpha()] #Sets the sprite image
        self.image = self.image_old[0] #Creates a copy of the image to rotate
        self.rect = self.image.get_rect() #Sets the rectangle attribute for mask collision checking
        self.screen_size = screen_size #Saves the screen size to the class
        self.rect.center = (self.screen_size[0]/2, self.screen_size[1]/2) #Calculates where the center of the screen is
        self.angle = 0 #Stores the angle of the object
        self.rando = random.randint(0, 1) #Randomizer for determining initial spin direction
        self.spin_speed_max = 1.5 #Sets the max speed of the beam
        self.spin_speed = 0 #Inits the current spin speed to 0
        self.speed_up = True #Flag that determines whether the beam should speed up or slow down. Inits flag to True.
        self.i = 0
        self.index = 0
        self.beam_len = len(self.image_old) - 1
        #print(self.beam_len)
        
        if self.rando == 1: #Checks the result of the randomizer and sets spin direction.
            self.flip = True
        else:
            self.flip = False
            
    def rotate(self): #Rotates the beam from the center of the screen
        self.animate()
        self.image = pygame.transform.rotate(self.image_old[self.index], self.angle) #Rotates the image by the amount that is set in self.angle

        if self.spin_speed < self.spin_speed_max and self.speed_up == True: #If speed hasn't reached max and the speed up flag is set to true
            self.spin_speed += .001 #Accelerate
            
        elif self.spin_speed > 0 and self.speed_up == False: #Else if speed is above 0 and the speed up flag is set to false
            self.spin_speed -= .001 #Deccelerate

        if self.spin_speed >= self.spin_speed_max: #If the spin speed reaches the max speed
            self.speed_up = not self.speed_up #negate the speed up flag to slow down

        elif self.spin_speed <= 0: #Else if the spin speed reaches 0
            self.flip = not self.flip #negate the flip up flag to rotate in opposite direction
            self.speed_up = not self.speed_up #negate the speed up flag to speed up

        if self.flip == False: #Spins according to the direction flag set
            self.angle += self.spin_speed % 360
        elif self.flip == True:
            self.angle -= self.spin_speed % 360
            
        x, y = self.rect.center #Stores the old center of the image
        self.rect = self.image.get_rect() #Grabs the new rectangle of the rotated image
        self.rect.center = (x, y) #Sets the image to the old center of the screen
        self.mask = pygame.mask.from_surface(self.image) #Sets the mask attribute from the rotated image
        beam_info = [self.image, self.rect.x, self.rect.y, self.rect.w, self.rect.h] #Stores all the info about the beam into a list
        return beam_info #Retuns the beam's info

    def animate(self):
        self.index = math.ceil(self.i/4)
        
        if self.index == self.beam_len:
            self.i = 0
        else:
            self.i += 1
            
        #print(self.index)

    
class spr_Player1(pygame.sprite.Sprite):
    def __init__(self): #Constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(os.path.join('spr','P1.png')).convert_alpha() #Loads the player sprite
        self.rect = self.image.get_rect() #Set the rectangle attribute of the image
        self.mask = pygame.mask.from_surface(self.image) #Sets the mask attribute of the image 
        
    def flip(self): #Function that flips the sprite
        self.image = pygame.transform.flip(self.image, True, False) #Flips the sprite
        self.mask = pygame.mask.from_surface(self.image) #Sets the mask
        
    def make_mask(self): #Function that sets the mask attribute as needed
        self.mask = pygame.mask.from_surface(self.image)
        
class spr_Player2(spr_Player1): #Player 2's sprite attribute, with functions inherited from Player 1's sprite attributes
    def __init__(self): #Constructor similar to Player 1's innit, loads different image 
        pygame.sprite.Sprite.__init__(self) 

        self.image = pygame.image.load(os.path.join('spr','P2.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

