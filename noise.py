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

            avgDist = 0
            valueT = 0

            for SP in samplePoints:

                value = SP[2]
                pX = SP[0]
                pY = SP[1]

                imageMap[pX][pY] = value

                dist = math.sqrt((pX - x) ** 2 + (pY - y) ** 2)

                avgDist = dist
                valueT = value

            linearDist = avgDist / (width + height)

            newPixelVal = lerp(valueT, 1, linearDist)

            newPixelVal = min(1, newPixelVal)

            imageMap[x][y] = newPixelVal

    return imageMap

                
