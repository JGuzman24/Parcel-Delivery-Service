from hash import HashTable
from Package import  Package
import csv

def load_package_data(file):
    with open(file) as packages:
        my_hash = HashTable()
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
            status = package[7]

            package = Package(pID, address, city, state, zipC, deadLine, weight, status)

            my_hash.insert(pID, package)
        return my_hash
