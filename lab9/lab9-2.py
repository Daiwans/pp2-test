import pygame
from pygame.locals import *
import glob

pygame.mixer.init()
pygame.init()

music_files = glob.glob('загрузки/*.mp3')
current_track = 0
pygame.mixer.music.load(music_files[current_track])

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_p:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == K_s:
                pygame.mixer.music.stop()
            elif event.key == K_n:
                current_track = (current_track + 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_track])
                pygame.mixer.music.play()
            elif event.key == K_b:
                current_track = (current_track - 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_track])
                pygame.mixer.music.play()

pygame.quit()
