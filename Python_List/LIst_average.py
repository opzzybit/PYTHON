import random


#THE LIST
length_list = []

for number in range(1,10):
     opzzy = random.randint(1,50)
     length_list.append(opzzy) 

print(length_list )

for number in range (length):
    length_sum = length_list[0] + length_list[1] + length_list[2] + length_list[3] + length_list[4]
    length_sum_two = length_list[5] + length_list[6] + length_list[7] +  length_list[8]
    
    general_number = length_sum + length_sum_two
    average = general_number / length 
    
print(f"average{ average}  ")

