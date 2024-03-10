import pygame
import numpy as np
import pygame.freetype
import librosa
import librosa.display
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Music-Driven Art Visualizer')
music_file = 'Tax Evasion.mp3'

y, sr = librosa.load(music_file)
D = np.abs(librosa.stft(y))
S = librosa.amplitude_to_db(D, ref=np.max)  

colormaps = list(plt.colormaps())
random_colormap = random.choice(list(plt.colormaps()))

#S_color = cm(random_colormap)((S - S.min()) / (S.max() - S.min()))
random_colormap_generator = getattr(cm, random_colormap)
colormap_generator_caller = random_colormap_generator((S - S.min()) / (S.max() - S.min()))
S_color = colormap_generator_caller



pygame.mixer.music.load(music_file)
pygame.mixer.music.play(-1)

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

running = True
clock = pygame.time.Clock()

waveform_change_y = 800
waveform_change_x = 0

steps = 50

last = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    now = pygame.time.get_ticks()

    if now - last >= steps:

        last = now

        if waveform_change_x >= 800:
            waveform_change_y = 400
            waveform_change_x = 800
        else:
            waveform_change_y -= 1
            waveform_change_x += 1

    screen.fill((0, 0, 0))


    frame = pygame.surfarray.make_surface(S_color[:waveform_change_x, :waveform_change_y, :3] * 255)
    frame = pygame.transform.scale(frame, (width, height))


    screen.blit(frame, (0, 0))


    pygame.display.flip()


    clock.tick(10)


pygame.quit()
