number_1 = int(input("Enter first number:   "))
number_2 = int(input("Enter second number:  "))
number_3 = int(input("Enter third number:  "))

largest = number_1
smallest = number_1

sum_of_number = number_1 + number_2 + number_3
average = sum_of_number / 3
product = number_1 * number_2 * number_3

if number_2 > largest:
    largest = number_2

if number_3 > largest:
    largest = number_3

if number_2 < smallest:
    smallest = number_2

if number_3 < smallest:
    smallest = number_3

print("The Sum of the numbers is", sum_of_number)
print("The average is", average)
print("The Product is", product)
print("largest number is", largest)
print("Smallest number is", smallest)
