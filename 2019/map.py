import numpy as np

cost_map = {
    '#' : 999999999,
    '~' : 800,
    '*' : 200,
    '+' : 150,
    'X' : 120,
    '_' : 100,
    'H' : 70,
    'T' : 50,
}

class Map:
    def __init__(self, name, width, height, customers, maxOffices, terrain):
        self.name = name
        self.width = width
        self.height = height
        self.customers = customers
        self.maxOffices = int(maxOffices)
        self.terrain = self.setTerrain(terrain)
        
    def setTerrain(self, lines):
        char_terrain = [list(line.strip()) for line in lines]
        numpy_terrain = np.vectorize(cost_map.get)(np.asarray(char_terrain))
        return numpy_terrain
        
    def toString(self):
        return f"Map Name: {self.name} | Dimensions: {self.width} x {self.height} | Customers: {self.customers} | Max. Offices: {self.maxOffices}"

