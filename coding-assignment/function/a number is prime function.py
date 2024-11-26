'''Write a Python function to check if a number is prime.'''

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


print(is_prime(7))  
print(is_prime(10))
