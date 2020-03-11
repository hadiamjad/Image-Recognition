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


def saveImage(individual, experiment, imgnum):
    cv2.imwrite("D:\\Academics\\Semester 6\\Artificial Intelligence\\Assignment 3\\17L-4243 & 17L-4280\\exp" + str(experiment) + "_img" + str(imgnum) + ".png", individual.getPop())


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
    for i in range(70):
        t = np.random.randint(0, 20)
        m = old_population[t:t+1]
        t2 = np.random.randint(0, 20)
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
        t = np.random.randint(0, 20)               # pick a random member of the population
        m = old_population[t:t+1]
        row = np.random.randint(0, 110)            # random selection of a pixel
        col = np.random.randint(0, 77)
        p = m[0].getPop()
        p[row][col] = np.random.randint(0, 256)
        ind = Chromosome(0, p)
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
    imgnum = 1
    while accuracy < 99.0:
        fittest, best_old = selection(old_population, target)
        new_population.extend(best_old)
        new_population.extend(crossOver(old_population))
        # new_population.extend(crossover)
        new_population.extend(mutation(old_population))
        if fittest < maxfit:
            accuracy = ((init_cost - maxfit)/init_cost) * 100
            print("Generation " + str(i) + " Fittest: " + str(fittest) + " Accuracy: " + str(accuracy))
            maxfit = fittest
        if i % 25000 == 0:
            saveImage(old_population[0], 3, imgnum)
            imgnum += 1
        i += 1
        old_population = new_population
        new_population = []
        crossover = []
    saveImage(old_population[0], 2, imgnum)


GeneticAlgorithm()
