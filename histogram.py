import sys
    
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

def unique_words(histogram):
    """
    Returns how many words
    are the length given
    via command log
    """
    return len(histogram)
    
def frequency(word, histogram):
    """ 
    Gives the frequency of 
    requested words in histogram
    via command log
    """
    return histogram[word]

if __name__ == '__main__':
    
    with open('tintern_abbey.txt', 'r') as f:
        # my_list = [line.rstrip('\n') for line in f for word in line.split()]
        # list comprehension
        my_list = f.readlines()

    args = sys.argv[1:]
    #print(frequency('in', histogram(args)))
    print(histogram(my_list))
    #print(unique_words(histogram(args)))