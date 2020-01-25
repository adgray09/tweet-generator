import sys

words_list = ("one fish two fish red fish blue fish")
words_list.split()

def dictionary(words_string):
    hist = {}
    words_list = words_string.split()
    for i in words_list:
        hist[i] = hist.get(i, 0) + 1
    return hist
        
counted = dictionary(words_list)

