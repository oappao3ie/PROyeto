import pygame
import noise
import time
import vector

gridSizeX = 100
gridSizeY = 100

windowX = 500
windowY = 500

gridSizeRatioX = windowX / gridSizeX

image = noise.generateNoiseImage(gridSizeX, gridSizeY, 16)
roadImage = noise.generateRoadImage(gridSizeX, gridSizeY, 25, 200)

window = pygame.display.set_mode((windowX, windowY))
clock = pygame.time.Clock()

for x in range(gridSizeX):
    for y in range(gridSizeY):

        value1 = image[x][y]
        value2 = roadImage[x][y]

        sea = value1 < 0.18
        selColor = (0, 0, 0)

        if sea:
            value2 = 0

        value = min(max(value1 + value2, 0), 1)

        if sea:
            selColor = (0, 0, 255)

        colorValue = selColor

        pygame.draw.rect(window, colorValue, (x*gridSizeRatioX, y*gridSizeRatioX, gridSizeX, gridSizeY))

pygame.display.update()

time.sleep(4)