print("Price Calculator")
age = int(input("Enter your age :   "))

if age < 5:
    print("Free")
if age >= 5  and age <= 12:
    print("this is the price:  $5")
if age >= 13 and age <= 64:
    print("this is the price:  $12")
if age >= 65:
    print("this is the price:  $8")
