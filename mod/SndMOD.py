import pygame
import os

class snd:
    def __init__(self, volume):
        self.volume = volume
        
    def Laser(self):
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.load(os.path.join('snd','laser.wav'))
        pygame.mixer.music.play()

    def Explode(self):
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.load(os.path.join('snd','explode.wav'))
        pygame.mixer.music.play()

    def Respawn(self):
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.load(os.path.join('snd','respawn.wav'))
        pygame.mixer.music.play()

    def AstExplode(self):
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.load(os.path.join('snd','ast_explode.wav'))
        pygame.mixer.music.play()

    def Teleporter(self):
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.load(os.path.join('snd','teleport.wav'))
        pygame.mixer.music.play()

    def Beam(self):
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.load(os.path.join('snd','teleport.wav'))
        pygame.mixer.music.play()
