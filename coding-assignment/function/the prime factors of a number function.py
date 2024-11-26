''' Write a program to find out the prime factors of a number. Example: prime factors of 56 - 2, 2, 2, 7'''
import math

prime_list = []

def primeFactors(num):
   
    
   
    while num % 2 == 0:
        prime_list.append(2)
        num = num/2
        
    
while num % 2 == 0:
        prime_list.append(2)
        num = num/2
        
    
    for i in range(3, int(math.sqrt(num))+1, 2):
        while num%i == 0:
            prime_list.append(i)
            num = num/i

   
    if num > 2:
        num = int(num)
        prime_list.append(num)
    return prime_list
        
primeFactors(56)
