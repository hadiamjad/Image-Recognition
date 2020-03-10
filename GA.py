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
    return random.randint(0, 256)


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
def evaluation(target, choice):
    value = 0
    for i in range(110):
        for j in range(77):
            value += target[i][j] - choice[i][j]
    return value


# selection
def selection(old_population, new_population, target, fittest):
    fitness = [0] * len(old_population)
    for i in range(len(old_population) - 1):
        fitness[i] = evaluation(target, old_population[i])

    # sorting acc. to fitness value
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(fitness) - 1):
            if fitness[i] > fitness[i + 1]:
                # Swaping the elements
                fitness[i], fitness[i + 1] = fitness[i + 1], fitness[i]
                old_population[i], old_population[i + 1] = old_population[i + 1], old_population[i + 1]
                # Set the flag to True so we'll loop again
                swapped = True

    fittest[0] = evaluation(target, old_population[0])
    for m in range(50):
        new_population.append(old_population[m])


# cross over
def crossOver(old_population, new_population, target, fittest):
    for i in range(20):
        t = random.randint(0, 50)
        m = old_population[t]
        t2 = random.randint(0, 50)
        m2 = old_population[t2]

        i = 0
        while i < 110:
            for j in range(77):
                m[i][j], m2[i][j] = m2[i][j], m[i][j]
            i = i + 2

        if fittest[0] > evaluation(target, m):
            fittest[0] = evaluation(target, m)
        elif fittest[0] > evaluation(target, m2):
            fittest[0] = evaluation(target, m2)
        new_population.append(m)
        new_population.append(m2)


# mutation
def mutation(old_population, new_population, target, fittest):
    for i in range(10):
        t = random.randint(0, 50)
        m = old_population[t]
        for i in range(110):
            for j in range(77):
                m[i][j] = abs(255 - m[i][j])

        if fittest[0] > evaluation(target, m):
            fittest[0] = evaluation(target, m)
        new_population.append(m)


# GA
def GeneticAlgorithm(generations):
    old_population = createPopulation(100)
    new_population = []

    target = getImage()
    fittest = [0]

    i = 0
    while i < generations and fittest != 0:
        selection(old_population, new_population, target, fittest)
        crossOver(old_population, new_population, target, fittest)
        mutation(old_population, new_population, target, fittest)
        print("Generation " + str(i) + " Fittest: " + str(fittest))
        i = i + 1
        old_population = new_population
        new_population = []


GeneticAlgorithm(1000)
