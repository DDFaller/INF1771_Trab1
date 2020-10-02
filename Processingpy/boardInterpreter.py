
from squareTypes import squareTypes


class boardInterpreter:
    casas = {"1":squareTypes.CASA[0],
             "2":squareTypes.CASA[1],
             "3":squareTypes.CASA[2],
             "4":squareTypes.CASA[3],
             "5":squareTypes.CASA[4],
             "6":squareTypes.CASA[5],
             "7":squareTypes.CASA[6],
             "8":squareTypes.CASA[7],
             "9":squareTypes.CASA[8],
             ")":squareTypes.CASA[9],
             "!":squareTypes.CASA[10],
             "@":squareTypes.CASA[11],
             "x":squareTypes.MOUNTAIN,
             "o":squareTypes.PLANE,
             "l":squareTypes.ROCKY
             }

    def __init__(self, path):
        self.path = path
        self.grid = []
        self.ReadFile()
        self.showing = False
        
    def GetGrid(self):
        return self.grid

    def ReadFile(self):
        file = open(self.path,"r")
        gridCount = 0
        for linha in file:
            self.grid.append([])
            gridElements = linha.split('_')
            for element in gridElements:
                self.grid[gridCount].append(boardInterpreter.casas[element[0]])
            gridCount += 1
        file.close()
        print(self.grid)
    
    def SetFile(self):
        file = open(self.path, "w")
        for linha in file:
            for element in linha:
                file.write(boardInterpreter.TranslateTypeToString(element))
                file.write('_')
            file.write('\n')
                
                
    def TranslateStringToType(strCode):
        return boardInterpreter[strCode]
     
    def TranslateTypeToString(typeCode):
        for element in boardInterpreter.casas.keys:
            if boardInterpreter.casas[element] == typeCode:
                return element
                
    def CreateDefaultFile(self):
        file = open(self.path,'w')
        for row in range(0,42):
            for column in range(0,42):
                if not(column == 41):
                    file.write("x_")
                else:
                    file.write("x")
            file.write("\n")
    
    def CalculateGridElementClicked(self,mousex,mousey):
        x = (mousex - self.offsetX)/ self.blockSize
        y = (mousey - 10 - self.offsetY) / self.blockSize
        print(x)
        print(y)
        return x,y
        
    def OpenGridWindow(self,width,height,edit):
        size(width,height)

    def setup(self):
        background(150)

    def Display (self,blockSize,offsetx, offsety):
        self.blockSize = blockSize
        BLACK = (80,80,80)
        GREY = (173,173,173)
        WHITE =(222,222,222)
        YELLOW = (150,150,0)
        self.offsetX = offsetx/2
        self.offsetY = offsety/2
        for x in range(0,42):
            for j in range(0,42):
                rectColor = (0,0,0)
                square = self.grid[x][j]
                if square == squareTypes.MOUNTAIN:
                    rectColor = BLACK
                elif square == squareTypes.ROCKY:
                    rectColor = GREY
                elif square == squareTypes.PLANE:
                    rectColor = WHITE
                else:
                    rectColor = YELLOW
                rect(x * blockSize + offsetx/2,j * blockSize + offsety/2,blockSize,blockSize)
                fill(rectColor[0],rectColor[1],rectColor[2])
                
        
                
    
    def mousePressedListener(self,mousex,mousey):
        if not self.showing:
            return 0
        
        x,y = self.CalculateGridElementClicked(mousex,mousey)
        square = self.grid[x][y]
        if square == squareTypes.MOUNTAIN:
            self.grid[x][y] = squareTypes.ROCKY
        elif square == squareTypes.ROCKY:
            self.grid[x][y] = squareTypes.PLANE
        elif square == squareTypes.PLANE:
            self.grid[x][y] = squareTypes.MOUNTAIN
            
        return 1
