from button import button

class knightSelection:
    def __init__(self,bronzeKnights,knightsNames,knightsColors):
        self.bronzeKnights= bronzeKnights
        self.buttons = []
        self.colors = knightsColors
        self.knightsNames = knightsNames
        self.createButtons()

    def createButtons(self):
        for index in range(0,len(self.bronzeKnights)):
            self.buttons.append(button(index * 50 + 20,0,(40,40),self.colors[index]))


    def Display(self):
        for button in self.buttons:
            button.Display()

    def mousePressedListener(self,x,y):
        for index in range(0,len(self.buttons)):
            if self.buttons[index].mousePressedListener(x,y):
                print("Knight Selected " + str(self.knightsNames[index]))
                return index
        return -1
