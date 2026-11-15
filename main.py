import pygame
import noise
import time

gridSizeX = 25
gridSizeY = 25

windowX = 500
windowY = 500

gridSizeRatioX = windowX / gridSizeX

image = noise.generateNoiseImage(gridSizeX, gridSizeY, 4)

window = pygame.display.set_mode((windowX, windowY))
clock = pygame.time.Clock()

for x in range(gridSizeX):
    for y in range(gridSizeY):

        value = image[x][y]
        colorValue = (value * 255, value * 255, value * 255)

        pygame.draw.rect(window, colorValue, (x*gridSizeRatioX, y*gridSizeRatioX, gridSizeX, gridSizeY))

pygame.display.update()

time.sleep(4)