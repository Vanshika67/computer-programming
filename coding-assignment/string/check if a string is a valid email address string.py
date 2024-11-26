'''Write a Python program to check if a string is a valid email address.'''
import re
def is_valid_email(email):
  pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
  return bool(re.match(pattern, email)) 
