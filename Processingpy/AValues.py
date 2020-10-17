
class AValues:
    def __init__(self):
        self.f = 0
        self.g = 0
        self.h = 0
        self.previous = None

    def heuristic(self,position,breakpointsList):
        lowestDistance = 1000
        for pos in breakpointsList:
            x = pos[0] - position[0]
            y = pos[1] - position[1]
            x = x**2
            y = y**2
            distance =(x + y)**(1/2)
            if distance < lowestDistance:
                lowestDistance = distance
        return lowestDistance

    def SetPrevious(self,previousSquare):
        self.previous = previousSquare
