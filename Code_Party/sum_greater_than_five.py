given_tuple_list = [(1, 2), (3, 4), (5,6)]
from functools import reduce
def sum_of_each_tuple(accumulator,numbers):
    new_tuple_list = []
    new_tuple_list = accumulator + numbers
    return new_tuple_list[0] + new_tuple_list[1]
    
result = list(reduce(sum_of_each_tuple,given_tuple_list))
print(result)
