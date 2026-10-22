products_list = [
("Laptop", 1200),
("Mouse", 25),
("Keyboard", 45),
("Monitor", 300),
("USB Cable", 10)]

def sort_product_greater_than_hundred(products):
    return products[1] > 100
    
result = list(filter(sort_product_greater_than_hundred,products_list))
print(result)

amount_sum = 0 
for product, amount in products_list:
    amount_sum += amount
print(amount_sum)    

for products,prices in products_list:
    print(products , prices)
