#ADDING PERCENTAGE  
given_prices = [100, 200, 300]
def adding_percentage_number_list(numbers):
    percentage = numbers * 0.10
    total = numbers + percentage 
    return int(total)
result = list(map(adding_percentage_number_list,given_prices))
print(f"10% added to the numbers  = {result}")




#SORTING NUMBERS DIVISIBLE BY 3
print()
divisible_number = list(range(1,52))
def checking_divisible_index (numbers):
    return numbers % 3 == 0 and numbers % 5 == 0
new_divisible_number = list(filter(checking_divisible_index, divisible_number))
print(divisible_number)
print()
print(f"number divisible by 3 and 5  from 1-51 = {new_divisible_number}") 




#SORTING EVEN NUMBERS
print()
number_list = list(range (1,22))
def even_number_list (numbers):
        return numbers % 2 == 0    

new_list_number = list(filter(even_number_list, number_list))
print(number_list)
print()
print(f"Even number from 1-21 = {new_list_number}")




#ADDING ANOTHER FRUIT TO THE LIST OF FRUITS
print()
fruit_tuple = ('Apple','Banana','Cherry')

new_fruit_list = []

new_fruit_list += fruit_tuple
new_fruit_list.append('Mango')
print(fruit_tuple)
print(tuple(new_fruit_list))




#TWO DIMENSIONAL ARRAY SUM
print()
def sum_of_two_dimensional_list(numbers):
    result = [[],[],[]]
  
    
    sum_up = [0,0,0]
    for adder in numbers[0]:
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




#REDUCE METHOD MAXIMUM NUMBER 
print()
number_set = [3, 5, 9, 2, 8]
from functools import reduce

def maximum_or_largest_number(accumulator,numbers):
    return max(accumulator,numbers)

result = reduce(maximum_or_largest_number,number_set)
print("the largest element in the list  = ",result)   




#CHANGING INDEX NUMBER IN A LIST
print()
numbers = (1,2,[3,8],5,)

number_sliced = []
new_set_numbers = []
new_set_numbers += numbers
new_set_numbers[2] += number_sliced

sliced = numbers[2]
sliced[1] = 99
number_sliced = sliced

for index in numbers:
    new_set_numbers = numbers 

print("the changed two element in the third element = " ,numbers)





#ADDING UP WORDS
print()
message = ['I', 'love', 'Python'] 
from functools import reduce
def adding_the_words_in_the_string(accumulator,words):
    
    return accumulator + " " + words
    
words = reduce(adding_the_words_in_the_string,message)
print(words)





#SQUARED AND PRODUCT OF LIST NUMBER
print()
number_list = [1, 2, 3, 4]
from functools import reduce
def squared_number(numbers):
    return numbers ** 2

def products_of_the_squared(accumulator,numbers):
    return accumulator * numbers
    
result = list(map(squared_number,number_list))
print("squared list = ",result)
print("the product of the squared = ",reduce(products_of_the_squared,result))





#SUM AND ALSO GETTING NUMBER GREATER THAN FIVE IN THE LIST 
print()
given_tuple_list = [(1, 2), (3, 4), (5,6)]

def sum_of_each_tuple(numbers):
    
    sum_of_index = 0
    sum_of_index += numbers[0] + numbers[1]
    return sum_of_index

def checking_number_greater_than_five_in_list(numbers):   
    if numbers > 5:
        return numbers


print (given_tuple_list)
result = list(map(sum_of_each_tuple,given_tuple_list))
print(f"The sum of each tuple in the list = {result}")

result_two = list(filter(checking_number_greater_than_five_in_list,result))
print(f"numbers grater than five in the sum list = {result_two}")



#SUM OF NUMBERS FROM 1-50 USING REDUCE 
print()
number_list = list(range(1,51))
from functools import reduce
def sum_of_the_list(accumulator,numbers):
    return accumulator + numbers
    
result = reduce(sum_of_the_list,number_list)
print("the sum of all the element in the list  = ",result)



#SQUARE OF NUMBERS 1-10 IN THE LIST
print()
number_list = list(range(1,11))
def square_of_the_numbers(numbers):
    return numbers ** 2
    
result = list(map(square_of_the_numbers,number_list))
print("the squared numbers = ",result)



#SORTING OUT NON-NUMERIC ELEMENT IN A  LIST AND CONVERTING THEM TO INTEGERS THEN SUM THE INTEGERS
print()
given_data = ['123', '456', '789','abc', 'def']
from functools import reduce
def sorting_out_non_numeric_string(strings):
    numeric_list = []
    
    if strings.isdigit():
        numeric_list.append(strings)
    else:
        return strings

def converting_non_numeric_to_integer(strings):
    
    new_string_list = 0
    if strings == 'abc':
        new_string_list = 124
    elif strings == "def":
        new_string_list = 568
    
    return new_string_list   


def sum_of_the_non_numeric_list(accumulator,numbers):
     result = 0
     result += accumulator + numbers
     return result

string_result = list(filter(sorting_out_non_numeric_string,given_data))
print("the non_numeric strings",string_result)

string_result_two = list(map(converting_non_numeric_to_integer,string_result))
print("converted string  = ",string_result_two)

string_result_three = reduce(sum_of_the_non_numeric_list,string_result_two)
print("total sum of the converted string = ",string_result_three)




#SORTING PALINDROME
print()
words_list = ['level','world', 'madam', 'python']
def reversing_the_word(words):
    palindrome = words[::-1]
    return palindrome == words
    
result = list(filter(reversing_the_word, words_list))
print("sorted palindrome = ", result)




#CAPITALIZING  THE FIRST LETTER 
print()
given_names = ['john', 'mary', 'steve']
def capitalizing_the_first_letter(words):
    return words.capitalize()
 
result = list(map(capitalizing_the_first_letter,given_names))
print(f"converted first letter to uppercase = {result}")


#CONVERTING ALL THE FIRST LETTER TO UPPERCASE
print()
given_strings = ['python', 'java', 'c++']
def converting_the_first_letter_to_uppercase(words):
    return words.capitalize()
 
result = list(map(converting_the_first_letter_to_uppercase,given_strings))
print(f"the first letter to uppercase = {result}")



#SUM OF CORRESPONDING NUMBERS IN A ARRAY
print()
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



#SORTING NUMBER GREATER THAN TWO IN A TUPLE
print()
mixed_list = [(1,'A'),(4,'B'),(2,'C')]
def sorting_out_index_greater_than_two(numbers):
	return  numbers[0] > 2
			
result = list(filter(sorting_out_index_greater_than_two,mixed_list))
print ("the index is = " ,result)
	

#ADDING MORE NUMBERS TO A ALREADY GIVEN SET OF TUPLE
print()
my_list = (30,20,40,50)
print(my_list)
my_list += (10,40) 

my_new_list = ()

my_new_list += my_list
print("the new tuple =", my_new_list)



#UNPACKING A SET OF TUPLE
print()
upacked_tuple_number = (10,20,30,40)
print (upacked_tuple_number)
number_1,number_2,number_3,number_4 = upacked_tuple_number

upack_one = number_1
upack_two = number_2

upack_three = number_3 , number_4
index_1,index_2 = upack_three

print("the unpacked tuple = ",upack_one,upack_two,index_1,index_2 )



# SORTING WORD THAT ARE MORE THAN FIVE 
print ()
animal_list = ['Cat','Elephant','Tiger','Lion']
def length_of_list (words):
    if len(words) > 5:
        return words
    
new_animal_list = list(filter(length_of_list,animal_list))
print(f"the word longer than 5 characters  = {new_animal_list}")


