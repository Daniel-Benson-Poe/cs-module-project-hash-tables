Hash Tables
------------

What problem are we solving with this data structure?

Quick O(1) searches:

["Lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit"]
    0       1         2       3       4         5               6          7

Hashing function:
f("dolor") -> 2
f("dolor") -> 2
f("dolor") -> 2
f("dolor") -> 2
f("consectetur") -> 5
f("beej") -> 5

Hash table: key-value store with a particular structure and O(1) time complexity
Python dict: basically is a hash table
General "Dictionary" equivalent to key-value store
Key-value store is a data structure that will return a value for a given key

"beej".encode() -> b'beej'
b = "beej".encode()
for i in b()
    print(i)
-> 66
-> 101
-> 101
-> 106
b.decode()
-> 'beej'

table = [None] * 8

def hashf(s):
    """Super-naive hashing function -- do NOT use"""

    b = s.encode() # get the bytes of the string

    total = 0

    for i in b:  # O(n) over the size of the key, O(1) over the size of the hash table
        total += i
    
    return total

def get_index(key):
    index_value = hashf(key)
    index_value %= len(table) # mod to get value somewhere between 0 and 8 (length of the table)
    return index_value

print(hashf("Beej"))
print(hashf("Goats"))

def put(key, value):  # O(1) over the size of the hash table
    # Which slot(aka index) in the table is the value going?
    index = get_index(key)
    # store the value at that slot
    table[index] = value

def get(key):
    index = get_index(key)

    return table[index]

def delete(key):
    index = get_index(key)

    table[index] = None

put("Beej", 3490)
print(get("Beej")) -> 3490
delete("Beej")
print(get("Beej")) -> None

print(table)
