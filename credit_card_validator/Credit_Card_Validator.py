def get_credit_card_type(numbers):
    
    if numbers[0] == 4:
       return " Visa Card"
    elif numbers[0] == 5:
        return "Master Card"
    elif numbers[0] == 3 and numbers[1] == 7:
        return "America Express Card"   
    elif numbers[0] == 6:
        return "Discover card"
    else:
        return "Not found"

def get_credit_card_length(numbers):
  length_of_numbers = len(numbers)
  return length_of_numbers

def get_confirmation_of_credit_card_length(numbers):
    if len(numbers) <= 16:
        print()
        return "Valid card length"
    else : 
        print()
        return "Error Message: you exceeded the card limit (13 or 16 length)"

def sum_of_card_second_digit_from_right_to_left(index):
    
    new_set_of_list = []
    sum_of_list = 0
    
    for numbers in index[::2]:
        result = numbers * 2

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


def sum_of_credit_card_odd_numbers(index):
    
    odd_number_sum = 0
    
    for numbers in index[::-2]:
        odd_number_sum += numbers
      
    return odd_number_sum


def sum_of_credit_card_validations(validator_one,validator_two):
    
    result = validator_one + validator_two
    
    
    return result


def final_credit_card_confirmation(validations):

    if validations % 10 == 0:
        return "VALID "
    
    else:
        return "INVALID"


print()
print("hello!  Kindly Enter your card (digit) details to verify \n\t The Digit length must be between 13 and 16")
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


type_confirmation = get_credit_card_type(result_list)

card_length = get_credit_card_length(result_list)

card_length_confirmation = get_confirmation_of_credit_card_length(result_list)


multipled =  sum_of_card_second_digit_from_right_to_left(result_list)

odd_numbers_sum = sum_of_credit_card_odd_numbers(result_list)

sum_of_validators = sum_of_credit_card_validations(multipled,odd_numbers_sum)

final_confirmation = final_credit_card_confirmation(sum_of_validators)


validation_status = f"""
======================================================================
        {card_length_confirmation}

****Credit card Type: {type_confirmation} 

****Credit card number: {main_number_input}

****Credit digit length: {card_length}

****Credit card validity status: {final_confirmation}
=======================================================================
"""
print (validation_status)
