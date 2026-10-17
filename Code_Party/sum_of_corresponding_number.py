def sum_of_the_corresponding_number(numbers):
    
    result = [[],[],[]]
  
    
    sum_up = [0,0,0]
    for adder in numbers:
        sum_up[0] += adder[0]
        sum_up[1] += adder[1]
        sum_up[2] += adder[2]
        result = sum_up[0], sum_up[1],sum_up[2]
    
    print(numbers)
    return result
    
result_number = sum_of_the_corresponding_number([[2,3,4,],[1,5,7],[4,6,8]])
print ("the sum of the dimensional array = ",list(result_number))
	
