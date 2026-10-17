def sum_of_two_dimensional_list(numbers):
    

    result = [[],[],[]]
  
    
    sum_up = [0,0,0]
    for adder in numbers[0]s:
        sum_up[0] += adder
        result[0] = sum_up[0]
    
    for adder_2 in numbers[1]:
        sum_up[1] += adder_2
        result[1] = sum_up[1]
    
    for adder_3 in numbers[2]:
        sum_up[2] += adder_3
        result[2] = sum_up[2] 
    
    print(numbers)
    return result
    
result_number = sum_of_two_dimensional_list([[2,3,4,],[1,5,7],[4,6,8]])
print ("the sum of the dimensional array = ",result_number)
