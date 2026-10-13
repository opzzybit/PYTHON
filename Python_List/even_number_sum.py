import random

length_list = []

for number in range(1,10):
     opzzy = random.randint(1,50)
     length_list.append(opzzy) 

print(length_list )
 

count_even = 0

if  length_list[0] % 2 == 0: 
        count_even += length_list[0]

if  length_list[1] % 2 == 0: 
        count_even += length_list[1]     

if  length_list[2] % 2 == 0: 
        count_even += length_list[2]     

if  length_list[3] % 2 == 0: 
        count_even += length_list[3]     

if  length_list[4] % 2 == 0: 
        count_even += length_list[4]

if  length_list[5] % 2 == 0: 
        count_even += length_list[5]     

if  length_list[6] % 2 == 0: 
        count_even += length_list[6]     

if  length_list[7] % 2 == 0: 
        count_even += length_list[7]     
if  length_list[8] % 2 == 0: 
        count_even += length_list[8]     
print(f"The sum of the even number = {count_even}")

