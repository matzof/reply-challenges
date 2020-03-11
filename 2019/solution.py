import os
import math

from pathlib import Path
from sklearn.cluster import KMeans
import numpy as np

# Custom object classes for the problem
from map import Map
from customer import Customer
import plotter

# Configuration for the input files
input_dir = Path("input/")
input_files = {
    "victoria": input_dir / "1_victoria_lake.txt",
    "himalayas": input_dir / "2_himalayas.txt",
    "budapest": input_dir / "3_budapest.txt",
    "manhattan": input_dir / "4_manhattan.txt",
    "oceania": input_dir / "5_oceania.txt",
}

# Function to open an input file
def openInput(name):
    # Open text file and store bag of lines
    file_contents = open(input_files[name], 'r')
    with file_contents as fc:
        content = fc.readlines()

    # Parse first line into a Map object
    width, height, num_customers, num_offices = content[0].split(' ')
    num_customers = int(num_customers) + 1
    map = Map(name, width, height, num_customers, num_offices, content[num_customers :])

    # Parse customer lines into Customer objects
    customers = []
    for i, customer in enumerate(content[1 : num_customers], 1):
        x, y, reward = customer.split(' ')
        customers.append(Customer(i, x, y, reward))

    # Return both Map and Customer objects
    return map, customers


def heuristicSolution(map, customers):
    # Define ratio-based clusters for the customers
    ratio = map.customers / map.maxOffices
    clusters = int(math.ceil(map.customers / ratio))
    kmeans = KMeans(n_clusters=clusters, max_iter=500, n_init=5)

    customer_locations = np.array([[customer.x, customer.y] for customer in customers])
    kmeans.fit_predict(customer_locations)
    cluster_centers = np.rint(kmeans.cluster_centers_)
    
    print(cluster_centers)

    # Generate radius of potential points in epicenter
    potential_areas = [cluster_centers]

    # Compute A Star paths for points in epicenter
    

    # Sort on score

    # Add max to solution
    return cluster_centers

if __name__ == '__main__':
    map, customers = openInput("oceania")
    
    offices = heuristicSolution(map, customers)
    plotter.plotMapCustomersOffices(map, customers, offices)

    