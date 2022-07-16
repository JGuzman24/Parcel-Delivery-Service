# Parcel-Delivery-Service
This program is designed to import a list of packages and address distance table (as CSV files) and find an efficient path to deliver all packages. The program scales with number of packages to deliver, unique addresses, and available delivery trucks.

# Delivery Algorithm 
The main feature of the program is the delivery algorithm. 

From the imported CSV files:
- An adjacency list is created based on the trucks' current location
- The packages loaded onto the truck creates a list of delivery addresses that must be reached at least once

From there dijkstra's algorithm is used to find a path to the closest delivery address to the truck. This process is repeated until all packages have been delivered. 

# User Interface
Interface is designed from the perspective of a logistics operator searching for information on the delivery trucks or packages. 

The users can select from the following actions:
* View full delivery log for all trucks
* View total mileage driven for all trucks
* View status of a specific package (based on package ID) at a specific time
* View status of all packages at a specific time

# Built With
  * Python 3 using JetBrains' PyCharm IDE
  * Imports standard CSV files



