from board import board
from gameManager import gameManager
from knights import athenaKnight
from squareTypes import squareTypes
from boardInterpreter import boardInterpreter

WIDTH = 420
HEIGHT = 420

interpreter = boardInterpreter("labirinto.txt")
gridInterpreted = interpreter.GetGrid()
game = gameManager()
game.GenerateBoard(gridInterpreted)


def setup():
    size(WIDTH,HEIGHT)

    
def draw():
    blockSize = WIDTH/42
    board = game.GetBoard()
    board.Display(blockSize)
