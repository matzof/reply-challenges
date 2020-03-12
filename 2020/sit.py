class Sit():
    def __init__(self, x, y, type):
        self.x = int(x)
        self.y = int(y)
        self.type = type
        self.taken = False
        self.person = None

    def toString(self):
        return f"{self.x}:{self.y} = {self.type}"
    
    def getNeighbours(self, sit_list, width, height):  
        neighbours = []
        if self.y > 0:
            person = sit_list[(self.y-1)*(width) + self.x].person
            if person != None:
                neighbours.append(person)

        if self.y < height -1:
            person = sit_list[(self.y+1)*(width) + self.x].person
            if person != None:
                neighbours.append(person)
       
        if self.x > 0:
            person = sit_list[(self.y)*(width) + (self.x - 1)].person
            if person != None:
                neighbours.append(person)
        
        if self.x < width -1:
            person = sit_list[(self.y+1)*(width) + (self.x + 1)].person
            if person != None:
                neighbours.append(person)
                
        return neighbours 
            
