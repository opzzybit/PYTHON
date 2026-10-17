number_list = list(range (1,22))
def even_number_list (numbers):
        return numbers % 2 == 0    

new_list_number = list(filter(even_number_list, number_list))
print(number_list)
print()
print(f"Even number from 1-21 = {new_list_number}")
