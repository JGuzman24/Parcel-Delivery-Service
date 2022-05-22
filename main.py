# Justin Guzman
# ID: 000812901
# WGU - C950 Data Structures and Algorithms II

from importCSV import load_package_data, distance_graph
from dijkstra import dijkstra_shortest_path, get_shortest_path
from Truck import Truck

'''
creates empty set for packages and graph from the given distance table
'''
package_set = set([])
g = distance_graph('WGUPS Distance Table.csv')

'''
verifies package loaded is valid and that the truck has space for another package
'''
# O(N)
def load(truck, packages):
    for package in packages:
        if my_hash.search(package) in package_set and truck.space:
            truck.load_package(my_hash.search(package))
            package_set.remove(my_hash.search(package))
            my_hash.search(package).update("status", "en route")
            my_hash.search(package).enroute = truck.time
            my_hash.search(package).update("truck", truck.tid)
        else:
            print("Could not load Package {}".format(package))


'''
inputs time in minutes - outputs time in standard format as string
'''
# O(1)
def get_time(time):
    hours = time // 60
    minutes = time % 60
    if hours >= 24:
        hours %= 24
    if hours == 12:
        display = "12:{:0>2d} p.m.".format(minutes)
    if hours > 12:
        display = "{:0>2d}:{:0>2d} p.m.".format(hours - 12, minutes)
    else:
        display = "{:0>2d}:{:0>2d} a.m.".format(hours, minutes)
    return display


'''
inputs start and end address and finds shortest path using dijkstra
'''
# O(N)
def route_check(start_address, end_address):
    start = g.get_key(start_address)
    end = g.get_key(end_address)

    dijkstra_shortest_path(g, start)

    total_d = end.distance

    # resets vertices once shortest path is determined
    for v in g.adjacency_list:
        v.distance = float('inf')
        v.pred_vertex = None
    return total_d


'''
starts truck departure. will continue while truck has at least 1 package
'''
# O(2NlogN)
def depart(truck):
    miles = 0
    path = []
    # O(logN)
    while truck.packages > 0:
        lastd = 0
        least = float('inf')
        nextd = ""

        # looks through all addresses and selects next closest
        # O(N)
        for dest in truck.destinations:
            miles = route_check(truck.location, dest)
            if miles < least and truck.location != dest:
                least = miles
                nextd = dest
        #print("\nNext destination is {:.1f} miles away: {} ".format(least, nextd))    - optional next destination text
        dijkstra_shortest_path(g, g.get_key(truck.location))
        path = get_shortest_path(g.get_key(truck.location), g.get_key(nextd))

        # adds distance to each stop until destination. checks if stop is a delivery address
        # O(N)
        for add in range(len(path)):
            #print("Next Stop: {} ({:.1f})".format(path[add].label, path[add].distance - lastd))    -optional next stop text
            lastd = path[add].distance - lastd
            truck.drive(path[add].label, lastd)

            if path[add].label in truck.destinations:
                truck.deliver(path[add].label)

def complete(truck):
    print("Truck-{}".format(truck.tid))
    print("Deliveries complete at: {}".format(truck.get_time()))
    print("Distance traveled: {:.1f} miles\n".format(truck.distance))

def print_mileage():
    print("Truck-1 distance traveled: {:.1f} miles".format(truck1.distance))
    print("Truck-2 distance traveled: {:.1f} miles".format(truck2.distance))
    print("Total distance traveled for all deliveries: {:.1f}\n".format(truck1.distance + truck2.distance))


'''
prints status of all packages based on time entered
'''
# O(N)
def get_packages_status(hour, minutes):
    time = (hour*60) + minutes
    print("Status of packages at {}:".format(get_time(time)))
    for id in range(1, len(my_hash.table)):
        package = my_hash.search(id)
        if time >= package.deliver:
            print("    Package {} status: {}".format(id, package.status))
        elif time >= package.enroute:
            print("    Package {} status: en route".format(id))
        else:
            print("    Package {} status: at the hub".format(id))
        id += 1
    print()


'''
prints full information of particular package based on time entered
'''
# O(N)
def get_package_status(i, hour, minutes):
    time = (hour*60) + minutes
    pack = my_hash.search(i)
    pack.info()
    if time >= pack.deliver:
        print("    Status: {}".format(pack.status))
    elif time >= pack.enroute:
        print("    Status: en route".format(i))
    else:
        print("    Status: at the hub".format(i))
    print()

def return_to_hub(truck):
    truck.drive("4001 South 700 East", route_check(truck.location, "4001 South 700 East"))
    truck.location = "4001 South 700 East"
    truck.space = True


'''
Start of program.
hash dynamically loaded from package file
packages loaded based on given criteria (special notes)
Space/Time complexity O(1) unless otherwise stated
'''
my_hash = load_package_data('WGUPS Package File.csv')
hash_length = len(my_hash.table)
package_load_1 = [13, 15, 19, 20, 16, 14, 39, 34, 21, 7, 29, 2, 33, 12, 4, 40]
package_load_2 = [18, 36, 3, 38, 30, 8, 27, 35, 11, 23, 10, 5, 37, 1]
package_load_3 = [6, 32, 25, 28, 31, 26, 17, 24, 22]
package_load_4 = [9]

'''packages loaded into package set'''
# O(N)
for package in range(hash_length):
    package_set.add(my_hash.search(package))

'''trucks created and loaded with first group'''
truck1 = Truck(1)
truck2 = Truck(2)
load(truck1, package_load_1)
load(truck2, package_load_2)

'''
package 15 has earliest deadline, therefor is first destination. 
afterwards, both trucks told to depart as normal for deliveries, then return to hub.
'''
truck1.drive("4580 S 2300 E", route_check(truck1.location, "4580 S 2300 E"))
truck1.deliver("4580 S 2300 E")
depart(truck1)
depart(truck2)
return_to_hub(truck1)
return_to_hub(truck2)

'''
truck 2 loaded with second group
priority delivery for second group are packages 25 and 6
'''
load(truck2, package_load_3)
truck2.drive("5383 South 900 East #104", route_check(truck2.location, "5383 South 900 East #104"))
truck2.deliver("5383 South 900 East #104")
truck2.drive("3060 Lester St", route_check(truck2.location, "3060 Lester St"))
truck2.deliver("3060 Lester St")
depart(truck2)

'''
truck 1 waits at hub until correct address for package 9 arrives
'''
if truck1.time < 620:
    truck1.time = 620
my_hash.search(9).update("address", "410 S State St")
my_hash.search(9).update("zipC", "84111")
load(truck1, package_load_4)
depart(truck1)


'''
user interface
'''
print("\n\nWelcome to the WGUPS Service\n")
print("Please choose from the following actions:\n")
print("    1: View delivery Logs for all Trucks\n"
      "    2: View total mileage for all Trucks\n"
      "    3: View status for all packages at a given time\n"
      "    4: View all info for one package at a given time\n\n"
      "    0: Exit\n")
entry = input("\n")

while entry != "0":
    if entry == "1":
        truck1.print_log()
        complete(truck1)
        truck2.print_log()
        complete(truck2)

    if entry == "2":
        print_mileage()

    if entry == "3":
        print("Please enter time (military)")
        hour = int(input("Hours: "))
        minutes = int(input("Minutes: "))
        print()
        get_packages_status(hour, minutes)

    if entry == "4":
        package = int(input("Please enter Package ID: "))
        print("Please enter time (military)")
        hour = int(input("Hours: "))
        minutes = int(input("Minutes: "))
        get_package_status(package, hour, minutes)

    entry = input("Please select action 1-4 or enter 0 to exit: \n")

exit()













