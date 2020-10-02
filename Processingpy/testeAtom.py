from board import board
from gameManager import gameManager
from knights import athenaKnight
from squareTypes import squareTypes
from boardInterpreter import boardInterpreter



interpreter = boardInterpreter("labirinto.txt")
gridInterpreted = interpreter.GetGrid()
game = gameManager()
game.GenerateBoard(gridInterpreted)
