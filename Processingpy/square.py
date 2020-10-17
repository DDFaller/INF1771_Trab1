from squareTypes import squareTypes
from AValues import AValues
class square:
    def __init__(self,board,squareType,position):
        self.squareType = squareType
        self.position = position
        self.knights = []
        self.AValues = AValues()

    def GetSquareType(self):
        return self.squareType

    def GetPosition(self):
        return self.position

    def GetKnights(self):
        return self.knights

    def GetGValue(self):
        if not self.squareType in squareTypes.CASA:
            return int(self.squareType)
        return squareTypes.MOUNTAIN

    def Display(self,blockSize,offsetx, offsety):
        BLACK = (80,80,80)
        GREY = (173,173,173)
        WHITE =(222,222,222)
        rectColor = (0,0,0)
        if self.squareType == squareTypes.MOUNTAIN:
            rectColor = BLACK
        if self.squareType == squareTypes.ROCKY:
            rectColor = GREY
        if self.squareType == squareTypes.PLANE:
            rectColor = WHITE
        fill(rectColor[0],rectColor[1],rectColor[2])
        rect(self.position[0] * blockSize + offsetx/2,self.position[1] * blockSize + offsety/2,blockSize,blockSize)
