number_list = [1, 2, 3, 4]
from functools import reduce
def squared_number(numbers):
    return numbers ** 2

def products_of_the_squared(accumulator,numbers):
    return accumulator * numbers
    
result = list(map(squared_number,number_list))
print("squared list = ",result)
print("the product of the squared = ",reduce(products_of_the_squared,result))
