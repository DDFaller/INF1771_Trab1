from squareTypes import squareTypes
class square:
    def __init__(self,board,squareType,position):
        self.squareType = squareType
        self.position = position
        self.knights = []

    def GetSquareType(self):
        return self.squareType

    def GetPosition(self):
        return self.position

    def GetKnights(self):
        return self.knights
    
    def Display(self,blockSize):
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
        rect(self.position[0] * blockSize,self.position[1] * blockSize,blockSize,blockSize)
        fill(rectColor[0],rectColor[1],rectColor[2])
