'''Write a Python function to find the sum of digits of a number.'''
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))
print(sum_of_digits(123))