import re

def read_file(source_text):
    with open(source_text, 'r') as f:
        words = f.read()
        # words = " ".join(words)
        words_list = re.sub(r'[^a-zA-Z\s]', '', words).lower()
        word_list = words_list.split()
        
        
        
        
        # words = f.read()
        # words_list = re.sub(r'[^a-zA-Z\s]', '', words).lower()
        # word_list = words_list.split()
        
        
        
        
    return word_list




# read_file = read_file("Dr_suess.txt")

# print(read_file)