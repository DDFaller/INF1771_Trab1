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

listeners_dict = {"Mouse pressed":[]}

listeners_dict["Mouse pressed"].append(interpreter)
listeners_dict["Mouse pressed"].append(menu)
listeners_dict["Mouse pressed"].append(game)

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
            if isinstance(menu,gameMenu):
                if code == 1:
                    interpreter.showing = True
                elif code == 2:
                    game.showing = True
                if code != 0:
                    menu.showing = False  
            return               
def assignMousePressed(classToAssign):
    listeners_dict["Mouse pressed"].append(classToAssign)
    
