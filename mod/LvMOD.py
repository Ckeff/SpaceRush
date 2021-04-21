import pygame
import mod.PlrMOD #Imports the module containing player-related classes
import mod.ScrMOD #Imports the module containing display-related classes
import mod.LvObjMOD #Imports the module containing Level object classes, such as hazards and walls



class Level:
    def __init__(self, lvlnum):
        if lvlnum == 1:
            self.Lvl_1()
        elif lvlnum == 2:
            self.Lvl_2()
        elif lvlnum == 3:
            self.Lvl_3()

    def Lvl_1(self): #Asteroids level
        LIGHTPURPLE = (153, 0, 153) #colors for wall
        WALL_AMOUNT = 3 #how many walls
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
        Player_1.send_screen(screen.get_size())
        Player_2.send_screen(screen.get_size())
        P1_list = Player_1.get_player() #Retrieves player sprite and rectangle positions and puts them in a list
        P2_list = Player_2.get_player()
        map_selection = 1
        smast_opened = 0
        if map_selection == 1:
            i = 0
            j = 0
            k = 0
            ast_list = [0]*3
            ast = [0]*3
            smast_list = [0]*6
            smast = [0]*6
            smast_filled = 0
            smast_empty = 0
            ast_respawn_max = 150
            ast_respawn_count = [0]*3
            #ast_mrespawn = 900
            while i < 3: 
                ast[i] = mod.LvObjMOD.Asteroid(screen.get_size(), P1_list, P2_list)
                ast_list[i] = ast[i].get_ast()
                i += 1
        
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

            if map_selection == 1:
                i = 0
                j = 0
                while i < 3:
                    if ast_list[i] != 0:
                        ast[i].movement()
                    i += 1
                    
                while j < 6:
                    if smast_list[j] != 0 and smast_list[j] != -1:
                        smast[j].movement()
                    if smast_list[j+1] != 0 and smast_list[j+1] != -1:
                        smast[j+1].movement()
                    j += 2
                        
                    
        #Screen wrapping
            Player_1.screen_wrap() #Screen Wrapping for P1
            Player_2.screen_wrap() #Screen wrapping for P2
            if map_selection == 1:
                i = 0
                j = 0
                while i < 3:
                    if ast_list[i] != 0:
                        ast[i].screen_wrap()
                    i += 1
                    
                while j < 6:
                    if smast_list[j] != 0 and smast_list[j] != -1:
                        smast[j].screen_wrap()
                    if smast_list[j+1] != 0 and smast_list[j+1] != -1:
                        smast[j+1].screen_wrap()
                    j += 2
            
        #Screen-clearing + Drawing
            if Player_1.checkHit(P2_Laser): #Checks to see if a player collided with a player/satellite's laser or an asteroid
                P2_Laser = Player_2.destroy_laser() #Destroy the incoming laser if so
                
            if Player_2.checkHit(P1_Laser):
                P1_Laser = Player_1.destroy_laser()            
            
            if map_selection == 1:
                #hit_flag = [False, False]
                i = 0
                j = 0
                k = 0
                smast_filled = 0
                #p1flag = False
                #p2flag = False
                while i < 3:
                   # print("Should loop 3 times")
                    if ast_list[i] != 0: 
                        Player_1.checkHit(ast_list[i]) #Checks to see if player got hit by an asteroid
                        Player_2.checkHit(ast_list[i])
                        P1_ast = ast[i].hit(P1_Laser)
                        P2_ast = ast[i].hit(P2_Laser)
                        if P1_ast or P2_ast: #Checks to see if an asteroid got hit by an enemy laser
                            while k < 6:
                                if smast[k] == 0 and smast_list[k] == 0 and smast_filled < 2:
                                    smast[k] = mod.LvObjMOD.sm_Asteroid(screen.get_size(), ast_list[i][1], ast_list[i][2])
                                    smast_list[k] = smast[k].get_ast()
                                    smast_filled += 1

                                if smast_filled >= 2:
                                    k = 7
             #                   if smast[k+1] == 0 and smast_list[k+1] == 0 and smast_filled < 2:
              #                      smast[k+1] = mod.LvObjMOD.sm_Asteroid(screen.get_size(), ast_list[i][1], ast_list[i][2])
               #                     smast_list[k+1] = smast[k+1].get_ast()
                #                    smast_filled += 1
                                else:
                                    k += 1
                            
                            ast[i] = 0
                            ast_list[i] = 0
                            
                            if P1_ast:
                                P1_Laser = Player_1.destroy_laser()
                            elif P2_ast:
                                P2_Laser = Player_2.destroy_laser()
                    i += 1

                while j < 6:
                    if smast_list[j] != 0 and smast_list[j] != -1:
                        Player_1.checkHit(smast_list[j])
                        Player_2.checkHit(smast_list[j])
                        
                        if smast[j].hit(P1_Laser):
                            smast[j] = 0 #-1 means just destroyed, 0 means empty but big asteroid could cause otherwise
                            smast_list[j] = 0
                            P1_Laser = Player_1.destroy_laser()
                            smast_empty += 1
                            
                        elif smast[j].hit(P2_Laser):
                            smast[j] = 0
                            smast_list[j] = 0
                            P2_Laser = Player_2.destroy_laser()
                            smast_empty += 1
                            
                    j += 1

                i = 0
                while i < 3:
                    if smast_empty >= 2 and ast_list[i] == 0:
                        smast_empty -= 2
                        ast_respawn_count[i] += 1
                        
                    elif ast_respawn_count[i] > 0 and ast_respawn_count[i] < ast_respawn_max and ast_list[i] == 0:
                        ast_respawn_count[i] += 1
                        
                    elif ast_respawn_count[i] == ast_respawn_max and ast_list[i] == 0:
                        ast[i] = mod.LvObjMOD.Asteroid(screen.get_size(), P1_list, P2_list)
                        ast_list[i] = ast[i].get_ast()
                        ast_respawn_count[i] = 0

                    i+=1
                    
            P1_list = Player_1.get_player() #Retrieves player sprite and rectangle positions and puts them in a list
            P2_list = Player_2.get_player()

            if map_selection == 1:
                i = 0
                j = 0
                while i < 3:
                    if ast_list[i] != 0:
                        ast_list[i] = ast[i].get_ast()
                    i += 1
                    
                while j < 6:
                    if smast_list[j] != 0 and smast_list[j] != -1:
                        smast_list[j] = smast[j].get_ast()
                    if smast_list[j+1] != 0 and smast_list[j+1] != -1:
                        smast_list[j+1] = smast[j+1].get_ast()
                    j += 2
           
            screen.update(P1_list, P2_list, P1_Laser, P2_Laser, WallList, ast_list, smast_list) #Updates each players position on the screen
           # print("Reaches end")
            clock.tick(60) #Limits game to 60 FPS
        pygame.quit() #Closes the window and quits the game

    def Lvl_2(self): #Teleporter level
        
        LIGHTPURPLE = (153, 0, 153) #colors for wall
        WALL_AMOUNT = 3 #how many walls
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
        Player_1.send_screen(screen.get_size())
        Player_2.send_screen(screen.get_size())
        P1_list = Player_1.get_player() #Retrieves player sprite and rectangle positions and puts them in a list
        P2_list = Player_2.get_player()
        ast_list = [0]*3
        smast_list = [0]*6
   
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
            Player_1.screen_wrap() #Screen Wrapping for P1
            Player_2.screen_wrap() #Screen wrapping for P2
            
        #Screen-clearing + Drawing
            if Player_1.checkHit(P2_Laser): #Checks to see if a player collided with a player/satellite's laser or an asteroid
                P2_Laser = Player_2.destroy_laser() #Destroy the incoming laser if so
                
            if Player_2.checkHit(P1_Laser):
                P1_Laser = Player_1.destroy_laser()            
            
                    
            P1_list = Player_1.get_player() #Retrieves player sprite and rectangle positions and puts them in a list
            P2_list = Player_2.get_player()
           
            screen.update(P1_list, P2_list, P1_Laser, P2_Laser, WallList, ast_list, smast_list) #Updates each players position on the screen
           # print("Reaches end")
            clock.tick(60) #Limits game to 60 FPS
        pygame.quit() #Closes the window and quits the game

    def Lvl_3(self): #Satellites level
        
        LIGHTPURPLE = (153, 0, 153) #colors for wall
        WALL_AMOUNT = 3 #how many walls
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
        Player_1.send_screen(screen.get_size())
        Player_2.send_screen(screen.get_size())
        P1_list = Player_1.get_player() #Retrieves player sprite and rectangle positions and puts them in a list
        P2_list = Player_2.get_player()
        ast_list = [0]*3
        smast_list = [0]*6
   
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
            Player_1.screen_wrap() #Screen Wrapping for P1
            Player_2.screen_wrap() #Screen wrapping for P2
            
        #Screen-clearing + Drawing
            if Player_1.checkHit(P2_Laser): #Checks to see if a player collided with a player/satellite's laser or an asteroid
                P2_Laser = Player_2.destroy_laser() #Destroy the incoming laser if so
                
            if Player_2.checkHit(P1_Laser):
                P1_Laser = Player_1.destroy_laser()            
            
                    
            P1_list = Player_1.get_player() #Retrieves player sprite and rectangle positions and puts them in a list
            P2_list = Player_2.get_player()
           
            screen.update(P1_list, P2_list, P1_Laser, P2_Laser, WallList, ast_list, smast_list) #Updates each players position on the screen
           # print("Reaches end")
            clock.tick(60) #Limits game to 60 FPS
        pygame.quit() #Closes the window and quits the game  
