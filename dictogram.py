from read_file import read_file
import random
from histogram import histogram

class Dictogram:
    def __init__(self):
        self.histogram = {}
        self.text = read_file("tintern_abbey.txt")
        
    def create_dictogram(self, text):
        for sentences in text:
            sentence = sentences.split()
            for word in sentence:
                self.histogram[word] = self.histogram.get(word, 0) + 1
        return self.histogram

    def add_count(self, word, count):
        pass
    
    def frequency(self, word):
        pass
    
    def sample(self):
        text = histogram(self.text)
        random_index = random.randint(0, sum(text.values()))
        total = 0
        for word,count in text.items():
            total += count
            if total >= random_index:
            # if total >= random_index return the word at that spot
                return word
    
    
    
dicto = Dictogram()
dicto.create_dictogram(read_file("tintern_abbey.txt"))
print(dicto.sample())