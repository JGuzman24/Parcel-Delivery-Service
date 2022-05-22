class Package:
    def __init__(self, pID, address, city, state, zipC, deadLine, weight, status):
        self.pID = pID
        self.address = address
        self.city = city
        self.state = state
        self.zipC = zipC
        self.deadline = deadLine
        self.weight = weight
        self.status = 'at the hub'
        self.truck = None
        self.enroute = 0
        self.deliver = 0

    # O(1)
    def __str__(self):
        return "{}, {}, {}, {}, {}, {}, {}, {}".format(self.pID, self.address, self.city, self.state,
                                                       self.zipC, self.deadline, self.weight, self.status)

    # O(1)
    def update(self, par, value):
        if par == 'pID':
            print('Cannot update Package ID')
        elif par == 'address':
            self.address = value
        elif par == 'city':
            self.city = value
        elif par == 'state':
            self.state = value
        elif par == 'zipC':
            self.zipC = value
        elif par == 'deadline':
            self.deadline = value
        elif par == 'weight':
            self.weight = value
        elif par == 'status':
            self.status = value
        elif par == 'truck':
            self.truck = value
        elif par == 'enroute':
            self.enroute = value
        elif par == 'deliver':
            self.deliver = value

    # O(1)
    def lookup(self, par):
        if par == 'pID':
            print(self.pID)
        elif par == 'address':
            print(self.address)
        elif par == 'city':
            print(self.city)
        elif par == 'state':
            print(self.state)
        elif par == 'zipC':
            print(self.zipC)
        elif par == 'deadline':
            print(self.deadline)
        elif par == 'weight':
            print(self.weight)
        elif par == 'status':
            print(self.status)
        elif par == 'truck':
            print(self.truck)

    # O(1)
    def info(self):
        print("\nPackage ID: {}\n"
              "    Address: {}\n"
              "    City: {}\n"
              "    State: {}\n"
              "    Zip: {}\n"
              "    Deadline: {}\n"
              "    Weight: {}".format(self.pID,self.address, self.city, self.state,
                                    self.zipC, self.deadline, self.weight))

