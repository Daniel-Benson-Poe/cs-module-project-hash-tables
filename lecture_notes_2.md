Slot
Index Chain (linked list)
----- -----------------------
0     ('quix', 10) -> None
1     ('plugh', 20) -> ('foo', 12) -> None
2     ('xyzzy', 50) -> ('baz', 999) -> ('bar', 30) -> None
3     -> None

put("foo", 12)  # hashes to 1
put("bar", 30)  # hashes to 2
put("baz", 999)  # hashes to 2 --collision
put("qux", 10)  # hashes to 0
put("plugh", 20)  # hashes to 1 (collision)
put("xyzzy", 50)  # hashes to 2 (collision)

get("bar")  # should give us 30 from index 2

Algorithm GET:
    get the index for the key
    search the linked list at that index for the entry for that key
    return the value (or None if not found)

Algorithm PUT:
    get the index for the key
    search the list for the key
    if it exists, overwrite the value
    else, insert the [key, value] at the head of the linked list at that slot