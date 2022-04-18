from hash import HashTable

hash = HashTable()

hash.insert(1, 'Justin Guzman')
hash.insert(2, 'Britany Guzman')
hash.insert(3, 'Nova Guzman')

print(hash.table)

hash.insert(4, 'Some other douche')

print(hash.table)

hash.search(3)

hash.remove(4)

print(hash.table)