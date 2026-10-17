number_list = list(range(1,11))
def square_of_the_numbers(numbers):
    return numbers ** 2
    
result = list(map(square_of_the_numbers,number_list))
print("the squared numbers = ",result)
