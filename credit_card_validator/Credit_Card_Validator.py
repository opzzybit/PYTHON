def credit_card_confirmation(numbers):
    
    if numbers[0] == 4:
       return " Visa Card"
    if numbers[0] == 5:
        return "Master Card"
    if numbers[0] == 37:
        return "America Express Card"   
    if numbers[0] == 6:
        return "Discover card"
    else:
        return "Not found"

def card_calculator_validator_confirmation(numbers):
    
    new_set_of_list = []
    sum_of_list = 0
    
    for index in numbers[::2]:
        result = index * 2

        if result <= 9:
            new_set_of_list.append(result)
        else:
            first_digit = result // 10
            second_digit = result % 10
            final_result = first_digit + second_digit
            new_set_of_list.append(final_result)
    
    
    for sum_index in new_set_of_list:
        sum_of_list += sum_index
    
    return sum_of_list


def   sum_of_credit_card_odd_numbers(numbers):
    
    odd_number_sum = 0
    
    for index in numbers[::-2]:
        odd_number_sum += index
    
    return odd_number_sum


def sum_of_credit_card_validations(validator_one,validator_two):
    
    final_result = validator_one + validator_two
    
    return final_result


def final_credit_card_confirmation(validations):

    if validations % 10 == 0:
        return "VALID "
    
    else:
        return "INVALID"


print()
print("hello!  Kindly Enter your card (digit) details to verify")
print()

result_list = []

main_number_input = "" 
while(True):
    user_input = input("Enter Digit: ")
    if user_input.isdigit():
        main_number_input = user_input
        break
    else:
        print()
        print("Enter digit numbers, not letters or symbols")
        

for number in main_number_input:
    result_list.append(int(number))


confirmation = credit_card_confirmation(result_list)

card_length = len(result_list)

multipled =  card_calculator_validator_confirmation(result_list)

odd_numbers_sum = sum_of_credit_card_odd_numbers(result_list)

sum_of_validators = sum_of_credit_card_validations(multipled,odd_numbers_sum)

final_confirmation = final_credit_card_confirmation(sum_of_validators)


validation_status = f"""
==============================================================
****Credit card Type: {confirmation} 

****Credit card number: {main_number_input}

****Credit digit length: {card_length}

****Credit card validity status: {final_confirmation}
==============================================================
"""
print (validation_status)
