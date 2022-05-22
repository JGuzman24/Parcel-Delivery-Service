class HashTable:

    # O(N)
    def __init__(self, initial_capacity):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # O(N)
    def insert(self, key, item):
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update item if key already in bucket
        for value in bucket_list:
            if value[0] == key:
                value[1] = item
                return True

        # insert item at the end of bucket
        new_value = [key, item]
        bucket_list.append(new_value)

    # O(N)
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        for key_value in bucket_list:
            if key_value[0] == key:
                return key_value[1]
            else:
                return None

    # O(N)
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for key_value in bucket_list:
            if key_value[0] == key:
                bucket_list.remove(key_value)
            else:
                return None

