#Kevin Andor, Cole Keffel, Cole Stewart
#Final Project CSC308
#Space Raiders

import mod.LvMOD #Imports the module containing the different map layouts in the game
import pygame
def main():
    game = mod.LvMOD.Level() #Inits the game
    restart = True
    while restart == True:
        restart = game.lvl_selector(2) #If player want to restart current level, returns True, else returns False


main() #Calls the main function
