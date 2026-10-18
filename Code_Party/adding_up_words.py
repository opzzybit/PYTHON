message = ['I', 'love', 'Python'] 
from functools import reduce
def adding_the_words_in_the_string(accumulator,words):
    
    return accumulator + words
    
result = reduce(adding_the_words_in_the_string,message)
print(str(result))
