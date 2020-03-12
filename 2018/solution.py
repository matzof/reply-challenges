# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 11:06:12 2020

@author: matzo
"""

import numpy

path = ''
path_in = path + 'input/'
path_out = path + 'output/'
input_files = {
    "first": path_in + "first_adventure.in",
    "second": path_in + "second_adventure.in",
    "third": path_in + "third_adventure.in",
    "fourth": path_in + "fourth_adventure.in"
}

class region:
    def __init__(self, name, width, height, customers, maxOffices, terrain):

file_contents = open(input_files['first'], 'r')
with file_contents as fc:
    lines = fc.readlines()
    num_v, num_s, num_c, num_p = lines.pop(0).split(' ')
    s_names = lines.pop(0).split(' ')
    c_names = lines.pop(0).split(' ')
    while len(lines[0].split(' ')) == 2:
        prov_name, num_r = lines.pop(0).split(' ')
        for i in range(num_r):
            
            
