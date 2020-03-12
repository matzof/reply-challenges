class Sit():
    def __init__(self, x, y, type):
        self.x = int(x)
        self.y = int(y)
        self.type = type
        self.taken = False

    def toString(self):
        return f"{self.x}:{self.y} = {self.type}"