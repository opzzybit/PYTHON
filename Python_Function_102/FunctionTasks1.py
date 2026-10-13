#LENGTH OF WORD
def length_of_a_String(word):
  
  new_word = word

  return len(new_word)

output = length_of_a_String("Semicolon")

print("The length of the string =",output)


#letter selection
def word_selection(word):
   
  
  if len(word) < 2:
        return ""
  
  return word[:2] +  word[-2:]
 
output = word_selection("semicolon")

print(f"the selected letter = {output}")



#ADDING LETTERS TO A WORD 
def  adding_letter(word):
    
    if len(word) < 3:
       return word
    
    if word[-3:] == "ing":
        return word + "ly"
    
    else:
        return word + "ing"
    
output = adding_letter("gon")

print(f"the added letter = {output}")


#LONGEST LETTER
def set_of_list(words):
    longest = words[0] 
    for letter in (words):
        if len(letter) > len(longest):
            longest = letter
            return longest , len(longest)
    
output = set_of_list(["toyin","opeyemi", "welcome", "banker"])
 
print (output)



#ODD INDEX 

def odd_index_value(word):
    
    string = " "
    for number in range (len(word)):
        if number % 2 == 1:
            string += word[number] 
    return string
          
output = odd_index_value("semicolon")
print (output)



#MINIMUM NUMBER
def minimum_number(number):
    minimum = number[0]
    if  number[1] < minimum: 
         minimum = number[1]

    if  number[2] < minimum: 
        minimum = number[2]

    if  number[3] < minimum: 
        minimum = number[3]

    if  number[4] < minimum: 
         minimum = number[4]
    return minimum    
output = minimum_number([11,8,9,10,3])
 
print ("the minimum number is " ,output)



#MAXIMUM NUMBER
def maximum_number(number):
    maximum = number[0]
    if  number[1] > maximum: 
         maximum = number[1]

    if  number[2] > maximum: 
        maximum = number[2]

    if  number[3] > maximum: 
        maximum = number[3]

    if  number[4] > maximum: 
         maximum = number[4]
    return maximum    
output = maximum_number([11,8,9,10,3])
 
print ("the maximum number is " ,output)



#MULTIPLE OF WORDS 
def multipling_words(input_word,input_number):
    
    string = ""
    for number in range (input_number):
         string += input_word
    
    return  string  
 
    if input_number == float(input_number): 
        return input_word
    

output = multipling_words("SEMI" ,4)
print(output)        
        



#squared lists
def squared_lists(list_number):

    for number in (list_number):
        print([ number * number] , end= " ")
        print()
output = squared_lists([3,7,10,2,4,8,])
      
        
        
# SUM OF THE SQUARED
def sum_squared_lists(list_number):
       
    sum_squared = 0
    for number in (list_number):
        squared = number * number
        sum_squared += squared
    return  sum_squared

output = sum_squared_lists([3,7,10,2,4,8,])
print ( "sum_squared = ",output)      
        
        
        
