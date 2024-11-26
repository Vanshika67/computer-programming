'''Write a Python function to find the Fibonacci sequence up to a given number n.'''

def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib
print(fibonacci(5)) 
