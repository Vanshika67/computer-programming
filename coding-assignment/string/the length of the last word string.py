'''Write a Python program to find the length of the last word in a sentence.'''
def length_of_last_word(input_string):
  words = input_string.split()
  if words:
    return len(words[-1])
    return 0        
