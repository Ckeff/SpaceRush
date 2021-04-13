import pygame
import tkinter as tk

pygame.init()
WIDTH, HEIGHT = 750, 750

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Rush")

BLACK = (0, 0, 0)
FPS = 60

def draw_window():
    WIN.fill(BLACK)
    pygame.display.update()


def draw_tk_window():
     window = tk.Tk()
     textBox = tk.Text()
     submit = Button()
     textBox.pack()
     window.mainloop()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()

    pygame.QUIT()

draw_tk_window()

if __name__ == "__main__":
     main()