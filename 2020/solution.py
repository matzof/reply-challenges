import os
import math

from pathlib import Path
import numpy as np

from office import Office
from developer import Developer
from developer import Manager

# Custom object classes for the problem
import plotter

# Configuration for the input files
input_dir = Path("input/")
output_path = Path("output/")
input_files = {
    "a": input_dir / "a_solar.txt",
    "b": input_dir / "b_dream.txt",
    "c": input_dir / "c_soup.txt",
    "d": input_dir / "d_maelstrom.txt",
    "e": input_dir / "e_igloos.txt",
    "f": input_dir / "f_glitch.txt",
}

# Function to open an input file
def openInput(name):
    # Open text file and store bag of lines
    file_contents = open(input_files[name], 'r')
    with file_contents as fc:
        content = fc.readlines()

    # Parse first line into a Map object
    width, height = content[0].split(' ')
    office = Office(name, width, height, content[1 : int(height) + 1])

    num_devs = int(content[int(height)+1])
    developers = [Developer(line) for line in content[int(height) + 2 : int(height) + 2 + num_devs]]
    developers = developers.sort(key=lambda developers: (developers.ci, developers.bi, developers.num_s), reverse=True)
    
    manager_start = int(height) + 1 + num_devs + 1
    num_managers = int(content[manager_start])

    managers = [Manager(line) for line in content[manager_start + 1 :]]
    managers = managers.sort(key=lambda managers: (managers.ci, managers.bi), reverse=True)

    # Return both Map and Customer objects
    return office, developers, managers


def computeSolution(file):
    office, devs, mans = openInput(file)

    output = []

    for sit in office.sits:
        if sit.type == '_' and sit.taken == False:
            neighbors = sit.getNeighbors()

            dev_compatibilities = {}

            for i, dev in enumerate(devs):
                if dev.sit == None:
                    dev_compatibility = 0
                    for neighbor in neighbors:
                        dev_compatibility = dev_compatibility + neighbor.compareDev(dev)
                    dev_compatibilities[i] = dev_compatibility
            
            dev_index = max(dev_compatibilities, key=lambda key: dev_compatibilities[key])
            dev = devs[dev_index]
            dev.setSit(sit)
            sit.taken = True
            sit.developer = dev
                

        if sit.type == 'M' and sit.taken == False:
            for man in mans:
                if man.sit == None:
                    man.setSit(sit)
                    sit.taken = True
                    break               
            
    for dev in devs:
        if dev.sit != None:
            output.append(f"{dev.sit.x} {dev.sit.y}")
        else:
            output.append("X")
    
    for man in mans:
        if man.sit != None:
            output.append(f"{man.sit.x} {man.sit.y}")
        else:
            output.append("X")


    with open(output_path / f"{file}.txt", 'w') as f:
        for i, line in enumerate(output):
            if i != (len(output) - 1):
                f.write(line + '\n')                
            else:
                f.write(line)


if __name__ == '__main__':
    inputs = input_files.keys()
    for input in inputs:
        computeSolution(input)
    

    #plotter.plotOffice(office.sitMap)
    
    
