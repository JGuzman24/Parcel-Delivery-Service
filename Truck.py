class Truck:
    def __init__(self, ID):
        self.tid = ID
        self.load = []
        self.destinations = set([])
        self.space = True
        self.speed = 18
        self.time = 480
        self.distance = 0
        self.packages = 0
        self.location = "4001 South 700 East"
        self.log = {}

    # O(1)
    def drive(self, location, distance):
        length = distance
        self.location = location
        self.distance += distance
        time = int((((distance / self.speed) * 60) + 1) // 1)
        self.time += time
        self.log[self.time] = [self.get_time(), self.location, length]

    # O(1)
    def load_package(self, package):
        if self.space:
            self.load.append(package)
            self.destinations.add(package.address)
            self.packages += 1
            if self.packages >= 16:
                self.space = False
        else:
            print("Cannot Load, at capacity")

    # O(N)
    def print_destinations(self):
        print("\n{} Destinations in Truck-{}".format(len(self.destinations), self.tid))
        for destination in self.destinations:
            print(" {}".format(destination))
        print()

    # O(N)
    def print_load(self):
        print("\n{} Packages in Truck: {}".format(self.packages, self.tid))
        for package in self.load:
            print(" {}".format(package))
        print()

    # O(N)
    def deliver(self, address):
        remove = []
        for package in self.load:
            if package.address == address:
                remove.append(package)
        for package in remove:
            self.load.remove(package)
            self.packages -= 1
            package.status = "delivered at: {}".format(self.get_time())
            package.deliver = self.time
        self.destinations.remove(address)

    # O(N)
    def get_time(self):
        hours = self.time // 60
        minutes = self.time % 60
        if hours >= 24:
            hours %= 24
        if hours == 12:
            display = "12:{:0>2d} p.m.".format(minutes)
        if hours > 12:
            display = "{:0>2d}:{:0>2d} p.m.".format(hours - 12, minutes)
        else:
            display = "{:0>2d}:{:0>2d} a.m.".format(hours, minutes)
        return display

    # O(N)
    def print_log(self):
        minutes = 480
        print("Truck-{} LOG:".format(self.tid))
        while minutes <= self.time:
            if minutes in self.log:
                print("    "+self.log[minutes][0] + ' -- Distance: {:.1f} miles'.format(self.log[minutes][2]) + ' -- ' + self.log[minutes][1])
            minutes += 1
        print()

