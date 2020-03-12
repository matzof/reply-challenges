import os
import math

from pathlib import Path
import numpy as np

from office import Office
from developer import Developer

# Custom object classes for the problem
import plotter

# Configuration for the input files
input_dir = Path("input/")
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
    developers = [Developer(line) for line in content[int(height)+2 : int(height)+1+num_devs]]
    
    # Return both Map and Customer objects
    return office, developers


if __name__ == '__main__':
    office, devs = openInput("a")


    




    plotter.plotOffice(office.sitMap)
    
    