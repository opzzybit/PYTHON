smallest = None
for given_number in (10, 20, 30, 40 ,50):
  
   if smallest is None or given_number < smallest :
     smallest = given_number
   print(f"{smallest}")     
print()    
print(f"{smallest}")
 
