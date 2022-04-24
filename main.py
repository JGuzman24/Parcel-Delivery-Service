from Package import Package
from importCSV import load_package_data, load_distance_data, distance_graph
from graph import Graph, Vertex
from dijkstra import dijkstra_shortest_path, get_shortest_path
from Truck import Truck

package_set = set([])

def load(truck, package):

    if my_hash.search(package) in package_set and truck.space:
        print("Loading Package: {}".format(my_hash.search(package)))
        my_hash.search(package).update("status", "On Truck")
        truck.load_package(my_hash.search(package))
        package_set.remove(my_hash.search(package))
        my_hash.search(package).update("status", "enroute")
    else:
        print("Could not load Package {}".format(package))


def route_check(graph, start_address, end_address):
    start = graph.get_key(start_address)
    end = graph.get_key(end_address)

    dijkstra_shortest_path(graph, start)

    path = get_shortest_path(start, end)

    print("Start: " + start.label)
    for stop in range(len(path) - 1):
        print("Stop {}: ".format(stop + 1) + path[stop])
        for j in range(40):
            if path[stop] == my_hash.search(j + 1).address:
                print("Package: {}".format(my_hash.search(j + 1).pID))
    print("Destination: " + end.label)
    for id in range(40):
        if end.label == my_hash.search(id + 1).address:
            print("Package: {}".format(my_hash.search(id + 1).pID))
    print("    Total Distance: {:.1f}\n".format(end.distance))


my_hash = load_package_data('WGUPS Package File.csv')
g = distance_graph('WGUPS Distance Table.csv')

#route_check(g, "4001 South 700 East", "233 Canyon Rd")

#route_check(g, my_hash.search(13).address, my_hash.search(10).address)

dijkstra_shortest_path(g, g.get_key("4001 South 700 East"))

route_check(g, "4001 South 700 East", "1488 4800 S")
route_check(g, "4001 South 700 East", "233 Canyon Rd")
route_check(g, "2010 W 500 S", "600 E 900 South")
route_check(g, "4001 South 700 East", "233 Canyon Rd")

path = get_shortest_path(g.get_key("4001 South 700 East"), g.get_key("1488 4800 S"))

#path = get_shortest_path(g.get_key("2010 W 500 S"), g.get_key("600 E 900 South"))

#path = get_shortest_path(g.get_key("4001 South 700 East"), g.get_key("233 Canyon Rd"))

'''route_check(g, "4001 South 700 East", "233 Canyon Rd")
route_check(g, "2010 W 500 S", "600 E 900 South")
route_check(g, "4001 South 700 East", "233 Canyon Rd")'''

for i in range(41):
    package_set.add(my_hash.search(i))

truck1 = Truck()
truck2 = Truck()

load(truck2, 1)
load(truck2, 2)
load(truck2, 10)
load(truck2, 3)
load(truck2, 5)
load(truck2, 5)

truck2.print_load()


#route_check(g, truck2.location, my_hash.search(10).address)

'''
for package in truck2.load:
    print("Truck at {}".format(truck2.location))
    print("Route check for package: {}".format(package.pID))
    route_check(g, truck2.location, package.address)'''


'''for v in g.adjacency_list:
    print(v.label, end="-->\n")
    for f in g.adjacency_list:
        print(" "+f.label, end=": ")
        print(g.edge_weights[(v, f)])'''


wgu = g.get_key("4001 South 700 East")



'''for i in range(len(path)):
    print("{} -> ".format(path[i]), end="")
print("total distance: {}".format(add.distance))

print("\nDijkstra shortest path:")
x = 0
for v in g.adjacency_list:

    path = get_shortest_path(wgu, v)
    print("Path from ({}) to ({}): ".format(wgu.label, v.label))
    print(wgu.label, end=" ")
    for i in range(len(path)):
        print("-> {} ".format(path[i]), end="")
    print("\n Total Distance: {:.1f}\n".format(v.distance))'''

'''for v in g.adjacency_list:
    print(v.label)
    for i in range(len(my_hash.table)):
        if v.label == my_hash.search(i+1).address:
            print(my_hash.search(i+1).pID, end=" - ")
            print(g.edge_weights[(wgu, v)])'''







