print("""            WELCOME 
                  TO 
             MAXNUM""")
first_number = int(input("Enter first number :  "))
second_number = int(input("Enter second number :  "))
third_number = int(input("Enter third number :  "))
 
largest = first_number

if second_number > largest:
    largest = second_number
if third_number > largest:
    largest =  third_number
   
print("the largest number is", largest)
