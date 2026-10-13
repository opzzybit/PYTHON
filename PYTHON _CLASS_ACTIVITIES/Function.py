print()
print("          CALCULATOR  FUNCTION    ")
print()

def addition_of_number(first_number, second_number):
    addition = first_number + second_number
    return addition
     
def subtraction_of_number(first_number, second_number):     
    subtraction = first_number - second_number
    return subtraction

def multiplication_of_number(first_number, second_number):     
    multiplication = first_number *  second_number
    return multiplication

def division_of_number(first_number, second_number):     
    division = first_number / second_number
    return division

def expontential_of_number(number, power):     
    expontential = number ** power
    return expontential


result  = addition_of_number(20, 10)

result_two = subtraction_of_number(30, 40)

result_three = multiplication_of_number(10, 5)

result_four = division_of_number(100, 10)

result_five = expontential_of_number(50, 2)


print("the addition of the two number is =" ,result)
print("the subtraction of the two number is =", result_two)
print("the multiplication of the two number is =", result_three)
print("the division of the two number is =", result_four)
print("the expontential of the two number is =", result_five)
