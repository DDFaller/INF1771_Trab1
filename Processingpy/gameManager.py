from board import board
from knights import athenaKnight
from moveSense import moveSense
from boardInterpreter import boardInterpreter
from knightTypes import knightTypes


GoldenKnightsNames = [
"Mu de Aries",
"Aldebaran de Touro",
"Saga de Gemeos",
"Mascara da morte de Cancer",
"Aioria de Leao",
"Shaka de Virgem",
"Dohko de Libra",
"Milo de Escorpiao",
"Aioros de Sagitario",
"Shura de Capricornio",
"Camus de Aquario",
"Afrodite de Peixes"
]

BronzeKnightsNames = [
"Shun",
"Hyoga",
"Shiryu",
"Ikki",
"Seiya"
]



class gameManager:
    def __init__(self):
        self.gameBoard = board()
        self.goldenKnights = []
        self.bronzeKnights = []
        self.interpreter = boardInterpreter("labirinto.txt")
        self.StartGame()
        gridInterpreted = self.interpreter.GetGrid()
        self.GenerateBoard(gridInterpreted)
        self.showing = False
        
        
    def GetBoard(self):
        return self.gameBoard

    def GenerateBoard(self,grid):
        self.gameBoard.SetBoard(grid)

    def StartGame(self):
        self.BuildGoldenKnightsList()
        self.BuildBronzeKnightsList()
        for index in range(0,12):
            goldenKnight = self.goldenKnights[index]
            self.gameBoard.boardGrid[5 + index][0].knights.append(goldenKnight)
            goldenKnight.position = (5 + index,0)
        for bronzeKnight in self.bronzeKnights:
            self.gameBoard.boardGrid[0][0].knights.append(bronzeKnight)
            bronzeKnight.position = (0,0)

    def Display(self,blockSize,offsetx,offsety):
        self.gameBoard.Display(blockSize,offsetx,offsety)

    def BuildGoldenKnightsList(self):
        for index in range(0,12):
            print(index)
            self.goldenKnights.append(athenaKnight(knightTypes.GOLDENKNIGHT,GoldenKnightsNames[index],50.0 + 5  *index,1))
        self.goldenKnights[10].cosmicPower += 5
        self.goldenKnights[11].cosmicPower += 10

    def BuildBronzeKnightsList(self):
        for index in range(0,5):
            self.bronzeKnights.append(athenaKnight(knightTypes.BRONZEKNIGHT,BronzeKnightsNames[index],1 + 0.1 * index,5))
            
    def mousePressedListener(self,mousex,mousey):
        if self.showing == False:
            return 0
        return self.gameBoard.mousePressedListener(mousex,mousey)

    def MoveKnight(self,knight,sense,value):
        x, y = knight.GetPosition()
        self.gameBoard.boardGrid[x][y].knights.remove(knight)
        if sense== moveSense.HORIZONTAL:
            self.gameBoard.boardGrid[x + value][y].knights.append(knight)
            knight.position = (x + value,y)
        else:
            self.gameBoard.boardGrid[x][y + value].knights.append(knight)
            knight.position = (x,y + value)

    def showKnights(self):
        for goldenKnight in (self.goldenKnights + self.bronzeKnights):
            print(goldenKnight.name + " na posicao " + str(goldenKnight.position))
