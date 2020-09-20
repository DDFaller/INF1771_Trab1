from board import board
from gameManager import gameManager
from knights import athenaKnight
from squareTypes import squareTypes

WIDTH = 420
HEIGHT = 420

BLACK = (80,80,80)
GREY = (173,173,173)
WHITE =(222,222,222)
game = gameManager()
def setup():
    size(WIDTH,HEIGHT)

    
def draw():
    blockSize = WIDTH/42
    board = game.GetBoard()
    for row in range(0,42):
        for column in range(0,42):
            squareType = board[row][column].GetSquareType()
            rectColor = (0,0,0)
            if squareType == squareTypes.MOUNTAIN:
                rectColor = BLACK
            if squareType == squareTypes.ROCKY:
                rectColor = GREY
            if squareType == squareTypes.PLANE:
                rectColor = WHITE
            rect(row * blockSize,column * blockSize,blockSize,blockSize)
            fill(rectColor[0],rectColor[1],rectColor[2])
