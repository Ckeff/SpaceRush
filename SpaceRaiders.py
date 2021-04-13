#Kevin Andor, Cole Keffel, Cole Stewart
#Final Project CSC308
#Space Raiders

LIGHTPURPLE = (153, 0, 153) #colors for wall
WALL_AMOUNT = 3 #how many walls

import pygame
import mod.PlrMOD #Imports the module containing player-related classes
import mod.ScrMOD #Imports the module containing display-related classes
import mod.LvObjMOD #Imports the module containing Level object classes, such as hazards and walls
import mod.LvlMOD #Imports the module containing the different map layouts in the game
def main():
    pygame.init()
    
    screen = mod.ScrMOD.Screen() #Inits the display screen
    
    Player_1 = mod.PlrMOD.Player() #Inits player 1
    Player_2 = mod.PlrMOD.Player() #Inits player 2
    Player_1.init_player(1) #Inits player 1 specific data
    Player_2.init_player(2) #Inits player 2 specific data

    WallList = [0] * WALL_AMOUNT #creates list for all walls based on wall amount constant
   # WallList[1] = mod.LvObjMOD.Wall(200, 200, 20, 20, LIGHTPURPLE, screen)
   # WallList[2] = mod.LvObjMOD.Wall(200, 400, 20, 20, LIGHTPURPLE, screen)
   #WallList[0] = mod.LvObjMOD.Wall(300, 400, 20, 20, LIGHTPURPLE, screen)

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

        P1_Laser = Player_1.shoot_laser()#Checks to see if player shoots this frame
        P2_Laser = Player_2.shoot_laser()

                
    #Screen wrapping
        Player_1.screen_wrap(screen.get_size()) #Screen Wrapping for P1
        Player_2.screen_wrap(screen.get_size()) #Screen wrapping for P2
        
    #Screen-clearing + Drawing
        Player_1.checkHit(P2_Laser)#Checks to see if a player collided with an enemy laser
        Player_2.checkHit(P1_Laser)
        
        P1_list = Player_1.get_player() #Retrieves player sprite and rectangle positions and puts them in a list
        P2_list = Player_2.get_player()

        screen.update(P1_list, P2_list, P1_Laser, P2_Laser, WallList) #Updates each players position on the screen
        clock.tick(60) #Limits game to 60 FPS
 

    pygame.quit() #Closes the window and quits the game

          
main() #Calls the main function
