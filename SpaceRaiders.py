#Kevin Andor, Cole Keffel, Cole Stewart
#Final Project CSC308
#Space Raiders


import pygame

def main():
    accy = 0 #Player acceleration in the Y axis
    accx = 0 #Player acceleration in the X axis
    speed = 7 #Max ship speed
    RECT = pygame.Rect(500, 100, 64, 64)#Player Hitbox (X, Y, Width, Height)

    
    pygame.init()
 
    size = (1152, 648) #Size of the scren (width, height)
    screen = pygame.display.set_mode(size) #Initalize the screen surface
 
    pygame.display.set_caption("Space Raiders") #Window title
 
    Player = pygame.image.load('P1.png').convert_alpha() #Load Player Sprite
    BG = pygame.image.load('BG.png').convert() #Load Background image
    flip = False #Flip flag for the player's sprite

 
    clock = pygame.time.Clock() #Used for managing how fast the screen updates

    done = False #Flag for closing the game (if user presses X)
    
#Game Loop
    while not done:
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
     
    #Game logic || NOTE: A player class will be made soon(TM), but for now movement will be in main() 

        #Movement
        #If the key is pressed       
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: #Move Up
                if accy > speed*-1:
                    accy -= .1
                RECT.y += accy
                
            if event.key == pygame.K_DOWN: #Move Down
                if accy < speed:
                    accy += .1
                RECT.y += accy
                
            if event.key == pygame.K_LEFT: #Move Left
                if flip == False: #Flips the player sprite
                    flip = True
                    Player = pygame.transform.flip(Player, True, False)
                    
                if accx > speed*-1:
                    accx -= .1
                RECT.x += accx
                
            if event.key == pygame.K_RIGHT: #Move Right
                if flip == True: #Flips the player sprite
                    flip = False
                    Player = pygame.transform.flip(Player, True, False)
                    
                if accx < speed:
                    accx += .1
                RECT.x += accx


        #If the key is not pressed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP: #Decelerate upward
                if accy < 0:
                    accy += .1
                RECT.y += accy
                
            if event.key == pygame.K_DOWN: #Decelerate downward
                if accy > 0:
                    accy -= .1
                RECT.y += accy
                
            if event.key == pygame.K_LEFT: #Decelerate leftward
                if accx < 0:
                    accx += .1
                RECT.x += accx
                
            if event.key == pygame.K_RIGHT: #Decelerate rightward
                if accx > 0:
                    accx -= .1
                RECT.x += accx




        #Screen Wrapping
        #If player exits screen to the right, wrap to the left
        if RECT.x > size[0]:
            RECT.x = -64
            
        #If player exits screen to the left, wrap to the right    
        if RECT.x < -64:
            RECT.x = size[0]

        #If player exits screen downward, wrap to the top
        if RECT.y > size[1]:
            RECT.y = -64
            
        #If player exits screen upward, wrap to the bottom
        if RECT.y < -64:
            RECT.y = size[1]
        
    #Screen-clearing
        screen.blit(BG, (0,0)) #Sets the BG image on the screen

    
    #Drawing
        #pygame.draw.rect(screen,RED,RECT)
        screen.blit(Player, RECT) #Sets the Player sprite to the current location of the rectangle on the screen

        pygame.display.flip()#Updates the screen
 
    
        clock.tick(60) #Limits game to 60 FPS
 

    pygame.quit() #Closes the window and quits the game



main()
