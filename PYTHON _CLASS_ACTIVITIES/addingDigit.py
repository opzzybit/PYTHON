print("      ADDING CALCULATOR   ")

user_input = int(input("Enter any  number :  "))
# FOR TENTH
first_digit = user_input // 10
second_digit = user_input % 10
final_result = first_digit + second_digit
    
#FOR HUNDREDTH
first_digit_two = final_result // 10
second_digit_two = final_result % 10
final_result_two = first_digit_two + second_digit_two

#FOR THOUSAND 
first_digit_three = final_result_two // 10
second_digit_three = final_result_two % 10
final_result_three = first_digit_three + second_digit_three

#FOR TEN THOUSAND
first_digit_four = final_result_three // 10
second_digit_four = final_result_three % 10
final_result_four = first_digit_four + second_digit_four

#FOR HUNDRED THOUSAND
first_digit_five = final_result_four // 10
second_digit_five = final_result_four % 10
final_result_five = first_digit_five + second_digit_five

# FOR MILLION 
first_digit_six = final_result_five // 10
second_digit_six = final_result_five % 10
final_result_six = first_digit_six + second_digit_six


# FOR TEN MILLION 
first_digit_seven = final_result_six // 10
second_digit_seven = final_result_six % 10
final_result_seven = first_digit_seven + second_digit_seven


# FOR HUNDRED MILLION 
first_digit_eight = final_result_seven // 10
second_digit_eight = final_result_seven % 10
final_result_eight = first_digit_eight + second_digit_eight

# FOR BILLION 
first_digit_nine = final_result_eight // 10
second_digit_nine = final_result_eight % 10
final_result_nine = first_digit_nine + second_digit_nine

print(f"The sum of each digit you inputted = {final_result_nine}")
