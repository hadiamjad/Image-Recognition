import numpy as np
import cv2
import random

# function to get image
# returns 2D array of pixels
def getImage():
    img = cv2.imread('imageB.bmp', 0)
    temp = np.array(img)
    return temp

# random number generator
def randomNumber():
    return random.randint(0,256)

# it generates random population of size 'n'
def createPopulation(n):
    population = []

    for k in range(n):
        x = np.zeros((110, 77))
        for i in range(110):
            for j in range(77):
                x[i][j] = randomNumber()
        population.append(x)

    return population

t = createPopulation(5)
t2 =  getImage()
print (t2)