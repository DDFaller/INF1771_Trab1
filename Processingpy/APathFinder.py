from squareTypes import squareTypes
from board import board



class APathFinder:
    def __init__(self,board):
        self.board = board
        self.openPath = []
        self.closedPath = []
        self.path = []
        self.showing = True
        self.breakpoints = []

    def FindPath(self,breakpoints):
        self.openPath.append(self.board.initialSquare)
        breakpoints.append(self.board.finalSquare.position)
        self.breakpoints = breakpoints

    def SetPath(self,path):
        self.path = path

    def GetNeighbors(self,x,y):
        squaresAround = []
        if x >= 0 and x < 42:
            if y >= 0 and y < 42:
                squaresAround.append(self.board.GetSquare(x- 1,y))
                squaresAround.append(self.board.GetSquare(x + 1,y))
                squaresAround.append(self.board.GetSquare(x,y - 1))
                squaresAround.append(self.board.GetSquare(x,y + 1))

        for i in range(len(squaresAround)-1,-1,-1):
            if squaresAround[i] == None:
                squaresAround.remove(squaresAround[i])
        return squaresAround

    def GeneratePath(self):
        if len(self.openPath) == 0:
            return False

        winnerIndex = 0
        for i in range(0,len(self.openPath)):
            if self.openPath[i].AValues.f < self.openPath[winnerIndex].AValues.f:
                winnerIndex = i
        current = self.openPath[winnerIndex]

        if current.position == self.board.finalSquare.position:
            path = []
            temp = current
            while(not(temp.AValues.previous == None)):
                path.append(temp.AValues.previous)
                temp = temp.AValues.previous

            self.SetPath(path)
            for elem in path:
                if elem.position in self.breakpoints:
                    print(elem)
            print("Done")

        self.RemoveOpenPath(current)
        self.closedPath.append(current)

        for neighbor in self.GetNeighbors(current.position[0],current.position[1]):

            if not(neighbor in self.closedPath) and not(neighbor.squareType == squareTypes.MOUNTAIN):
                tempG = current.AValues.g + neighbor.squareType

                betterPath = False
                if neighbor in self.openPath:
                    if tempG < neighbor.AValues.g:
                        neighbor.AValues.g = tempG
                        betterPath = True
                else:
                    betterPath = True
                    neighbor.AValues.g = tempG
                    self.openPath.append(neighbor)

                if betterPath:
                    #Maybe resolve using square position instead of closedSet
                    nextBreakpoint = self.breakpoints[:]#Copy of breakpoints
                    for pos in self.breakpoints:
                        if pos in self.closedPath:
                            nextBreakpoint.remove(pos)

                    neighbor.AValues.h = neighbor.AValues.heuristic(neighbor.position,nextBreakpoint)
                    neighbor.AValues.f = neighbor.AValues.g + neighbor.AValues.h
                    neighbor.AValues.SetPrevious(current)

    def RemoveOpenPath(self,current):
        for i in range(len(self.openPath) -1,-1,-1):
            if self.openPath[i] == current:
                self.openPath.remove(self.openPath[i])

    def DecideNextMove(self,square):
        index = self.path.index(square)
        if index + 1 < len(self.path):
            return self.path[index + 1]
        return self.path[index]

    def keyPressedListener(self,keyValue):
        if keyValue == "k":
            self.showing = not(self.showing)

    def Display(self,blockSize,offsetX,offsetY):
        self.GeneratePath()
        if self.showing:
            for square in self.closedPath:
                rect(offsetX/2 + blockSize * square.position[0],offsetY/2 + blockSize * square.position[1],blockSize,blockSize)
                fill(125,125,0)
            for square in self.openPath:
                rect(offsetX/2 + blockSize * square.position[0],offsetY/2 + blockSize * square.position[1],blockSize,blockSize)
                fill(0,125,125)
            for square in self.path:
                rect(offsetX/2 + blockSize * square.position[0],offsetY/2 + blockSize * square.position[1],blockSize,blockSize)
                fill(125,0,125)
