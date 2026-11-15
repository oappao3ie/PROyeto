from random import random, randint
import math

def lerp(a, b, x):
    return a + x * (b-a)

def generateNoiseImage(width, height, samplePointCount = 10):

    imageMap = [[0 for _ in range(height)] for _ in range(width)]

    samplePoints = [[randint(0, width-1), randint(0, height-1), random()] for _ in range(samplePointCount)]

    for SP in samplePoints:

        value = SP[2]
        pX = SP[0]
        pY = SP[1]

        imageMap[pX][pY] = value

    for x in range(width):
        for y in range(height):

            weightedSum = 0.0
            totalWeight = 0.0

            for pX, pY, value in samplePoints:
                dist = math.hypot(pX - x, pY - y)

                if dist == 0:
                    weightedSum = value
                    totalWeight = 1.0
                    break

                weight = 1.0 / (dist)
                weightedSum += value * weight
                totalWeight += weight

            imageMap[x][y] = weightedSum / totalWeight

    return imageMap

                
