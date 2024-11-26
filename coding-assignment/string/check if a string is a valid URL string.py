'''Write a Python program to check if a string is a valid URL.'''
import re
def is_valid_url(url):
   pattern = r'^https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
   return bool(re.match(pattern, url)) 
