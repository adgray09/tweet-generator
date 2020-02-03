import sys
    
def histogram(text):
    """
    Creates histogram from text file
    """
    histogram = {}
    for sentences in text:
        sentence = sentences.split()
        for word in sentence:
            histogram[word] = histogram.get(word, 0) + 1
    return histogram

def list_histogram(text):
    histogram = []
    for sentences in text:
        sentence = sentences.split()
        for word in sentence:
            # temp inner list
            tmp_list = [word, 1]
            found_word = False
            found_word_index = None
            for index, value in enumerate(histogram):
                if value[0] == tmp_list[0]:
                    # if word == to word word is found
                    found_word = True
                    found_word_index = index
            if found_word:
                # word counter
                histogram[found_word_index][1] += 1
            else:
                # once all word found append temp inner list to histogram
                histogram.append(tmp_list)
            found_word = False
            found_word_index = None
    return histogram
                
def tuple_histogram(text):
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
    print(list_histogram(my_list))