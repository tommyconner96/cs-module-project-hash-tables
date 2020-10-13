# A hash function needs to take a string and return a single number
# It must be deterministic (i.e the same result every time given the same input)
def hash_fn(s): 
    # convert the string to a UTF-8 (Unicode) representation
    encoded_string = s.encode() # O(1)
    result = 0
    # every character is now a number based off UTF-8 rules
    for byte_char in encoded_string:
        # simply add the numbers up to get one single new number
        result += byte_char
    
    return result

# print(hash_fn("banana")) # => 609
# print(hash_fn("apple")) # => 530

# Lets map the result of hash_fn to an index in some array
# we create an array of size 8
hash_array = [None] * 8
# we can use modulo to bind the number from hash_fn to 0 -> length of the array

# Store banana inside hash_array
# Banana is the key
# Banana is yellow is the value
hash_value = hash_fn("banana") # 609
index = hash_value % len(hash_array)
hash_array[index] = ("banana","banana is yellow")

# Store apple inside hash_array
hash_value = hash_fn("apple") # 530
print(f'apple hashed to the number {hash_value}')
index_of_apple = hash_value % len(hash_array)
print(f'Apple will go into index {index_of_apple}')
hash_array[index] = ("apple", "apple is green")

# Store eggg inside hash_array
## THIS WILL COLLIDE WITH APPLE

# egg_hash_value = hash_fn("eggg") #410
# print(f'egg hashed to the number {egg_hash_value}')
# index_of_egg = egg_hash_value % len(hash_array)
# print(f'Eggg will go into index {index_of_egg}')
# hash_array[index_of_egg] = ("eggg", "This will replace apple")


# Look up Banana in hash_array
# Get the index value for Banana
hash_value = hash_fn("banana") # 609 #O(N) but N === Length of String which is usually very small compared to Array
index = hash_value % len(hash_array) #O(1)


# -------- SUMMARY --------- (i.e lets convert the above into reusable functions)
# Hash function + An Array == Hash_table

# To insert a key and value to this hash_table
# - hash the key to convert it to a number
# - take that number and MOD it by the size of hash_table
# - insert the VALUE into the index given by the MOD operation
def insert_to_hash_table(key, value):
    hash_value = hash_fn(key)
    index = hash_value % len(hash_array)
    hash_array[index] = (key, value)

# To retrieve a value given a specific key from a hash_table
# - hash the key to convert it to a number
# - use MOD to find the index within the underlying array
# - use this new index to find the value in the array
def get_from_hash_table(key):
    hash_value = hash_fn(key)
    index = hash_value % len(hash_array) # convert the number into a new number between 0 - len(array)
    return hash_array[index]
