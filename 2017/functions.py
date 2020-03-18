# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 18:40:23 2020

@author: matzo
"""
import numpy as np

from classes import Obstacle


def read_input(filename, input_files):
    file_contents = open(input_files[filename], 'r')
    with file_contents as fc:
        content = fc.readlines()
        
    xs, ys, xf, yf = content.pop(0).rstrip().split(' ')
    num_obs = int(content.pop(0).rstrip())
    
    obs_list = [[int(elem) for elem in content.pop(0).rstrip().split(' ')] 
                    for _ in range(num_obs)]
    obs_arr = np.asarray(obs_list)
    return obs_arr, (xs, ys), (xf, yf), num_obs

def get_map(obstacles):
    maxes = np.max(np.max(obstacles, axis=0).reshape((3, 2)), axis=0)
    mins = np.min(np.min(obstacles, axis=0).reshape((3, 2)), axis=0)
    map_width, map_heigth = maxes - mins
    

def compute_path(filename, input_files):
    obstacles, start_pos, end_pos, n_obs = read_input(filename, input_files)