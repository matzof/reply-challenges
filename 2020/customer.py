class Developer:
    def __init__(self, line):
        line_content = line.split(' ')
        self.ci = line_content[0]
        self.bi = line_content[1]
        self.num_s = line_content[2]
        self.skills = line_content[2:]

    def toString(self):
        return f"Company: {self.ci} | Bonus: {self.bi} | Skills: {self.skills}"
    
    def compareDev(self, dev):
        for skills
        return grade

class Manager:
    def __init__(self, line):
        line_content = line.split(' ')
        self.ci = line_content[0]
        self.bi = line_content[1]

    def toString(self):
        return f"Company: {self.ci} | Bonus: {self.bi}"
