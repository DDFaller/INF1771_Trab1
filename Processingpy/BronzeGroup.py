from random import randint,randrange


class BronzeGroup:
    def __init__(self,knightList,bronzeKnights,goldenKnights):
        self.goldenKnights = goldenKnights
        self.bronzeKnights = bronzeKnights
        self.fights = knightList# [12][0,5] bronze
        self.ocurrences = {}
        self.fitness = 1000
        for knight in bronzeKnights:
            self.ocurrences[knight] = 0

    def GetUnassignedKnight(self):
        lowestAssignment = 6
        lowestAssignedKnight = None
        for k,v in self.ocurrences.items():
            if v < lowestAssignment:
                lowestAssignment = v
                lowestAssignedKnight = k
        return lowestAssignedKnight

    def GetAvailableKnights(self):
        availableKnights = []
        for k,v in self.ocurrences.items():
            if v < 5:
                availableKnights.append(k)
        return availableKnights

    def GetMostAvailableKnight(self):
        availableKnights = []
        for k,v in self.ocurrences.items():
            if v >= 5:
                return k

    def RemoveKnightRamdonly(self,knight):
        positionsAvailable = []
        for fightIndex in range(0,12):
            if len(self.fights[fightIndex]) > 1 and knight in self.fights[fightIndex]:
                positionsAvailable.append(fightIndex)
        if len(positionsAvailable) == 0:
            return False

        randomIndex = positionsAvailable[randint(0,len(positionsAvailable) - 1)]
        self.fights[randomIndex].remove(knight)
        self.ocurrences[knight] -= 1
        return True

    def EnsureKnightRules(self):
        for k,v in self.ocurrences.items():
            #if v > 5:
            for i in range(v,5,-1):

                #Lowest Assigned Knight
                LessAssignedKnight = self.GetUnassignedKnight()

                if LessAssignedKnight == None or self.ocurrences[LessAssignedKnight] == 5:
                    if self.RemoveKnightRamdonly(k) == True:
                        return self.EnsureKnightRules()


                #Generate a index ramdonly to change the knight fight
                randIndex = randint(0,len(self.fights) - 1)
                while not(k in self.fights[randIndex]):
                    randIndex = randint(0,len(self.fights) -1)

                for knightIndex in range(0,len(self.fights[randIndex])):
                    if self.fights[randIndex][knightIndex] == k:
                        self.ocurrences[LessAssignedKnight] += 1
                        self.ocurrences[self.fights[randIndex][knightIndex]] -= 1
                        self.fights[randIndex][knightIndex] = LessAssignedKnight

        for fightIndex in range(0,12):
            if len(self.fights[fightIndex]) == 0:
                LessAssignedKnight = self.GetUnassignedKnight()

                if LessAssignedKnight == None or self.ocurrences[LessAssignedKnight] == 5:
                    if self.RemoveKnightRamdonly(self.GetMostAvailableKnight()) == True:
                        return self.EnsureKnightRules()

                self.fights[fightIndex].append(LessAssignedKnight)
                self.ocurrences[LessAssignedKnight] += 1

    def Generate(self,index):
        for knight in range(0,randint(1,5)):
            listOfKnights = self.GetAvailableKnights()
            if len(listOfKnights) == 0:
                return
            if len(listOfKnights) == 1:
                knightToAssign = listOfKnights[0]
            else:
                knightToAssign = listOfKnights[randint(0,len(listOfKnights) - 1)]
            while knightToAssign in self.fights[index] and len(listOfKnights) > 0:
                if len(listOfKnights) == 1:
                    knightToAssign = listOfKnights[0]
                else:
                    knightToAssign = listOfKnights[randint(0,len(listOfKnights) - 1)]
                listOfKnights.remove(knightToAssign)
            self.fights[index].append(knightToAssign)
            self.ocurrences[knightToAssign] += 1

    def Crossover(self, otherGroup):
        mergedList = []
        for x in range(0,12):
            midpoint = randint(0,len(self.fights[x]))

            #Midpoint in [0,len(self.fights) -1]
            crossoverList = []
            maxRange = 0
            minRange = 0
            if len(self.fights[x]) > len(otherGroup.fights[x]):
                maxRange = len(self.fights[x])
                minRange = len(otherGroup.fights[x]) -1
                a = otherGroup.fights[x]
                b = self.fights[x]
            else:
                maxRange = len(otherGroup.fights[x])
                minRange = len(self.fights[x]) -1
                a = self.fights[x]
                b = otherGroup.fights[x]

            for i in range(0,maxRange):
                if i < midpoint:
                    if i > minRange:
                        break
                    crossoverList.append(a[i])
                else:
                    crossoverList.append(b[i])

            #if len(otherGroup.fights[x]) > midpoint:
            #    crossoverList = self.fights[x][:midpoint] + otherGroup.fights[x][midpoint:]
            #else:
            #    crossoverList = otherGroup.fights[x][:midpoint] + self.fights[x][midpoint:]
            mergedList.append(crossoverList)

        generatedGroup = BronzeGroup(mergedList,self.bronzeKnights,self.goldenKnights)
        generatedGroup.UpdateOcurrences()
        generatedGroup.EnsureKnightRules()
        return generatedGroup

    def UpdateOcurrences(self):
        self.ocurrences = {}
        for fightIndex in range(0,len(self.fights)):
            for knight in self.fights[fightIndex]:
                if not knight in self.ocurrences.keys():
                    self.ocurrences[knight] = 0
                self.ocurrences[knight] += 1
        for knight in self.bronzeKnights:
            if not knight in self.ocurrences.keys():
                self.ocurrences[knight] = 0

    def Mutate(self,mutationRate):
        for fightIndex in range(0,len(self.fights)):
            if randrange(0,1) < mutationRate:
                knightIndex = randint(0,len(self.fights[fightIndex]) - 1)
                knights = list(self.ocurrences.keys())
                newKnight = knights[randint(0,len(knights) - 1)]
                self.ocurrences[self.fights[fightIndex][knightIndex]] -= 1
                self.ocurrences[newKnight] += 1
                self.fights[fightIndex][knightIndex] = newKnight
                self.EnsureKnightRules()

    def EstimateTime(self):
        sum = 0
        for fightIndex in range (0,len(self.fights)):
            goldenKnight = self.goldenKnights[fightIndex]
            if len(self.fights[fightIndex]) == 0:
                self.EnsureKnightRules()
            sum += goldenKnight.CalculateTimeToDefeat(self.fights[fightIndex])
        return sum

    def CalcFitness(self,target):
        score = self.EstimateTime()
        self.fitness = target/score
        if self.fitness > 1:
            print("Encontrou fitness otimizado score: " + str(score))
            #self.Show()


    def Show(self):
        for k,v in self.ocurrences.items():
            print(k.name + " ocurrences " + str(v) )
        for index in range(0,12):
            print("Contra: "+ str(self.goldenKnights[index].name) + " Time to defeat: " + str(self.goldenKnights[index].CalculateTimeToDefeat(self.fights[index])))
            for knight in self.fights[index]:
                print(knight.name)
            print("")
