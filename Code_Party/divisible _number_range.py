divisible_number = list(range(1,52))
def divisible_index (numbers):
    return numbers % 3 == 0 and numbers % 5 == 0
new_divisible_number = list(filter(divisible_index, divisible_number))
print(divisible_number)
print()
print(f"number divisible by 3 and 5  from 1-51 = {new_divisible_number}")    

