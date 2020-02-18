from read_file import read_file
import random


class Dictogram():
    def __init__(self, word_list):
        self.histogram = {}
        self.text = read_file("tintern_abbey.txt")
        self.word_list = word_list
        
        self.dictionary_histogram = self.build_dictogram()

        self.tokens = sum(self.dictionary_histogram.values())
        self.types = self.unique_words()
        
    def build_dictogram(self, text):
        for sentences in text:
            sentence = sentences.split()
            for word in sentence:
                self.histogram[word] = self.histogram.get(word, 0) + 1
        return self.histogram

    def frequency(self, word):
        if word in self.histogram:
            return self.histogram[word]
        else:
            return 0
    
    def unique_words(self):
        '''returns the number of unique words in the dictionary histogram'''
        #TODO: use your unique words function as a starting point to complete this method
        pass

    def sample(self):
        text = self.histogram
        random_index = random.randint(0, sum(text.values()))
        total = 0
        for word,count in text.items():
            total += count
            if total >= random_index:
            # if total >= random_index return the word at that spot
                return word
    
dicto = Dictogram()
dicto.create_dictogram(read_file("tintern_abbey.txt"))
#print(dicto.sample())
#print(dicto.frequency("my"))

def print_dictogram(word_list):
    '''Creates a dictionary based histogram (dictogram) and then prints out its properties and samples from it'''

    print()
    print('Dictionary Histogram:')
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    dictogram = Dictogram(word_list)
    print('dictogram: {}'.format(dictogram.dictionary_histogram))
    print('{} tokens, {} types'.format(dictogram.tokens, dictogram.types))
    for word in word_list[-2:]:
        freq = dictogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()
    print_dictogram_samples(dictogram)

def print_dictogram_samples(dictogram):
    '''Compares sampled frequency to observed frequency'''

    print('Dictionary Histogram samples:')
    # Sample the histogram 10,000 times and count frequency of results
    samples_list = [dictogram.sample() for _ in range(10000)]
    samples_hist = Dictogram(samples_list)
    print('samples: {}'.format(samples_hist.dictionary_histogram))
    print()
    print('Sampled frequency and error from observed frequency:')
    header = '| word type | observed freq | sampled freq  |  error  |'
    divider = '-' * len(header)
    print(divider)
    print(header)
    print(divider)
    # Colors for error
    green = '\033[32m'
    yellow = '\033[33m'
    red = '\033[31m'
    reset = '\033[m'
    # Check each word in original histogram
    for word, count in dictogram.dictionary_histogram.items():
        # Calculate word's observed frequency
        observed_freq = count / dictogram.tokens
        # Calculate word's sampled frequency
        samples = samples_hist.frequency(word)
        sampled_freq = samples / samples_hist.tokens
        # Calculate error between word's sampled and observed frequency
        error = (sampled_freq - observed_freq) / observed_freq
        color = green if abs(error) < 0.05 else yellow if abs(error) < 0.1 else red
        print('| {!r:<9} '.format(word)
            + '| {:>4} = {:>6.2%} '.format(count, observed_freq)
            + '| {:>4} = {:>6.2%} '.format(samples, sampled_freq)
            + '| {}{:>+7.2%}{} |'.format(color, error, reset))
    print(divider)
    print()

print_dictogram(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'])