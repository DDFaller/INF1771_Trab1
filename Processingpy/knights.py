from knightTypes import knightTypes


class athenaKnight:
    def __init__(self,knightType,name,cosmicPower,energyPoint):
        self.name = name
        self.cosmicPower = cosmicPower
        self.type = knightType
        self.energyPoints = energyPoint
        self.position = (0,0)

    def CalculateTimeToDefeat(self,knights):
        sum = 0.0
        for knight in knights:
            sum += knight.cosmicPower
        return self.cosmicPower/sum

    def GetName(self):
        return self.name

    def GetCosmicPower(self):
        return self.cosmicPower

    def GetPosition(self):
        return self.position[0],self.position[1]
