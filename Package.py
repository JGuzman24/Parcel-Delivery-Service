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

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.pID, self.address, self.city, self.state,
                                                   self.zipC, self.deadline, self.weight, self.status)

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
