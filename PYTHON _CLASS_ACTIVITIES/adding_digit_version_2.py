def sum_of_the_inputed_digit(index):
  
  while(True):
      if index >= 10:
          first_digit = index // 10
          second_digit = index % 10
          final_result = first_digit + second_digit
     
       
          first_result = final_result // 10 
          second_result = final_result % 10
          final_result_two = first_result + second_result
        
          first_digit_three = final_result_two // 10
          second_digit_three = final_result_two % 10
          return first_digit_three + second_digit_three

      
      elif index < 0:
          first_digit = index // -10
          second_digit = index % -10
          negative_result = first_digit + second_digit
     
       
          first_result = negative_result // -10 
          second_result = negative_result % -10
          negative_result_two = first_result + second_result
        
          first_result_two = negative_result_two // -10
          second_result_two = negative_result_two % -10
          negative_result_three = first_result_two + second_result_two

          first_result_three = negative_result_three // -10
          second_result_three = negative_result_three % -10
          return first_result_three - second_result_three






user_input = int(input("Enter any number:  "))
result = sum_of_the_inputed_digit(user_input)
print(result)
