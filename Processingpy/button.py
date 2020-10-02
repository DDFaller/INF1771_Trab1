





class button:
    def __init__(self, x,y, buttonSize,bColor):
        self.position = (x - buttonSize[0]/2,y- buttonSize[1]/2)
        self.buttonSize = buttonSize
        self.bColor = bColor
        
        
    def Display(self):
        rect(self.position[0],self.position[1],self.buttonSize[0],self.buttonSize[1])
        fill(self.bColor[0],self.bColor[1],self.bColor[2])
        
    def mousePressedListener(self,x,y):
        if x >= self.position[0] and x <= self.position[0] + self.buttonSize[0]:
            if y >= self.position[1] and y <= self.position[1] + self.buttonSize[1]:
                return True
        return False
