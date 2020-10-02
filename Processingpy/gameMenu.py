from button import button



class gameMenu:
    def __init__(self, windowWidth, windowHeight):
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.interpreterButton = button(windowWidth/2,windowHeight/2,[200,100],(200,0,0))
        self.gameButton = button(windowWidth/2, windowHeight/2 + 150,[200,100],(0,0,200))
        self.showing = False
        
    def Display(self,blockSize,offsetX,offsetY):
        self.interpreterButton.Display()
        self.gameButton.Display()
        
    def mousePressedListener(self,x,y):
        if not self.showing:
            return 0
        
        interpreter = self.interpreterButton.mousePressedListener(x,y)
        gameButton = self.gameButton.mousePressedListener(x,y)
        if interpreter:
            return 1
        if gameButton:
            return 2
    
        return 0
