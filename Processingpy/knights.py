from knightTypes import knightTypes
from math import ceil

class athenaKnight:
    def __init__(self,knightType,name,cosmicPower,energyPoint):
        self.name = name
        self.cosmicPower = cosmicPower
        self.type = knightType
        self.energyPoints = energyPoint
        self.position = (0,0)
        self.restTime = 0
        self.battle = False

    def __hash__(self):
        return hash(self.name)

    def CalculateTimeToDefeat(self,knights):
        #print("Boss:" + self.name )
        #[print(x.name) for x in knights]
        if self.energyPoints == 0:
            return 0
        sum = 0.0
        for knight in knights:
            sum += knight.cosmicPower
        if sum == 0:
            input("Travo")
        return self.cosmicPower/sum

    def Defeat(self,knights):
        if len(knights) == 0:
            return
        print(self.name + " Vs. " )
        for knight in knights:
            print(knight.name + ",")
        time = self.CalculateTimeToDefeat(knights)

        self.battle = True
        self.energyPoints -= 1
        for knight in knights:
            knight.energyPoints -= 1
            knight.restTime += ceil(time)
        return True

    def GetName(self):
        return self.name

    def GetCosmicPower(self):
        return self.cosmicPower

    def GetPosition(self):
        return self.position[0],self.position[1]

    def Move(self,movement):
        x = movement[0]
        y = movement[1]
        if self.position[0] == 0 and x < 0:
            return False
        if self.position[0] == 41 and x >0:
            return False
        if self.position[1] == 0 and  y < 0:
            return False
        if self.position[1] == 41 and y > 0:
            return False
        self.position = (self.position[0] + x, self.position[1] + y)

        return True

    def WriteFile(self):
        return self.name
