#Name: Conor Smith
#Date: 05/05/21
#Description: A function that finds a median from a list of numbers

def find_median(some_nums):
  """takes a parameter of a list of numbers, and puts them in order. If odd picks the middle number. if even finds the avg of the two middle numbers"""
  sort = sorted(some_nums) #sorts list
  mid = len(some_nums) // 2 #mid variable finds length of list uses floor division
  if len(some_nums) % 2:
    return sort[mid]
  else:
    median = (sort[mid] + sort[mid - 1]) / 2 #for even numbers, finds avg of two middle numbers
    return median
#print(find_median([13,7,8,82,4]))