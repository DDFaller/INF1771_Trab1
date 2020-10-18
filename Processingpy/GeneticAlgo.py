from BronzeGroup import BronzeGroup
from random import *
from math import floor

class GeneticAlgo:
    def __init__(self):
        self.path = []
        self.bronzeKnights = None
        self.goldenKnights = None
        self.elementsInPopulation = 1000
        self.population = []
        self.matingPool = []
        self.generations = 0
        self.mutationRate = 0.3
        self.done = False

    def Initialize(self,path,bronzeKnights,goldenKnights):
        self.path = path
        self.bronzeKnights = bronzeKnights
        self.goldenKnights = goldenKnights
        self.GeneratePopulation()

    def Execute(self):
        if not(self.done):
            self.CalcFitness()
            self.NaturalSelection()
            self.Reproduction()
            self.Evaluate()

    def ShowFighters(self):
        for x in self.population:
            for y in x.fights:
                print(len(y))

    def GeneratePopulation(self):
        for index in range(0,self.elementsInPopulation):
            elemsList = []
            [elemsList.append([]) for x in range(0,12)]
            self.population.append(BronzeGroup(elemsList,self.bronzeKnights,self.goldenKnights))
            for fight in range(0,12):
                self.population[index].Generate(fight)
            self.population[index].UpdateOcurrences()
            self.population[index].EnsureKnightRules()
        print("Population generated")
        #for index in range(0,len(self.population)):
        #    print(len(self.population[index].fights[0]))

    def CalcFitness(self):
        for elem in self.population:
            elem.CalcFitness(300)

    def p5map(self,n, start1, stop1, start2, stop2):
        return ((n-start1)/(stop1-start1))*(stop2-start2)+start2

    def NaturalSelection(self):
        maxFitness = 0
        self.matingPool = []
        for elem in self.population:
            if elem.fitness > maxFitness:
                maxFitness = elem.fitness
        for index in range(0,len(self.population)):
            fitness = self.p5map(self.population[index].fitness,0,maxFitness,0,1)
            n = floor(fitness * 100)
            for x in range(0,n):
                self.matingPool.append(self.population[index])

    def Reproduction(self):
        for index in range(0,len(self.population)):
            a = randint(0,len(self.matingPool) -1)
            b = randint(0,len(self.matingPool) -1)
            parentA = self.matingPool[a]
            parentB = self.matingPool[b]
            child = parentA.Crossover(parentB)
            child.Mutate(self.mutationRate)
            self.population[index] = child
        self.generations += 1

    def Evaluate(self):
        if self.generations == 30:
            self.done = True
            print("Generations " + str(self.generations))
            self.CalcFitness()
