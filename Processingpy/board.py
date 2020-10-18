from squareTypes import squareTypes
from square import square
from random import randint
from knightSelection import knightSelection

class board:
    def __init__(self):
        self.boardGrid = []
        self.BuildBoard()
        self.offsetX = 0
        self.offsetY = 0
        self.blockSize = 1
        #self.initialSquare = self.boardGrid[4][36]
        #self.finalSquare = self.boardGrid[37][36]
        self.initialSquare = self.boardGrid[37][37]
        self.finalSquare = self.boardGrid[36][4]

    def GetSquare(self,x,y):
        if x >= 0 and x < 42:
            if y >= 0 and y < 42:
                return self.boardGrid[x][y]
        return None

    def BuildBoard(self):
        for x in range(0,42):
            self.boardGrid.append([])
            for y in range(0,42):
                self.boardGrid[x].append(square(self,squareTypes.ROCKY,(x,y)))

        for index in range(0,50):
            bucket = int(randint(0,2))
            if bucket == 0:
                self.boardGrid[int(randint(0,41))][int(randint(0,41))].squareType = squareTypes.MOUNTAIN
            if bucket == 1:
                self.boardGrid[int(randint(0,41))][int(randint(0,41))].squareType = squareTypes.PLANE
            if bucket == 2:
                self.boardGrid[int(randint(0,41))][int(randint(0,41))].squareType = squareTypes.ROCKY

    def SetBoard(self,board):
        self.boardGrid = []
        for x in range(0,42):
            self.boardGrid.append([])
            for y in range(0,42):
                self.boardGrid[x].append(square(self,board[x][y],(x,y)))
        self.initialSquare = self.boardGrid[37][37]
        self.finalSquare = self.boardGrid[36][4]

    def Display(self,blockSize, offsetx, offsety):
        self.offsetX = offsetx/2
        self.offsetY = offsety/2
        self.blockSize = blockSize
        for x in range(0,len(self.boardGrid)):
            for j in range(0,len(self.boardGrid[x])):
                self.boardGrid[x][j].Display(blockSize,offsetx ,offsety)
        #Initial position

        fill(0,225,0)
        rect(offsetx/2 + blockSize * self.initialSquare.position[0],offsety/2 + blockSize * self.initialSquare.position[1],blockSize,blockSize)


        #Final position
        fill(225,0,0)
        rect(offsetx/2 + blockSize * self.finalSquare.position[0],offsety/2 + blockSize * self.finalSquare.position[1],blockSize,blockSize)


    def PrintBoard(self):
        for x in range(0,42):
            for y in range(0,42):
                print(self.boardGrid[x][y].squareType)

    def CalculateGridElementClicked(self,mousex,mousey):
        x = (mousex - self.offsetX)/ self.blockSize
        y = (mousey - 10 - self.offsetY) / self.blockSize
        return x,y

    def mousePressedListener(self,mousex,mousey):
        if mousex >= self.offsetX and mousex <= self.offsetX + self.blockSize * 42:
            if mousey >= self.offsetY and mousey <= self.offsetY + self.blockSize * 42:
                x,y = self.CalculateGridElementClicked(mousex,mousey)
                return 1
        return 0
