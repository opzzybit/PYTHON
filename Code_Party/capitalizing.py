given_name_list = ['john', 'mary','steve']
def capitalized_first_letter(words):
    new_given_name_list = []
    new_given_name_list[0] += words[0]
    new_given_name_list[1] += words[1]
    new_given_name_list[2] += words[2]
    result = new_given_name_list[0], new_given_name_list[1],new_given_name_list[2]
     
    return new_given_name_list
result = list(map(capitalized_first_letter,given_name_list))
print(result)    
