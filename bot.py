import pygame
import numpy as np
import pygame.freetype
import librosa
import librosa.display
import matplotlib.pyplot as plt
import random

import matplotlib.cm as cm

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Music-Driven Art Visualizer')
music_file = 'Tax Evasion.mp3'
y, sr = librosa.load(music_file)
D = np.abs(librosa.stft(y))
S = librosa.amplitude_to_db(D, ref=np.max)
y_harmonic, y_percussive = librosa.effects.hpss(y)

S_color = cm.viridis((S - S.min()) / (S.max() - S.min()))

#print(S_color)

pygame.mixer.music.load(music_file)
pygame.mixer.music.play(-1)

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

running = True
clock = pygame.time.Clock()

waveform_change_y = 0
waveform_change_x = 0

cooldown = 50

last = pygame.time.get_ticks()

while running:
    #print(beat_times)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    now = pygame.time.get_ticks()

    if now - last >= cooldown:
        last = now
        #waveform_change_y = random.randint(10, 800)
        #waveform_change_x = random.randint(10, 500)
        if waveform_change_x > 800:
            pass
        else:
            waveform_change_y += 1
            waveform_change_x += 1


    screen.fill((0, 0, 0))



    frame = pygame.surfarray.make_surface(S_color[:waveform_change_x, :waveform_change_y, :3] * 255)
    frame = pygame.transform.scale(frame, (width, height))


    screen.blit(frame, (0, 0))


    pygame.display.flip()


    clock.tick(30)


pygame.quit()
