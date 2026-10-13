def sorted_prime_number(numbers):
    sorted_number_list = []
    for number in numbers:
        if number <  1:
            continue
            
        prime = True
        for index in range(2, number):
            if number % index == 0:
                prime = False
                break
        
        if prime:
            sorted_number_list.append(number)
            
    return sorted_number_list   

inputed_number = sorted_prime_number([5,9,2,6,3])
print(inputed_number)



def replacing_negative_number(numbers):

    replace_list = []
    for index in numbers:
        if index < 0 :
            index = 0
        replace_list.append(index)
        
    return replace_list

inputed_number = replacing_negative_number([5,-9,3,-6,2,-11])
print(inputed_number)




def displacing_the_number(numbers):
    
    displace_list_zero = []
    displace_list_not_zero = []
    for index in numbers:
        if index == 0 :
            displace_list_zero.append(index)
        else:
             displace_list_not_zero.append(index)
    
    return displace_list_not_zero + displace_list_zero
    
inputed_number = displacing_the_number([5,0,3,0,2,0])
print(inputed_number)
    
    
    
    

def duplicate_numbers(numbers):


    print(numbers)
    
    new_duplicate_list = numbers
    
    count = 0
    compare = numbers[count]
    for index in range (len(numbers)):
        if numbers[0] == compare:
            new_duplicate_list.pop(0) 
            continue
        
    return new_duplicate_list 
    
inputed_number = duplicate_numbers([45,60,3,0,67,2,45,3,22,0])
print(inputed_number)
        
    
