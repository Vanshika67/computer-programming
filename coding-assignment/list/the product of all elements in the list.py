'''Calculate the product of all elements in the list.'''
from functools import reduce
import operator
def product_of_elements(nums):
   return reduce(operator.mul, nums, 1) 
