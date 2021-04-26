import pygame
import mod.PlrMOD #Imports the module containing player-related classes
import mod.ScrMOD #Imports the module containing display-related classes
import mod.LvObjMOD #Imports the module containing Level object classes, such as hazards and walls
import mod.SprMOD #Imports the module containing sprites and their attributes


class Level:
    def __init__(self): #Takes the level selection as input and selects the desired level layout
        super().__init__()    
        
    def lvl_selector(self, lvlnum):
        self.lvlnum = lvlnum
        if lvlnum == 1:
            option = self.Lvl_1()
        elif lvlnum == 2:
            option = self.Lvl_2()
        elif lvlnum == 3:
            option = self.Lvl_3()
        return option

    def Lvl_1(self): #Asteroids level
        COLOR = (0, 0, 0) #color for debug wall
        WALL_AMOUNT = 3 #how many walls
        pygame.init()
        
        screen = mod.ScrMOD.Screen(self.lvlnum) #Inits the display screen
        
        Player_1 = mod.PlrMOD.Player(500) #Inits player 1
        Player_2 = mod.PlrMOD.Player(500) #Inits player 2
        Player_1.init_player(1) #Inits player 1 specific data
        Player_2.init_player(2) #Inits player 2 specific data

        WallList = [0] * WALL_AMOUNT #creates list for all walls based on wall amount constant

        clock = pygame.time.Clock() #Used for managing how fast the screen updates
        done = False #Flag for closing the game (if user presses X)
        Player_1.send_screen(screen.get_size())
        Player_2.send_screen(screen.get_size())
        P1_list = Player_1.get_player() #Retrieves player sprite and rectangle positions and puts them in a list
        P2_list = Player_2.get_player()
        beam_info = [0]*2
        map_selection = 1
        smast_opened = 0

        i = 0 #Loop counter for big asteroids
        j = 0 #Loop counter for small asteroids
        k = 0 #Loop counter for small asteroids within big asteroid loop
        
        ast_list = [0]*3 #Inits the list of info for big asteroids
        ast = [0]*3 #Inits the list of asteroids
        smast_list = [0]*6 #Inits the list of info for small asteroids
        smast = [0]*6 #Inits the list of small asteroids
        smast_filled = 0 #Inits the count of filled small asteroid slots
        smast_empty = 0 #Inits the count of empty small asteroid slots
        ast_respawn_max = 150 #Max repawn time of a big asteroid
        ast_respawn_count = [0]*3 #Inits the list of each big asteroids respawn count
        winner = [0]*2
        while i < 3: #Creates three asteroids and grabs their info
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
            #game_over = Player_1.Game_Over()
            #game_over = Player_2.Game_Over()
                         
            #Movement
            Player_1.movement()#Player 1 movement function
            Player_2.movement()#Player 2 movement function

            P1_Laser = Player_1.shoot_laser()#Checks to see if player shoots this frame
            P2_Laser = Player_2.shoot_laser()

            i = 0
            j = 0
            while i < 3: #Moves every big asteroid
                if ast_list[i] != 0:
                    ast[i].movement()
                i += 1
                    
            while j < 6: #Moves every small asteroid
                if smast_list[j] != 0:
                    smast[j].movement()
                    
                if smast_list[j+1] != 0:
                    smast[j+1].movement()
                j += 2
                        
                    
        #Screen wrapping
            Player_1.screen_wrap() #Screen Wrapping for P1
            Player_2.screen_wrap() #Screen wrapping for P2
            
            i = 0
            j = 0
            while i < 3: #Screen wrapping for each big asteroid
                if ast_list[i] != 0:
                    ast[i].screen_wrap()
                i += 1
                    
            while j < 6: #Screen wrapping for each small asteroid
                if smast_list[j] != 0 and smast_list[j] != -1:
                    smast[j].screen_wrap()
                if smast_list[j+1] != 0 and smast_list[j+1] != -1:
                    smast[j+1].screen_wrap()
                j += 2
            
        #Screen-clearing + Drawing
            if Player_1.checkHit(P2_Laser, False): #Checks to see if a player collided with a player/satellite's laser or an asteroid
                P2_Laser = Player_2.destroy_laser() #Destroy the incoming laser if so
                
            if Player_2.checkHit(P1_Laser, False):
                P1_Laser = Player_1.destroy_laser()            
            

            i = 0
            j = 0
            k = 0
            smast_filled = 0
                
            while i < 3:
                  
                if ast_list[i] != 0: 
                    Player_1.checkHit(ast_list[i], False) #Checks to see if player got hit by an asteroid
                    Player_2.checkHit(ast_list[i], False)
                    
                    P1_ast = ast[i].hit(P1_Laser) #Checks to see if a big asteroid got hit by an enemy laser
                    P2_ast = ast[i].hit(P2_Laser)
                    
                    if P1_ast or P2_ast: #If a big asteroid is destroyed, create two smaller asteroids and destriy the big asteroid
                        while k < 6:
                            if smast[k] == 0 and smast_list[k] == 0 and smast_filled < 2:
                                smast[k] = mod.LvObjMOD.sm_Asteroid(screen.get_size(), ast_list[i][1], ast_list[i][2])
                                smast_list[k] = smast[k].get_ast()
                                smast_filled += 1

                            if smast_filled >= 2:
                                k = 7
                            else:
                                k += 1
                            
                        ast[i] = 0
                        ast_list[i] = 0
                            
                        if P1_ast: #If the asteroid is hit by a laser, destroy the laser
                            P1_Laser = Player_1.destroy_laser()
                        elif P2_ast:
                            P2_Laser = Player_2.destroy_laser()
                i += 1

            while j < 6: #Checks to see if a small asteroid got hit by a laser
                if smast_list[j] != 0:
                    Player_1.checkHit(smast_list[j], False)
                    Player_2.checkHit(smast_list[j], False)
                        
                    if smast[j].hit(P1_Laser): #If hit, destroy the asteroid, and count the amount of empty slots
                        smast[j] = 0 
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
                if smast_empty >= 2 and ast_list[i] == 0: #Checks to see if there are two missing small asteroids and 1 big asteroid 
                    smast_empty -= 2 #If so, count down empty slots and activate the respawn count for that asteroid
                    ast_respawn_count[i] += 1
                        
                elif ast_respawn_count[i] > 0 and ast_respawn_count[i] < ast_respawn_max and ast_list[i] == 0: #If the asteroid respawn count has been activated, the regen count is less then the max time,
                                                                                                                #and the current asteroid slot is empty, then increment the respawn count by 1
                    ast_respawn_count[i] += 1
                        
                elif ast_respawn_count[i] == ast_respawn_max and ast_list[i] == 0: #If the respan count reaches the limit and the current asteroid slot is empty, create a new asteroid and reset the count for that asteroid to 0
                    ast[i] = mod.LvObjMOD.Asteroid(screen.get_size(), P1_list, P2_list)
                    ast_list[i] = ast[i].get_ast()
                    ast_respawn_count[i] = 0

                i+=1

            winner[0] = Player_1.win_game(Player_2.game_over())
            winner[1] = Player_2.win_game(Player_1.game_over())
            
            P1_list = Player_1.get_player() #Retrieves player sprite and rectangle positions and puts them in a list
            P2_list = Player_2.get_player()


            i = 0
            j = 0
            while i < 3: #Grabs info about the big asteroids
                if ast_list[i] != 0:
                    ast_list[i] = ast[i].get_ast()
                i += 1
                    
            while j < 6: #Grabs info about the small asteroids
                if smast_list[j] != 0:
                    smast_list[j] = smast[j].get_ast()
                if smast_list[j+1] != 0:
                    smast_list[j+1] = smast[j+1].get_ast()
                j += 2
           
            screen.update(P1_list, P2_list, P1_Laser, P2_Laser, WallList, ast_list, smast_list, beam_info, winner) #Updates each object's position on the screen
            
            if winner[0] or winner[1]:
                option = self.restart_quit()
                if option != None:
                    pygame.display.quit()
                    return option
                
            clock.tick(60) #Limits game to 60 FPS
        pygame.quit() #Closes the window and quits the game

    def Lvl_2(self): #Teleporter level
        
        #GREEN = (113,243,65) #color for debug wall
        #WALL_AMOUNT = 6 #how many walls
        pygame.init()
        
        screen = mod.ScrMOD.Screen(self.lvlnum) #Inits the display screen
        
        Player_1 = mod.PlrMOD.Player(150) #Inits player 1
        Player_2 = mod.PlrMOD.Player(150) #Inits player 2
        Player_1.init_player(1) #Inits player 1 specific data
        Player_2.init_player(2) #Inits player 2 specific data

        WallList = [0] * 6 #creates list for all walls based on wall amount constant
        #middle walls
        WallList[0] = mod.LvObjMOD.Wall(550, 0, 50, 650, True, screen)
        WallList[1] = mod.LvObjMOD.Wall(0, 300, 1200, 50, False, screen)
        #top and bottom
        WallList[2] = mod.LvObjMOD.Wall(0, 0, 1200, 50, False, screen)
        WallList[3] = mod.LvObjMOD.Wall(0, 600, 1200, 50, False, screen)
        #left and right
        WallList[4] = mod.LvObjMOD.Wall(0, 0, 50, 650, True, screen)
        WallList[5] = mod.LvObjMOD.Wall(1104, 0, 50, 650, True, screen)

        clock = pygame.time.Clock() #Used for managing how fast the screen updates
        done = False #Flag for closing the game (if user presses X)
        Player_1.send_screen(screen.get_size())
        Player_2.send_screen(screen.get_size())
        P1_list = Player_1.get_player() #Retrieves player sprite and rectangle positions and puts them in a list
        P2_list = Player_2.get_player()
        ast_list = [0]*3
        smast_list = [0]*6
        beam_info = [0]*5
        winner = [0]*2
   
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
            if Player_1.checkHit(P2_Laser, False): #Checks to see if a player collided with a player/satellite's laser or an asteroid
                P2_Laser = Player_2.destroy_laser() #Destroy the incoming laser if so
                
            if Player_2.checkHit(P1_Laser, False):
                P1_Laser = Player_1.destroy_laser()

            Player_1.checkCollision(WallList)
            Player_2.checkCollision(WallList)

            if Player_1.checkLaserCollision(WallList):
                P1_Laser = Player_1.destroy_laser()
                
            if Player_2.checkLaserCollision(WallList):
                P2_Laser = Player_2.destroy_laser()

            winner[0] = Player_1.win_game(Player_2.game_over())
            winner[1] = Player_2.win_game(Player_1.game_over())
                
            P1_list = Player_1.get_player() #Retrieves player sprite and rectangle positions and puts them in a list
            P2_list = Player_2.get_player()
           
            screen.update(P1_list, P2_list, P1_Laser, P2_Laser, WallList, ast_list, smast_list, beam_info, winner) #Updates each players position on the screen
            
            if winner[0] or winner[1]:
                option = self.restart_quit()
                if option != None:
                    pygame.display.quit()
                    return option
           # print("Reaches end")
            clock.tick(60) #Limits game to 60 FPS
        pygame.quit() #Closes the window and quits the game  

    def Lvl_3(self): #Satellites level
        
        COLOR = (0, 0, 0) #color for debug wall
        WALL_AMOUNT = 3 #how many walls
        pygame.init()
        
        screen = mod.ScrMOD.Screen(self.lvlnum) #Inits the display screen
        
        Player_1 = mod.PlrMOD.Player(300) #Inits player 1
        Player_2 = mod.PlrMOD.Player(300) #Inits player 2
        Player_1.init_player(1) #Inits player 1 specific data
        Player_2.init_player(2) #Inits player 2 specific data

        WallList = [0] * WALL_AMOUNT #creates list for all walls based on wall amount constant

        clock = pygame.time.Clock() #Used for managing how fast the screen updates
        done = False #Flag for closing the game (if user presses X)
        Player_1.send_screen(screen.get_size())
        Player_2.send_screen(screen.get_size())
        P1_list = Player_1.get_player() #Retrieves player sprite and rectangle positions and puts them in a list
        P2_list = Player_2.get_player()
        ast_list = [0]*3
        smast_list = [0]*6
        beam_info = [0]*5
        beam = mod.LvObjMOD.Beam(screen.get_size())
        winner = [0]*2
   
    #Game Loop
        while not done:
            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True #Sets flag for quitting the game
         
        #Game logic

            #game_over = Player_1.Game_Over()
            #game_over = Player_2.Game_Over()             
                  
            #Movement
            Player_1.movement()#Player 1 movement function
            Player_2.movement()#Player 2 movement function

            P1_Laser = Player_1.shoot_laser()#Checks to see if player shoots this frame
            P2_Laser = Player_2.shoot_laser()
                        
            beam_info = beam.rotate()
        #Screen wrapping
            Player_1.screen_wrap() #Screen Wrapping for P1
            Player_2.screen_wrap() #Screen wrapping for P2
            
        #Screen-clearing + Drawing
            if Player_1.checkHit(P2_Laser, False): #Checks to see if a player collided with a player/satellite's laser or an asteroid
                P2_Laser = Player_2.destroy_laser() #Destroy the incoming laser if so
                
            if Player_2.checkHit(P1_Laser, False):
                P1_Laser = Player_1.destroy_laser()            

            Player_1.checkHit(beam.get_mask(), True)
            Player_2.checkHit(beam.get_mask(), True)

            winner[0] = Player_1.win_game(Player_2.game_over())
            winner[1] = Player_2.win_game(Player_1.game_over())
           # print(winner[0])
            P1_list = Player_1.get_player() #Retrieves player sprite and rectangle positions and puts them in a list
            P2_list = Player_2.get_player()
           
            screen.update(P1_list, P2_list, P1_Laser, P2_Laser, WallList, ast_list, smast_list, beam_info, winner) #Updates each players position on the screen

            if winner[0] or winner[1]:
                option = self.restart_quit()
                if option != None:
                    pygame.display.quit()
                    return option
           # print("Reaches end")
            clock.tick(60) #Limits game to 60 FPS
        pygame.quit() #Closes the window and quits the game


    def restart_quit(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_r]:
            return True
        if key[pygame.K_q]:
            return False
