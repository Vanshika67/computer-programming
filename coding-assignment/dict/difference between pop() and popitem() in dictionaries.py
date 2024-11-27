'''What is the difference between pop() and popitem() in dictionaries?'''

my_dict = {"name": "Alice", "age": 25}
name = my_dict.pop("name")
print(name)  # Output: Alice

key_value = my_dict.popitem()
print(key_value)
