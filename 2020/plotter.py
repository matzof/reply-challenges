import matplotlib
from matplotlib import pyplot as plt
from matplotlib import colors
import numpy as np

color_dict = {    
    999999999: (0,0,0),
    1: (0,255,0),
    2: (0,0,255),
}

def valueToColor(value):
    return color_dict[value]

def plotOffice(sits):
    print("Plotting:")    
    data = sits
    plt.figure(figsize=(8,8))
    test_rgb = [[color_dict[i] for i in row] for row in data]
    plt.imshow(test_rgb, interpolation = 'none')
    plt.show()

def plotMapAndCustomers(map, customers):
    print("Plotting:")
    data = map.terrain

    for customer in customers:
        x, y = customer.x, customer.y
        data[y][x] = -1

    plt.figure(figsize=(8,8))
    test_rgb = [[color_dict[i] for i in row] for row in data]
    plt.imshow(test_rgb, interpolation = 'none')
    plt.show()


def plotMapCustomersOffices(map, customers, offices):
    print("Plotting:")
    data = map.terrain

    for customer in customers:
        x, y = customer.x, customer.y
        data[y][x] = -1

    for office in offices:
        x, y = int(office[0]), int(office[1])
        data[y][x] = -2

    plt.figure(figsize=(8,8))
    test_rgb = [[color_dict[i] for i in row] for row in data]
    plt.imshow(test_rgb, interpolation = 'none')
    plt.show()