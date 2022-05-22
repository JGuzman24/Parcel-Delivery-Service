from hash import HashTable
from Package import Package
from graph import Graph, Vertex
import csv

'''
dynamically creates a hashtable and loads packages from a csv file
'''
# O(N)
def load_package_data(file):
    with open(file) as packages:
        size = sum(1 for row in csv.reader(packages, delimiter=',')) - 1


    with open(file) as packages:
        my_hash = HashTable(size)
        pData = csv.reader(packages, delimiter=',')
        next(pData)
        for package in pData:
            pID = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zipC = package[4]
            deadLine = package[5]
            weight = package[6]
            status = "at the hub"

            package = Package(pID, address, city, state, zipC, deadLine, weight, status)
            my_hash.insert(pID, package)

    return my_hash

# O(N)
def load_distance_data(file):
    with open(file) as distances:
        group = []
        dData = csv.reader(distances, delimiter=',')
        next(dData)
        for item in dData:
            group.append(item)
        return group

# O(N2)
def distance_graph(file):
    distances = load_distance_data(file)
    g = Graph()

    for v in range(len(distances)):
        g.add_vertex(Vertex(distances[v][0]))

    x = 0
    y = 1
    # O(N2)
    for i in g.adjacency_list:
        for j in g.adjacency_list:
            g.add_edge(i, j, distances[x][y])
            y += 1
        y = 1
        x += 1

    return g




