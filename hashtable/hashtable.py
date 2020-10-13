class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    """
    # day 1

    def __init__(self, capacity=MIN_CAPACITY):
        self.capacity = capacity
        self.hash_array = [None] * self.capacity
        self.item_count = 0

    # day 1
    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        """
        num_slots = len(self.hash_array)
        return num_slots

    # day 2
    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        """
        load_factor = self.item_count / self.capacity
        return load_factor

    # day 1 or 2
    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        """
        pass

    # day 1
    def djb2(self, key):

        hash = 5381

        for x in key:
            hash = (hash * 33) + ord(x)

        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    # day 1
    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.
        """
        cur_index = self.hash_index(key)

        if self.hash_array[cur_index] is not None:
            if self.hash_array[cur_index].key == key:
                head = HashTableEntry(key, value)
                head.next = self.hash_array[cur_index].next
                self.hash_array[cur_index] = head
            else:
                head = HashTableEntry(key, value)
                head.next = self.hash_array[cur_index]
                self.hash_array[cur_index] = head
                self.item_count += 1
        else:
            self.hash_array[cur_index] = HashTableEntry(key, value)
            self.item_count += 1

    # day 1
    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.
        """
        cur_index = self.hash_index(key)

        if self.hash_array[cur_index] is not None:

            if self.hash_array[cur_index].key == key:
                old_head = self.hash_array[cur_index]
                self.hash_array[cur_index] = self.hash_array[cur_index].next
                old_head.next = None
                self.item_count -= 1
                return old_head
            while self.hash_array[cur_index].next is not None:
                if self.hash_array[cur_index].next.key == key:
                    self.hash_array[cur_index].next = None
                    self.item_count -= 1

        print("warning: key not found")

    # day 1
    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.
        """
        cur_index = self.hash_index(key)
        node = self.hash_array[cur_index]

        if node is not None:
            while node.next is not None and node.key is not key:
                node = node.next
            if node.key == key:
                return node.value
            else:
                return
        else:
            return None

    # day 2

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        """
        hash_array_copy = self.hash_array.copy()
        self.hash_array = [None] * new_capacity
        self.capacity = new_capacity

        for i in range(len(hash_array_copy)):
            node = hash_array_copy[i]
            # if node is None:
            #     return
            # else:
            while node is not None:
                self.put(node.key, node.value)
                node = node.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    # testing printing all lines
    for i in range(1, 12):
        print(ht.get(f"line_{i}"))
    print(ht.get("line_10"))

    # testing "key not found" for delete
    print(ht.delete("line_13"))  # expected "warning: key not found"

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))
    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
