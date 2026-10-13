import random


#THE LIST
length_list = []

for number in range(1,10):
     opzzy = random.randint(1,50)
     length_list.append(opzzy) 

print(length_list )

smallest = length_list[0]


if  length_list[1] < smallest : 
        smallest  = length_list[1]

if  length_list[2] < smallest : 
        smallest  = length_list[2]

if  length_list[3] < smallest : 
        smallest  = length_list[3]

if  length_list[4] < smallest : 
        smallest  = length_list[4]

if  length_list[5] < smallest : 
        smallest  = length_list[5]

if  length_list[6] < smallest : 
        smallest  = length_list[6]

if  length_list[7] < smallest : 
        smallest  = length_list[7]

if  length_list[8] < smallest : 
        smallest  = length_list[8]

print(f"The smallest number = {smallest}")


