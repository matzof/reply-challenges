class Developer:
    def __init__(self, line):
        line_content = line.rstrip().split(' ')
        self.ci = line_content[0]
        self.bi = int(line_content[1])
        self.num_s = int(line_content[2])
        self.skills = set(line_content[3:])
        self.sit = None

    def toString(self):
        return f"Company: {self.ci} | Bonus: {self.bi} | Skills: {self.skills}"
    
    def compareDev(self, person):
        try:
            common = len(self.skills.intersection(person.skills))
            diff = len(self.skills.union(person.skills)) - common
            work_score = common * diff
            bonus_score = self.bi * person.bi  
            return work_score + bonus_score
        except: 
            return self.bi * person.bi  

    def setSit(self, sit):
        self.sit = sit

class Manager:
    def __init__(self, line):
        line_content = line.rstrip().split(' ')
        self.ci = line_content[0]
        self.bi = int(line_content[1])
        self.sit = None

    def compareDev(self, person):
        return self.bi * person.bi

    
    def setSit(self, sit):
        self.sit = sit
    
    def toString(self):
        return f"Company: {self.ci} | Bonus: {self.bi}"
