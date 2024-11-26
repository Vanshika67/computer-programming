'''Write a Python program to find the longest word in a sentence.'''
def longest_word(input_string):
 words = input_string.split()
 return max(words, key=len)    
