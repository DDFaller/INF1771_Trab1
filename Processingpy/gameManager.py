from board import board
from knights import athenaKnight
from moveSense import moveSense
from boardInterpreter import boardInterpreter
from knightTypes import knightTypes
from knightSelection import knightSelection
from squareTypes import squareTypes
from APathFinder import APathFinder
from GeneticAlgo import GeneticAlgo

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

BronzeKnightsColors = [
(153,50,153),
(0,0,225),
(225,0,0),
(0,225,0),
(0,0,0)
]



class gameManager:
    def __init__(self):
        self.gameBoard = board()
        self.interpreter = boardInterpreter("labirinto.txt")
        self.pathFinder = APathFinder(self.gameBoard)
        self.geneticAlgo = GeneticAlgo()
        self.showing = False
        self.findPath = False
        self.ResetGame()


    def GetBoard(self):
        return self.gameBoard

    def GenerateBoard(self,grid):
        self.gameBoard.SetBoard(grid)

    def CheckVictory(self):
        for bronzeKnight in self.bronzeKnights:
            if not(bronzeKnight.position[0] == self.gameBoard.finalSquare.position[0] and bronzeKnight.position[1] == self.gameBoard.finalSquare.position[1]):
                return False
        return True

    def MoveKnight(self,knight,movement):
        preMovePosX,preMovePosY = knight.GetPosition()
        if knight.Move(movement):
            x, y = knight.GetPosition()
            print(self.gameBoard.boardGrid[preMovePosX][preMovePosY].position)
            print(self.gameBoard.initialSquare.position)
            print(self.gameBoard.boardGrid[preMovePosX][preMovePosY].knights)
            #self.gameBoard.boardGrid[preMovePosX][preMovePosX].knights.remove(knight)
            self.gameBoard.boardGrid[x][y].knights.append(knight)
            return True
        return False

    #Initilization Classes to run the game
    def StartGame(self,Grid):
        self.GenerateBoard(Grid)
        self.BuildGoldenKnightsList()
        self.BuildBronzeKnightsList()

        for index in range(0,12):
            goldenKnight = self.goldenKnights[index]
            self.gameBoard.boardGrid[5 + index][0].knights.append(goldenKnight)

        for bronzeKnight in self.bronzeKnights:
            bronzeKnight.position = self.gameBoard.initialSquare.position
            self.gameBoard.initialSquare.knights.append(bronzeKnight)

        self.knightSelect = knightSelection(self.bronzeKnights,BronzeKnightsNames,BronzeKnightsColors)
        self.pathFinder.FindPath([x.GetPosition() for x in self.goldenKnights])
        while not(self.geneticAlgo.done == True):
            self.geneticAlgo.Initialize(self.pathFinder.path,self.bronzeKnights,self.goldenKnights)
            self.geneticAlgo.Execute()

    def BuildGoldenKnightsList(self):
        for index in range(0,12):
            self.goldenKnights.append(athenaKnight(knightTypes.GOLDENKNIGHT,GoldenKnightsNames[index],50.0 + 5  *index,1))
        self.goldenKnights[10].cosmicPower += 5
        self.goldenKnights[11].cosmicPower += 10

        for index in  range(0,len(self.goldenKnights)):
            for i in range(0,len(self.gameBoard.boardGrid)):
                for j in range(0,len(self.gameBoard.boardGrid[i])):
                    if self.gameBoard.boardGrid[i][j].squareType == squareTypes.CASA[index]:
                        self.goldenKnights[index].position = (i,j)
                        break

    def BuildBronzeKnightsList(self):
        for index in range(0,5):
            self.bronzeKnights.append(athenaKnight(knightTypes.BRONZEKNIGHT,BronzeKnightsNames[index],1 + 0.1 * index,5))

    def ResetGame(self):
        self.goldenKnights = []
        self.bronzeKnights = []
        self.knightSelectedIndex = -1


    #GameManager Display functions and Listeners to input
    #Show gameboard, knight selection menu and Knights
    def Display(self,blockSize,offsetx,offsety):
        self.gameBoard.Display(blockSize,offsetx,offsety)
        self.showKnights(blockSize,offsetx,offsety)
        self.knightSelect.Display()
        if self.findPath:
            self.pathFinder.Display(blockSize,offsetx,offsety)
            if not(self.pathFinder.path == []):
                self.geneticAlgo.Initialize(self.pathFinder.path,self.bronzeKnights,self.goldenKnights)
                self.geneticAlgo.Execute()

    #Father class ProcessingPY checks if this is valid to receive clicks
    #Process knight selection menu and clicks on board
    def mousePressedListener(self,mousex,mousey):
        index = self.knightSelect.mousePressedListener(mousex,mousey)
        if index != -1:
            self.knightSelectedIndex = index
            print("Knight selected index " + str(index))
        if self.gameBoard.mousePressedListener(mousex,mousey) == 0:
            return 0
        return 1

    #Just used to test knights movement
    def keyPressedListener(self,keyValue):
        print("Key pressed " + str(keyValue))
        self.pathFinder.keyPressedListener(keyValue)
        if keyValue == "a":
            return self.MoveKnight(self.bronzeKnights[self.knightSelectedIndex],(-1,0))
        if keyValue == "w":
            return self.MoveKnight(self.bronzeKnights[self.knightSelectedIndex],(0,-1))
        if keyValue == "d":
            return self.MoveKnight(self.bronzeKnights[self.knightSelectedIndex],(1,0))
        if keyValue == "s":
            return self.MoveKnight(self.bronzeKnights[self.knightSelectedIndex],(0,1))
        if keyValue == "x":
            self.findPath = not(self.findPath)
            return True
        return False

    def showKnights(self,blockSize,offsetX,offsetY):
        for knightIndex in range(0,len( self.bronzeKnights)):
            rect(offsetX/2 + blockSize * self.bronzeKnights[knightIndex].position[0],offsetY/2 + blockSize * self.bronzeKnights[knightIndex].position[1],blockSize,blockSize)
            fill(BronzeKnightsColors[knightIndex][0],BronzeKnightsColors[knightIndex][1],BronzeKnightsColors[knightIndex][2])
            for goldenKnight in range(0,len(self.goldenKnights)):
                textAlign(CENTER)
                #text(goldenKnight,offsetX/2 +blockSize/2 +  blockSize * self.goldenKnights[goldenKnight].position[0],offsetY/2 + (blockSize+1) * self.goldenKnights[goldenKnight].position[1])#blockSize,blockSize)
                text(goldenKnight,offsetX/2 +  blockSize * self.goldenKnights[goldenKnight].position[0],offsetY/2 + blockSize * self.goldenKnights[goldenKnight].position[1])
