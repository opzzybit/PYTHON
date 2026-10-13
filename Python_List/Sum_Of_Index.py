def sum_of_lists(number1,number2,number3,number4,number5,number6):
    opzzy_list = [number1,number2,number3,number4,number5,number6]
    
    sum_of_list = 0
    for number in range (len(opzzy_list)):
        sum_of_list = opzzy_list[0] + opzzy_list[1] + opzzy_list[5]
    return sum_of_list

output = sum_of_lists(10,3,7,6,12,8)

print (f"the total of the first, second, and last index is = {output}")


