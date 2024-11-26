'''Write a Python program to count the occurrences of each word in a sentence.'''
def count_word_occurrences(input_string):
 words = input_string.split()
 word_count = {}
 for word in words:
     word_count[word] = word_count.get(word, 0) + 1  
