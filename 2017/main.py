# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 18:28:20 2020

@author: matzo
"""
# Import functions and classes
from functions import compute_path

# Configuration for the input files
input_dir = "input/"
output_path = "output/"
input_files = {
    "1": input_dir + "input_1.txt",
    "2": input_dir + "input_2.txt",
    "3": input_dir + "input_3.txt",
    "4": input_dir + "input_4.txt"
}



if __name__ == '__main__':
    inputs = ['1', '2', '3', '4']
    for filename in inputs:
        compute_path(filename, input_files)