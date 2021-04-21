#Kevin Andor, Cole Keffel, Cole Stewart
#Final Project CSC308
#Space Raiders

LIGHTPURPLE = (153, 0, 153) #colors for wall
WALL_AMOUNT = 3 #how many walls

import pygame
import mod.PlrMOD #Imports the module containing player-related classes
import mod.ScrMOD #Imports the module containing display-related classes
import mod.LvObjMOD #Imports the module containing Level object classes, such as hazards and walls
import mod.LvMOD #Imports the module containing the different map layouts in the game
def main():
    game = mod.LvMOD.Level(3)
main() #Calls the main function
