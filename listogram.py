from helper_functions import get_index
from read_file import read_file

class Listogram:
    def __init__(self):
        self.histogram = []
        
    def create_listogram(self, text):
        for sentences in text:
            sentence = sentences.split()
            for word in sentence:
                index = get_index(word, self.histogram)
                if index == -1:
                    self.histogram.append([word, 1])
                else:
                    self.histogram[index][1] += 1
        return self.histogram

steve = Listogram()
print(steve.create_listogram(read_file('tintern_abbey.txt')))
