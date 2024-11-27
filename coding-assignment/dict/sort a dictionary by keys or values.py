'''How do you sort a dictionary by keys or values?'''

my_dict = {"name": "Alice", "age": 25, "city": "New York"}
sorted_by_keys = sorted(my_dict.items())
print(sorted_by_keys)  
sorted_by_values = sorted(my_dict.items(), key=lambda x: x[1])
print(sorted_by_values) 
