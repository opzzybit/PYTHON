def list_addition(number1,number2,number3,number4,number5,number6):
    opzzy_list = [number1,number2,number3,number4,number5,number6]
    
    sum_of_third_list = 0
    for number in range (len(opzzy_list)):
        sum_of_third_list = opzzy_list[2] + opzzy_list[5]
    return sum_of_third_list

output = list_addition(2,6,7,4,5,9)

print (f"the total of the third index is = {output}")


