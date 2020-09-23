from squareTypes import squareTypes
from square import square

class board:
    def __init__(self):
        self.boardGrid = []
        self.BuildBoard()

    def BuildBoard(self):
        for x in range(0,42):
            self.boardGrid.append([])
            for y in range(0,42):
                self.boardGrid[x].append(square(self,squareTypes.ROCKY,(x,y)))

        for index in range(0,50):
            bucket = int(random(0,2))
            if bucket == 0:
                self.boardGrid[int(random(0,42))][int(random(0,42))].squareType = squareTypes.MOUNTAIN
            if bucket == 1:
                self.boardGrid[int(random(0,42))][int(random(0,42))].squareType = squareTypes.PLANE
            if bucket == 2:
                self.boardGrid[int(random(0,42))][int(random(0,42))].squareType = squareTypes.ROCKY
        
    def SetBoard(self,board):
        for x in range(0,42):
            self.boardGrid.append([])
            for y in range(0,42):
                self.boardGrid[x].append(square(self,board[x][y]))
        
        
    def Display(self,blockSize):
        for row_list in self.boardGrid:
            for square_y in row_list:
                square_y.Display(blockSize)
                
    def PrintBoard(self):
        for x in range(0,42):
            for y in range(0,42):
                print(self.boardGrid[x][y].squareType)
