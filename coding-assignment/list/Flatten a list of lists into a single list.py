'''Flatten a list of lists into a single list.'''
def flatten_list(lists):
   return [item for sublist in lists for item in sublist]   
