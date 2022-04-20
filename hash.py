# HashTable class using chaining.
class HashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=41):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table.
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

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        for key_value in bucket_list:
            # looks for key in bucket list
            if key_value[0] == key:
                # returns item if found
                return key_value[1]
            else:
                # the key is not found.
                return None

    # Removes an item with matching key from the hash table.
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for key_value in bucket_list:
            if key_value[0] == key:
                bucket_list.remove(key_value)
            else:
                return None

    #def update(self, key, item, value):

