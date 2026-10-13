import random


#THE LIST
length_list = []

for number in range(1,10):
     opzzy = random.randint(1,50)
     length_list.append(opzzy) 

print(length_list )

largest = length_list[0]


if  length_list[1] > largest: 
        largest = length_list[1]

if  length_list[2] > largest: 
        largest = length_list[2]

if  length_list[3] > largest: 
        largest = length_list[3] 

if  length_list[4] > largest: 
        largest = length_list[4]

if  length_list[5] > largest: 
        largest = length_list[6]

if  length_list[6] > largest: 
        largest = length_list[6]

if  length_list[7] > largest: 
        largest = length_list[7]    

if  length_list[8] > largest: 
        largest = length_list[8]

print(f"The largest number = {largest}")

