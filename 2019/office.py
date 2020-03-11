import astar

class Office:
    def __init__(self, id, x, y, customers):
        self.id = id
        self.x = int(x)
        self.y = int(y)
        self.customers = customers
        self.paths = []


    def computePaths(self):
        for customer in customers:
            # Check if is reached and either ignore or replace if better
            
            paths.append

    def toString(self):
        return f"Office: {self.id} | Location: {self.x} x {self.y} | Customers: {len(self.customers)}"
