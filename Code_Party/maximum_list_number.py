number_set = [3, 5, 9, 2, 8]
from functools import reduce
def maximum_or_largest_number(accumulator,numbers):
    return max(accumulator,numbers)
result = reduce(maximum_or_largest_number,number_set)
print("the largest element in the list  = ",result)   
