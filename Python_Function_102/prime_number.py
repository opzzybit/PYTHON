def checking_for_prime_number(prime):
    
    for index in range (prime):
        if index < 1:
           continue
           
    
    for index2 in range (2,index):
            if index2 % index == 0:
              print ("true"
            if index2 % index != 0:   
              return False
        
        
output = checking_for_prime_number(3)
print (output)
