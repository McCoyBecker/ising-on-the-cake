#The GewekeList class allows an implementation of the Geweke statistic for determining chain convergence

class GewekeList:
    
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.countsheet = [[0 for i in range(self.height)] for k in range(self.width)]
        self.sheet = [[0 for i in range(self.height)] for k in range(self.width)]
        self.InterChainVariation = [0 for i in range(self.width)]
        self.WithinChainVariation = [[0 for i in range(self.height)] for k in range(self.width)]

    def add(self, number):
        self.sheet[self.width]self.[height] += (self.sheet[self.width][self.height]*self.countsheet[self.width][self.height]+float(number))/(self.countsheet[self.width][self.height]+1)
        self.countsheet[self.width][self.height]+=1

    def updateInterChainVariation(self):
        
        SheetMean = [0 for k in range(self.width)]
        for k in range(len(self.InterChainVariation)):
            for l in range(self.height):
                SheetMean[k] += self.sheet[k][l]
            SheetMean[k] = SheetMean[k]/float(self.height)
    
        for k in range(len(self.InterChainVariation)):
            for l in range(self.height):
                self.InterChainVariation[k] += (self.sheet[k][l]-SheetMean[k])**2

    def updateWithinChainVariation(self):



