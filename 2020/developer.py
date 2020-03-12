class Developer:
    def __init__(self, line):
        line_content = line.rstrip().split(' ')
        self.ci = line_content[0]
        self.bi = int(line_content[1])
        self.num_s = int(line_content[2])
        self.skills = set(line_content[3:])

    def toString(self):
        return f"Company: {self.ci} | Bonus: {self.bi} | Skills: {self.skills}"
    
    def compareDev(self, person): 
        common = len(self.skills.intersection(person.skills))
        diff = len(self.skills.union(person.skills)) - common
        work_score = common * diff
        bonus_score = self.bi * person.bi  
        return work_score + bonus_score
#        except: 
#            return self.bi * person.bi  

class Manager:
    def __init__(self, line):
        line_content = line.split(' ')
        self.ci = line_content[0]
        self.bi = line_content[1]

    def toString(self):
        return f"Company: {self.ci} | Bonus: {self.bi}"
