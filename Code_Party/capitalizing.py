given_name_list = ['john', 'mary','steve']
def capitalized_first_letter(words):
    new_given_name_list = []
    new_given_name_list += words[0] 
    new_given_name_list += words[1]
    new_given_name_list += words[2]
    
     
    return new_given_name_list
result = list(map(capitalized_first_letter,given_name_list))
print(result)    
