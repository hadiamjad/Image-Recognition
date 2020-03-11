import numpy as np
import cv2
from numpy import random
import copy


init_cost = 9999999

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
    value = 0
    value = np.sum(np.abs(np.subtract(target, choice)))
    return value


# selection
def selection(old_population, target):
    global init_cost

    for i in range(len(old_population)):
        old_population[i].setFitness(evaluation(target, old_population[i].getPop()))

    old_population.sort(key=lambda individual: individual.fitness)
    fittest = old_population[0].getFitness()
    if init_cost == 9999999:
        init_cost = fittest

    return fittest, old_population[:20]


# cross over
def crossOver(old_population):
    crossover = []
    for i in range(60):
        t = np.random.randint(0, 50)
        m = old_population[t:t+1]
        t2 = np.random.randint(0, 50)
        m2 = old_population[t2:t2+1]
        p = m[0].getPop()
        p2 = m2[0].getPop()
        child = np.zeros((110, 77))
        child[:54][:76] = p[:54][:76]
        child[54:][:76] = p2[54:][:76]
        ind = Chromosome(0,child)
        crossover.append(ind)
    return crossover[:]


# mutation
def mutation(old_population):
    mutation = []
    for i in range(10):
        t = np.random.randint(0, 60)               # pick a random member of the population
        m = copy.copy(old_population[t].getPop())
        row = np.random.randint(0, 110)            # random selection of a pixel
        col = np.random.randint(0, 77)
        m[row][col] = np.random.randint(0, 256)
        ind = Chromosome(0, m)
        mutation.append(ind)
    return mutation


# GA
def GeneticAlgorithm():
    old_population = createPopulation(100)
    new_population = []
    crossover = []
    target = getImage()
    global init_cost
    fittest = -1
    maxfit = 999999
    accuracy = 0.0
    i = 0
    while accuracy < 99.0:
        fittest, best_old = selection(old_population, target)
        new_population.extend(best_old)
        crossover.extend(crossOver(old_population))
        new_population.extend(crossover)
        new_population.extend(mutation(crossover))
        if fittest < maxfit:
            accuracy = ((init_cost - maxfit)/init_cost) * 100
            print("Generation " + str(i) + " Fittest: " + str(fittest) + " Accuracy: " + str( accuracy))
            maxfit = fittest
        i += 1
        old_population = new_population
        new_population = []
        crossover = []


GeneticAlgorithm()
