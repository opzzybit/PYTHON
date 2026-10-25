from Credit_Card_Validator_function import *
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
