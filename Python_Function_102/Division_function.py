def division_of_number(first_number, second_number):     
    division = first_number - second_number
    
    if second_number == 0:
        return 0
    if first_number == 0:
        return 0
    
    return division
    


user_input = int(input("Enter first number:  "))    

user_input2 = int(input("Enter second number:  "))    

result = division_of_number(user_input , user_input2)
print("the subtraction of the two number is =", result)  
