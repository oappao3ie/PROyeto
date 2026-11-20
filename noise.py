from random import random, randint
import math

strength = 0.25
def generateNoiseImage(width, height, samplePointCount = 10):

    imageMap = [[0 for _ in range(height)] for _ in range(width)]

    samplePoints = [[randint(0, width-1), randint(0, height-1), random()] for _ in range(samplePointCount)]

    for x in range(width):
        for y in range(height):

            weightedSum = 0.0
            totalWeight = 0.0

            distToCenter = math.hypot(width / 2 - x, height / 2 - y)

            if distToCenter == 0:
                distToCenter = 0.001

            for pX, pY, value in samplePoints:
                dist = math.hypot(pX - x, pY - y)

                fallOff = max(min(1.0 - (distToCenter / ((width + height) * strength)), 1), 0)

                if dist == 0:
                    weightedSum = value * fallOff
                    totalWeight = 1.0
                    break

                weight = 1.0 / (dist)
                weightedSum += value * weight * fallOff
                totalWeight += weight

            weightedSum = max(weightedSum, 0)

            imageMap[x][y] = weightedSum / totalWeight

    return imageMap

directions = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1]
]

class Drawer():
    def __init__(self, x, y, width, height):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.previousMovement = directions[randint(0, len(directions)-1)]

    def move(self, image):

        stepDir = directions[randint(0, len(directions)-1)]

        copiedMove = False
        if self.previousMovement:
            stepDir = self.previousMovement
            self.previousMovement = None
            copiedMove = True

        nextX = self.x + stepDir[0]
        nextY = self.y + stepDir[1]

        if nextX < 0 or nextX > self.width-1:
            return

        if nextY < 0 or nextY > self.height-1:
            return

        image[nextX][nextY] = 1

        if not copiedMove:
            self.previousMovement = stepDir

        self.x = nextX
        self.y = nextY
                
def generateRoadImage(width, height, sampleCount=1, iterations = 10):

    image = [[0 for _ in range(height)] for _ in range(width)]

    drawers = [Drawer(randint(0, width-1), randint(0, height-1), width, height) for _ in range(sampleCount)]

    for step in range(iterations):

        for drawer in drawers:
            
            drawer.move(image)

    return image

