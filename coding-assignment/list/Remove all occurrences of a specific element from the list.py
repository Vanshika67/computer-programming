'''Remove all occurrences of a specific element from the list.'''
def remove_all_occurrences(nums, target):
  return [num for num in nums if num != target]  
