import pygame
import numpy as np
import pygame.freetype
import librosa
import librosa.display
import matplotlib.pyplot as plt
import matplotlib.cm as cm

pygame.init()


width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Music-Driven Art Visualizer')


music_file = 'Tax Evasion.mp3'
y, sr = librosa.load(music_file)


D = np.abs(librosa.stft(y))
S = librosa.amplitude_to_db(D, ref=np.max)

S_color = cm.viridis((S - S.min()) / (S.max() - S.min()))

pygame.mixer.music.load(music_file)
pygame.mixer.music.play(-1)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    frame = pygame.surfarray.make_surface(S_color[:, :800, :3] * 255)
    frame = pygame.transform.scale(frame, (width, height))
    screen.blit(frame, (0, 0))
    pygame.display.flip()

    clock.tick(30)

pygame.quit()
