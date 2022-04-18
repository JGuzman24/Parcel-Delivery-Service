
from Package import Package
from importCSV import load_package_data

my_hash = load_package_data('WGUPS Package File.csv')

print(my_hash.search(9).address)

p9 = Package(9, 'Whats State St', 'Salt Lake City', 'UT', '84111', 'EOD', 2, '')

my_hash.insert(9, p9)

print((my_hash.search(12)).state)

print(my_hash.search(32).address)

print(my_hash.search(9))

p9.update('address', '123 Updated Road')

print(my_hash.search(5))

my_hash.search(5).update('address', 'Holy Shit it worked')

print(my_hash.search(5))

for i in range(len(my_hash.table)):
    print("Package: {}".format(my_hash.search(i + 1)))





