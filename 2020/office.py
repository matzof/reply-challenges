import numpy as np
from sit import Sit

cost_map = {
    '#' : 999999999,
    '_' : 1,
    'M' : 2
}

class Office():
    def __init__(self, name, width, height, lines):
        self.name = name
        self.width = int(width)
        self.height = int(height)
        self.sits = self.setSits(lines)
        self.sitMap = self.getSitMap(lines)
        
    def setSits(self, lines):
        char_sits = [list(line.rstrip()) for line in lines]

        sits = []
        for y, row in enumerate(char_sits):
            for x, sit in enumerate(row):
                sits.append(Sit(x,y, sit))
        
        return sits

    def getSitMap(self, lines):
        char_sits = [list(line.rstrip()) for line in lines]
        numpy_sits = np.vectorize(cost_map.get)(np.asarray(char_sits))
        return numpy_sits
        
    def toString(self):
        return f"Map Name: {self.name} | Dimensions: {self.width} x {self.height}"