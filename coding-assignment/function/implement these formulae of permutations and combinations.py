'''Write a program to implement these formulae of permutations and combinations.
Number of permutations of n objects taken r at a time: p(n, r) = n! / (n-r)!.

Number of combinations of n objects taken r at a time is: c(n, r) = n! / (r!*(n-r)!) = p(n,r) / r!'''

import operator as op

def factorial(num):
   
    
    if num == 1:
        return num
    return num * factorial(num-1)

def permutation(n, r):
    
return int(factorial(n) / factorial(n-r))

def combination(n, r):
   
    return int(factorial(n) / (factorial(r) * factorial(n-r)))

print("Permutation: ", permutation(15,4))
print("Combination: ", combination(15,4))
