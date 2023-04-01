test = ['hello', 'hi', 'goodbye', 'yo', 'yes']

def print_upper_words(words,must_start_with):
    """prints all words in the list that start with the second paramter uppercased"""
    
        
    
    for word in words:
        for test in must_start_with:
            char = word[0]
            if(char == test):
                print(word.upper())

