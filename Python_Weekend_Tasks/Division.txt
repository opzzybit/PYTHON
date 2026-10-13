def subtraction_of_number(first_number, second_number):     
    subtraction = abs(first_number - second_number)
    return subtraction
    


user_input = int(input("Enter first number:  "))    

user_input2 = int(input("Enter second number:  "))    

result = subtraction_of_number(user_input , user_input2)
print("the subtraction of the two number is =", result)  
