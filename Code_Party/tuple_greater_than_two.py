mixed_list = [(1,'A'),(4,'B'),(2,'C')]
def sorting_out_index_greater_than_two(numbers):
	return  numbers[0] > 2
			
print(f"the index is   = {tuple(filter(sorting_out_index_greater_than_two,mixed_list))}")

