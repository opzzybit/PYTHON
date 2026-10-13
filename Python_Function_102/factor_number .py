def factor_of_number(number):
  
    for factor in range (2,number):
        
        if  number % factor == 0:
        
        return factor 


user_input = int(input("Enter any number:  "))  
result = factor_of_number(user_input)

print (f"The factor of the number is {result}")
