given_prices = [100, 200, 300]
def adding_percentage_number_list(numbers):
    percentage = numbers * 0.10
    total = numbers + percentage 
    return total
result = list(map(adding_percentage_number_list,Given_prices))
print("10% added to the numbers  = ",result)
