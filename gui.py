import pygame
from tkinter import *
from PIL import ImageTk, Image

class GUI(object):
     def __init__(self):
          self.window = Tk()
          self.window.geometry("500x250")
          self.window.title("Space Raiders")

          self.player1 = ""
          self.player2 = ""
          
          self.p1 = Label(self.window, text='Player 1: ')
          self.p1Entry = Entry(self.window)
          self.p2 = Label(self.window, text='Player 2: ')
          self.p2Entry = Entry(self.window)

          self.map = Canvas(self.window, width=175, height=100)
          self.map2 = Canvas(self.window, width=175, height=100)
          
          img = ImageTk.PhotoImage(Image.open("map.png")) #update to correct maps
          img2 = ImageTk.PhotoImage(Image.open("map.png")) #waiting on maps to be finished
          self.map.create_image(175,100, image=img)
          self.map2.create_image(175,100, image=img2)

          self.subButton = Button(self.window, text='Submit', width=10, command=self.submit)
          self.quitButton = Button(self.window, text='Cancel', width=10, command=self.window.destroy)

          self.getPlayers()
          self.widgetAllign()
          mainloop()
     
     def submit(self):
          self.player1 = str(self.p1Entry.get())  ## add selected map
          self.player2 = str(self.p2Entry.get())

     def getPlayers(self):
          return self.player1, self.player2

     def widgetAllign(self):
          self.window.columnconfigure(0, weight=0)
          self.window.rowconfigure(0, weight=0)
          self.window.columnconfigure(2, weight=1)
          self.p1.grid(row=0, column=0)
          self.p1Entry.grid(row=0, column=1)
          self.p2.grid(row=1, column=0)
          self.p2Entry.grid(row=1, column=1)
          self.map.grid(row=0, column=8, columnspan=2, rowspan=3, padx=10)
          self.map2.grid(row=5, column=8, columnspan=2, rowspan=3, padx=10)

          self.subButton.grid(row=8, column=0, padx=10)
          self.quitButton.grid(row=8, column=1)

#gui = GUI()
#gui.getPlayers()   #---- To get player data
#p1 = gui.player1
#p2 = gui.player2
#print(p1 + " " +p2)


