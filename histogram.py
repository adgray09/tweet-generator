import sys
    
def dictogram(text):
    """
    Creates histogram from text file
    """
    histogram = {}
    for sentences in text:
        sentence = sentences.split()
        for word in sentence:
            histogram[word] = histogram.get(word, 0) + 1
    return histogram

def get_index(word, listogram):
    """Helper function
    """
    current_index = 0
    for item in listogram:
        if item[0] == word:
            return current_index
        current_index += 1 
    return -1
            
def listogram(text):
    listogram = []
    for sentences in text:
        sentence = sentences.split()
        for word in sentence:
            index = get_index(word, listogram)
            if index == -1:
                listogram.append([word, 1])
            else:
                listogram[index][1] += 1
    return listogram

def tuplegram(text):
    tuplegram = []
    pass

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
        # my_list = f.readlines()
        my_list = f.readlines()
        
    with open('small_file.txt', 'r') as f:
        # my_list = [line.rstrip('\n') for line in f for word in line.split()]
        # list comprehension
        small_file = f.readlines()

    args = sys.argv[1:]
    #print(frequency('in', histogram(args)))
    #print(histogram(my_list))
    #print(unique_words(histogram(args)))
    #print(my_list)
    print(listogram(my_list))