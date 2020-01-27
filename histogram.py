import sys
import re

with open('tintern_abbey.txt', 'r') as f:
    words = f.read()
    my_list = re.sub(r'[^a-zA-Z\s+-]',' ', words).lower()
    my_list = my_list.split()
    
def dictionary(words_string):
    hist = {}
    for i in my_list:
        hist[i] = hist.get(i, 0) + 1
    return hist
        
counted = dictionary(my_list)
print(counted)
