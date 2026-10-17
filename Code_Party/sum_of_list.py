number_list = list(range(1,51))
from functools import reduce
def sum_of_the_list(accumulator,numbers):
    return accumulator + numbers
    
result = reduce(sum_of_the_list,number_list)
print("the sum of all the element in the list  = ",result)
