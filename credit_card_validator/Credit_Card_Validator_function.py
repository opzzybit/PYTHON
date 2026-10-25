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



