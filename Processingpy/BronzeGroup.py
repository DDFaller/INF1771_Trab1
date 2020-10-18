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
        for bronze in self.bronzeKnights:
            if self.ocurrences[bronze] < lowestAssignment:
                lowestAssignment = self.ocurrences[bronze]
                lowestAssignedKnight = bronze
        return lowestAssignedKnight

    def GetAvailableKnights(self):
        availableKnights = []
        for bronze in self.bronzeKnights:
            if self.ocurrences[bronze] < 5:
                availableKnights.append(bronze)
        return availableKnights

    def GetMostAvailableKnight(self):
        availableKnights = []
        for bronze in self.bronzeKnights:
            if self.ocurrences[bronze] >= 5:
                return bronze

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

    def AddKnightRamdonly(self,index):
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

    def ChangeKnightRamdonly(self,index):
        self.RemoveKnightRamdonly(index)
        self.AddKnightRamdonly(index)

    def CheckForDuplicated(self):
        for fightIndex in range(0,12):
            knightsToRemove = {}
            for knightIndex in range(0,len(self.fights[fightIndex])):
                sum = 0
                knight = self.fights[fightIndex][knightIndex]
                if knight in knightsToRemove.keys():
                    continue
                for searchIndex in range(0,len(self.fights[fightIndex])):
                    if self.fights[fightIndex][searchIndex] == knight:
                        sum += 1
                if sum >= 2:
                    knightsToRemove[knight] = sum

            for k in knightsToRemove.keys():
                for i in range(knightsToRemove[k],1,-1):
                    for searchIndex in range(len(self.fights[fightIndex]) -1,-1,-1):
                        if self.fights[fightIndex][searchIndex] == k:
                            self.fights[fightIndex].pop(searchIndex)
                            self.ocurrences[k] -= 1

    def EnsureKnightRules(self):
        self.CheckForDuplicated()
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
            self.AddKnightRamdonly(knight)

    def Crossover(self, otherGroup):
        mergedList = []
        for x in range(0,12):
            if len(self.fights[x]) > len(otherGroup.fights[x]):
                minRange = len(otherGroup.fights[x])
            else:
                minRange = len(self.fights[x])

            midpoint = randint(0,minRange)

            #Midpoint in [0,len(self.fights) -1]

            #if len(otherGroup.fights[x]) > midpoint:
            #    crossoverList = self.fights[x][:midpoint] + otherGroup.fights[x][midpoint:]
            #else:
            #    crossoverList = otherGroup.fights[x][:midpoint] + self.fights[x][midpoint:]
            crossoverList = self.fights[x] + otherGroup.fights[x]
            mergedList.append(crossoverList)

            #print("\n \\=\\=\\=\\=\\=\\=\\=\\=\\=\\=\\=\\=\\=\\=\\=\\=\\=\\=\\=\\=\\=\\=\\=\\=")
            #print("Parent A => ")
            #for a in range(0,len(self.fights[x])):
            #    print(self.fights[x][a].name , end=",")
            #print("")
            #print("Parent B => ")
            #for b in range(0,len(otherGroup.fights[x])):
            #    print(otherGroup.fights[x][b].name , end=",")
            #print("")
            #print("Child => ")
            #for child in range(0,len(crossoverList)):
            #    print( crossoverList[child].name , end=",")
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
                case = randrange(0,1)
                if case > 0 and case < 0.33:
                    self.AddKnightRamdonly(fightIndex)
                elif case >= 0.33 and case <0.66:
                    self.RemoveKnightRamdonly(fightIndex)
                else:
                    self.ChangeKnightRamdonly(fightIndex)
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
        #Adicionar peso a cada casa
        #Simular jogada ideal
        #Computar cavaleiros por casa * peso da casa
        #[][][][][][][][][][][][]
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
