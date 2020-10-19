from squareTypes import squareTypes
from BronzeGroup import BronzeGroup

class Agent:
    def __init__(self,goldenKnights,bronzeKnights,path,fightsSolution,endPosition):
        self.goldenKnights = goldenKnights
        self.bronzeKnights = bronzeKnights
        self.path = path
        self.bronzeGroup = fightsSolution
        self.fightsSolution = fightsSolution.fights
        self.blockedList = []
        self.currentCost = self.EstimatePathCost(path)
        self.endPosition = endPosition
        self.done = False
        self.count = 0
        print("path")
        for square in path:
            print(square.position)
        for index in range(0,len(bronzeKnights)):
            print("Index:" +str(index)+ " "+bronzeKnights[index].name )
        if self.fightsSolution[0][0] == self.bronzeKnights[1]:
            print(str("True"))

    def Reset(self):
        self.count = 0
        self.blockedList = []
        self.currentCost = self.EstimatePathCost(self.path)
        self.done = False

    def ShowKnightStats(self,index):
        knight = self.bronzeKnights[index]
        print("Rest time:" + str(knight.restTime))
        print("Position:" + str(knight.position))
        print("Energy Points:" + str(knight.energyPoints))
        for goldenKnight in self.goldenKnights:
            fightIndex = self.goldenKnights.index(goldenKnight)
            if knight.position == goldenKnight.position:
                print("Waiting for")
                for bronzeKnight in self.fightsSolution[fightIndex]:
                    if not bronzeKnight == knight:
                        print(bronzeKnight.name)

    def KnightInBattle(self,knight):
        for goldenIndex in range(0,len(self.goldenKnights)):
            if self.goldenKnights[goldenIndex].energyPoints == 1 and knight.position == self.goldenKnights[goldenIndex].position:
                if knight in self.fightsSolution[goldenIndex]:
                    return True
        return False

    def KnightsToBattleReady(self,index):
        for knightIndex in range(0,len(self.fightsSolution[index])):
            if not(self.fightsSolution[index][knightIndex].position == self.goldenKnights[index].position):
                return False
        return True

    def GetKnightUnready(self,index):
        for knight in self.fightsSolution[index]:
            if not (knight.position == self.goldenKnights[index].position):
                return  knight.position
        return None

    def GetDistantKnight(self,index):
        distantKnight = 0
        for knight in self.fightsSolution[index]:
            pos = knight.position
            endPosition = self.goldenKnights[index].position
            pathDistance = len(self.GetPath(pos,endPosition)) - 1 + knight.restTime
            if pathDistance > distantKnight:
                distantKnight = pathDistance
        return distantKnight

    def GetAwaitingFighters(self,index,knight):
        awaitingFighters = []
        for solutionKnight in self.fightsSolution[index]:
            if not knight == solutionKnight:
                if knight.position == solutionKnight.position and solutionKnight in self.blockedList:
                    awaitingFighters.append(solutionKnight)
        return awaitingFighters

    def GetGoldenKnightIndexInPos(self,position):
        for goldenKnightIndex in range(0,len(self.goldenKnights)):
            if self.goldenKnights[goldenKnightIndex].position == position:
                return goldenKnightIndex
        return -1

    def CheckVictory(self):
        for knight in self.bronzeKnights:
            if not(knight.position == self.endPosition):
                return False
        return True

    def ExecuteMovement(self):
        print("BlockedList")
        for knight in self.blockedList:
            print(knight.name)

        self.MoveKnights()
        self.CheckRoundBattles()


        for knight in self.bronzeKnights:
            if knight.restTime > 0:
                knight.restTime -= 1

        if self.CheckVictory():
            self.done = True
        else:
            if self.count % 5 ==0:
                print("Custo atual: "+ str(self.currentCost))
        self.count += 1

    def MoveKnights(self):
        for knight in self.bronzeKnights:
            if not knight.restTime > 0 and not self.KnightInBattle(knight):
                if knight in self.blockedList:
                    self.blockedList.remove(knight)
                movement = self.DecideNextMove(knight,self.path)
                if not movement[0] == None:
                    knight.Move(movement)

    def CheckRoundBattles(self):
        for knight in self.bronzeKnights:
            #Check if knight is in position of a golden knight
            if self.KnightInBattle(knight):
                #Get this golden knight position
                index = self.GetGoldenKnightIndexInPos(knight.position)
                #Check if all knights that should be in battle are in position
                if self.KnightsToBattleReady(index):
                    estimatedTime = self.goldenKnights[index].CalculateTimeToDefeat(self.fightsSolution[index])
                    for knight in self.fightsSolution[index]:
                        self.blockedList.append(knight)
                    self.currentCost += estimatedTime
                    self.goldenKnights[index].Defeat(self.fightsSolution[index])
                else:
                    for missingKnight in self.fightsSolution[index]:
                        if not missingKnight.position == knight.position:
                            #print("Waiting for: " + missingKnight.name )
                            pass
                    if not knight in self.blockedList:
                        self.blockedList.append(knight)
                        awaitingFighters = self.GetAwaitingFighters(index,knight)
                        if len(awaitingFighters) == 0:
                            waitingTime = self.GetDistantKnight(index)
                            knight.restTime = waitingTime
                            self.currentCost += waitingTime
                            print("Lost time: "+ str(waitingTime) + " current position: "+ str(knight.position))
                        else:
                            knight.restTime = awaitingFighters[0].restTime


    def GetPath(self,sourcePosition,endPosition):
        sourceIndex = 0
        endIndex = 0
        for squareIndex in range(len(self.path) - 1,-1,-1):
            if self.path[squareIndex].position == sourcePosition:
                sourceIndex = squareIndex
            if self.path[squareIndex].position == endPosition:
                endIndex = squareIndex
        return self.path[sourceIndex:endIndex - 1]

    def EstimatePathCost(self,path):
        sum = 0
        for square in path:
            if square.squareType == squareTypes.MOUNTAIN or square.squareType ==squareTypes.PLANE  or square.squareType == squareTypes.ROCKY :
                sum += square.squareType
        return sum

    def EstimateTime(self,path):
        return len(path)-1

    def DecideNextMove(self,knight,path):
        knightPos = knight.position
        goldenKnightIndex = self.GetGoldenKnightIndexInPos(knightPos)
        if not goldenKnightIndex == -1 and self.goldenKnights[goldenKnightIndex].energyPoints == 1:
            return (None,None)
        for squareIndex in range (len(path) - 1,-1,-1):
            if knightPos == path[squareIndex].position and not knightPos == path[0].position:
                nextSquarePos = path[squareIndex - 1]
                return (nextSquarePos.position[0] - knightPos[0],nextSquarePos.position[1] - knightPos[1] )

        return (None,None)
