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
