'''Write a Python program to capitalize the first letter of each word in a sentence.'''
def capitalize_first_letter(input_string):
 return " ".join(word.capitalize() for word in input_string.split())      
