animal_list = ['Cat','Elephant','Tiger','Lion']
def length_of_list (words):
    if len(words) > 5:
        return words
    
new_animal_list = list(filter(length_of_list,animal_list))
print(f"the word longer than 5 characters  = {new_animal_list}")
