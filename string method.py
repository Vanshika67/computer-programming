# 1. Create a String
s = "Hello, Python!"

# 2. Access characters
print("First character:", s[0])      # H
print("Last character:", s[-1])     # !

# 3. String Slicing
print("First 5 characters:", s[:5])  # Hello
print("Characters from index 7:", s[7:])  # Python!

# 4. String Length
print("Length of string:", len(s))

# 5. String Methods
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
print("Replace:", s.replace("Python", "World"))
print("Split:", s.split(","))   # Split into list by comma

# 6. Check substring
print("Contains 'Python'? :", "Python" in s)
print("Contains 'Java'? :", "Java" in s)

# 7. Concatenation
s1 = "Hello"
s2 = "World"
print("Concatenation:", s1 + " " + s2)

# 8. String Formatting
name = "Vanshika"
age = 20
print(f"My name is {name} and I am {age} years old.")

# 9. Loop through string
for ch in "Cat":
    print(ch)

# 10. Reverse a string
rev = s[::-1]
print("Reversed String:", rev)
