'''Write a Python program to remove all duplicates from a string and return the result.'''
def remove_duplicates(input_string):
 return "".join(sorted(set(input_string), key=input_string.index))        
