
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
        self.CreateDefaultFile()   
    
    def GetGrid(self):
        return self.grid
    
    def ReadFile(self):
        file = open(self.path,"r")
        for linha in file:
            self.grid.append([])
            gridElements = linha.split('_')
            for element in gridElements:
                self.grid.append(boardInterpreter.casas[element])
        self.file.close()
        print(self.grid)    
                
    def CreateDefaultFile(self):
        file = open(self.path,'w')
        for row in range(0,42):
            for column in range(0,42):
                if not(column == 41): 
                    file.write("x_")
                else:
                    file.write("x")
            file.write("\n")
        
