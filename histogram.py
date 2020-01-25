import sys

with open('tintern_abbey.txt') as f:
    my_list = [line.rstrip('\n') for line in f for word in line.split()]
    
def dictionary(words_string):
    hist = {}
    for i in my_list:
        hist[i] = hist.get(i, 0) + 1
    return hist
        
counted = dictionary(my_list)
print(counted)
