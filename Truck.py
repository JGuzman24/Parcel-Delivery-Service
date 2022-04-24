class Truck:
    def __init__(self):
        self.load = []
        self.space = True
        self.speed = 18
        self.time = 480
        self.distance = 0
        self.packages = 0
        self.location = "4001 South 700 East"

    def load_package(self, package):
        if self.space:
            self.load.append(package)
            self.packages += 1
            if self.packages >= 16:
                self.space = False
        else:
            print("Cannot Load, at capacity")

    def print_load(self):
        print("\nPackages in Truck: ")
        for package in self.load:
            print(" {}".format(package))
        print()


