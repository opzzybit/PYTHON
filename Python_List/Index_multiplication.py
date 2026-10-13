import random


#THE LIST
length_list = []

for number in range(1,10):
     opzzy = random.randint(1,50)
     length_list.append(opzzy) 

print(length_list )
 
multiplied_list = length_list[2] * length_list[5] * length_list[8]

print(f"The multiple of the third list = {multiplied_list}")
