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

# evaluation function
def evaluation (target, choice):
    value = 0
    for i in range(110):
        for j in range(77):
            value += target[i][j]-choice[i][j]
    return value

# selection
def selection(old_population, new_population):
    fitness = [0] * len(old_population)
    target = getImage()
    for i in range(len(old_population)-1):
        fitness[i] = evaluation(target, old_population[i])

    # sorting acc. to fitness value
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(fitness) - 1):
            if fitness[i] > fitness[i + 1]:
                # Swaping the elements
                fitness[i], fitness[i + 1] = fitness[i + 1], fitness[i]
                old_population[i], old_population[i+1] = old_population[i+1], old_population[i+1]
                # Set the flag to True so we'll loop again
                swapped = True

    for m in range(50):
        new_population[m] = old_population[m]

# cross over
def crossOver(old_population, new_population):
    for i in range(20):
        t = random.randint(0,20)



t = createPopulation(5)
t2 =  getImage()
t3 = evaluation(t2,t[1])
print (t3)
