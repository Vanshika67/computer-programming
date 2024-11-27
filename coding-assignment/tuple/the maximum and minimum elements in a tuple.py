'''Find the maximum and minimum elements in a tuple.'''

# Solution:
def max_min_elements(tup):
    return max(tup), min(tup)

tup = (5, 8, 2, 10, 3)
max_element, min_element = max_min_elements(tup)
print("Max:", max_element)  
print("Min:", min_element) 
