import numpy as np
import cv2
from numpy import random
import copy

class Chromosome:
    def __init__(self, fitness, pop):
        self.fitness = fitness
        self.pop = pop

    def setFitness(self, fitness):
        self.fitness = fitness

    def getPop(self):
        return self.pop

    def getFitness(self):
        return self.fitness



    def __lt__(self, other):
        flag = False
        if self.fitness < other.fitness:
            flag = True
        return flag

    def __gt__(self, other):
        flag = False
        if self.fitness > other.fitness:
            flag = True
        return flag


# function to get image
# returns 2D array of pixels
def getImage():
    img = cv2.imread('imageB.bmp', 0)
    temp = np.array(img)
    return temp


# random number generator
def randomNumber():
    return np.random.randint(0, 255)       # return value in [low,high)


# it generates random population of size 'n'
def createPopulation(n):
    population = []

    for k in range(n):
        x = np.random.randint(0, 256, (110, 77))        # generate random numbers in [low, high)
        c = Chromosome(0, x)
        population.append(c)

    return population

# evaluation function
def evaluation(target, choice):

    value = np.sum(np.abs(np.subtract(target, choice)))
    return value


# selection
def selection(old_population, new_population, target):

    for i in range(len(old_population)):
        old_population[i].setFitness(evaluation(target, old_population[i].getPop()))

    old_population.sort(key=lambda individual: individual.fitness)
    fittest = old_population[0].getFitness()

    for m in range(10):
        new_population.append(copy.deepcopy(old_population[m]))
    return fittest


# cross over
def crossOver(old_population, new_population):
    for i in range(40):
        t = np.random.randint(0, 100)
        m = old_population[t].getPop()
        t2 = np.random.randint(0, 100)
        m2 = old_population[t2].getPop()

        i = 0
        while i < 110/2:
            for j in range(77):
                m[i][j], m2[109-i][j] = m2[109-i][j], m[i][j]
            i += 1

        new_population.append(copy.deepcopy(old_population[t]))
        new_population.append(copy.deepcopy(old_population[t2]))


# mutation
def mutation(old_population, new_population):
    for i in range(100):
        t = np.random.randint(0, 100)               # pick a random member of the population
        m = old_population[t].getPop()
        k = random.randint(0, 10)
        if k < 10:
            row = np.random.randint(0, 110)            # random selection of a pixel
            col = np.random.randint(0, 77)
            m[row][col] = np.random.randint(0, 256)
            new_population.append(copy.deepcopy(old_population[t]))


# GA
def GeneticAlgorithm():
    old_population = createPopulation(100)
    new_population = []

    target = getImage()
    fittest = -1
    maxfit = 9999999

    i = 0
    while maxfit != 0:
        fittest = selection(old_population, new_population, target)
        crossOver(old_population, new_population)
        mutation(old_population, new_population)
        if fittest < maxfit:
            print("Generation " + str(i) + " Fittest: " + str(fittest))
            maxfit = fittest
        i += 1
        old_population = new_population
        new_population = []


GeneticAlgorithm()
