import sys

with open('tintern_abbey.txt', 'r') as f:
    # my_list = [line.rstrip('\n') for line in f for word in line.split()]
    # list comprehension
    my_list = f.readlines()
    
    
def histogram(text):
    """
    Creates histogram from text file
    """
    hist = {}
    for i in my_list:
        words = i.split()
        for word in words:
            hist[word] = hist.get(word, 0) + 1
    return hist

def unique_words():
    pass

def frequency(word, histogram):
    """ 
    Gives the frequency of 
    words in histogram
    """
    return histogram[word]

if __name__ == '__main__':
    args = sys.argv[1]
    #print(frequency('These', histogram(args)))
    #counted = histogram(my_list)
    #print(counted)