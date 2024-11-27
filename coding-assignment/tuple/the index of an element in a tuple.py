'''Find the index of an element in a tuple.'''

# Solution 1:
def find_index(tup, value):
    return tup.index(value)

# Solution 2:
tup = (10, 20, 30, 40, 50)
index = tup.index(30)
print(index)
