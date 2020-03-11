class Customer:
    def __init__(self, id, x, y, reward):
        self.id = id
        self.x = int(x)
        self.y = int(y)
        self.reward = reward

    def toString(self):
        return f"Customer: {self.id} | Location: {self.x} x {self.y} | Reward: {self.reward}"
