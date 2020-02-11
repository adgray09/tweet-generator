from read_file import read_file

class Dictogram:
    def __init__(self):
        self.histogram = {}
        
    def create_dictogram(self, text):
        for sentences in text:
            sentence = sentences.split()
            for word in sentence:
                self.histogram[word] = self.histogram.get(word, 0) + 1
        return self.histogram

dicto = Dictogram()
print(dicto.create_dictogram(read_file("tintern_abbey.txt")))