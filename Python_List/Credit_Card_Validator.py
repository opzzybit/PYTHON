def credit_card_validator(numbers):
    
    card_number = []
    
    adder = 1
    for index in numbers:
        if  index[-adder]:
            card_number.append(index)
            adder += 2
    
    return card_number
    
    
    
    
result_list = []
for number in range (1,17):
    user_input = int(input("Enter your card number:  "))
    result_list.append(user_input)

result = credit_card_validator(result_list)
print(result)
