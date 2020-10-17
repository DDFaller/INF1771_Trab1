from board import board
from gameManager import gameManager
from knights import athenaKnight
from squareTypes import squareTypes
from boardInterpreter import boardInterpreter
from gameMenu import gameMenu

WIDTH = 940
HEIGHT = 990
offsetx = 50
offsety = 100
blockSize = (WIDTH - offsetx)/42

game = gameManager()
menu = gameMenu(WIDTH,HEIGHT)
interpreter = boardInterpreter("labirinto.txt")

listeners_dict = {"Mouse pressed":[], "Key pressed":[]}

listeners_dict["Mouse pressed"].append(interpreter)
listeners_dict["Mouse pressed"].append(menu)
listeners_dict["Mouse pressed"].append(game)
listeners_dict["Key pressed"].append(game)

menu.showing = True

def setup():
    size(WIDTH,HEIGHT)

def draw():
    background(240)
    if game.showing:
        game.Display(blockSize,offsetx,offsety)
    if menu.showing:
        menu.Display(blockSize,offsetx,offsety)    
    if interpreter.showing:
        interpreter.Display(blockSize,offsetx,offsety)
    
def mousePressed():
    for listener in listeners_dict["Mouse pressed"]:
        if listener.showing:
            code = listener.mousePressedListener(mouseX,mouseY)
            if isinstance(listener,gameMenu):
                if code == 1:
                    interpreter.showing = True
                    game.showing = False
                elif code == 2:
                    game.showing = True
                    interpreter.showing = False
                    game.StartGame(interpreter.GetGrid())
                if code != 0:
                    menu.showing = False  
            if isinstance(listener,boardInterpreter):
                if code == 2:
                    game.showing = False
                    interpreter.showing = False
                    menu.showing = True
            
            return           

def keyPressed():
    for listener in listeners_dict["Key pressed"]:
        if listener.showing:
            listener.keyPressedListener(key)
            

def assignMousePressed(classToAssign):
    listeners_dict["Mouse pressed"].append(classToAssign)
    
