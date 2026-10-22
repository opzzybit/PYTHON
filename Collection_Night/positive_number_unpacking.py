points_list = [ (2, 3),
(-1, 4),
(5, -6),
(0, 7),
(-3, -2)]
def sorting_positive_number(numbers):
     first_number,second_number = numbers
     return first_number > 0 and second_number > 0
    
result = list(filter(sorting_positive_number,points_list))
print(result)
