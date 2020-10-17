from knightTypes import knightTypes


class athenaKnight:
    def __init__(self,knightType,name,cosmicPower,energyPoint):
        self.name = name
        self.cosmicPower = cosmicPower
        self.type = knightType
        self.energyPoints = energyPoint
        self.position = (0,0)
        self.restTime = 0

    def CalculateTimeToDefeat(self,knights):
        if self.energyPoints == 0:
            return 0
        sum = 0.0
        for knight in knights:
            sum += knight.cosmicPower
        return self.cosmicPower/sum

    def Defeat(self,knights):
        if len(knights) == 0:
            return False

        time = self.CalculateTimeToDefeat(knights)
        if time == 0:
            return True
        self.energyPoints -= 1
        for knight in knights:
            knight.energyPoints -= 1
            knight.restTime += time
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
