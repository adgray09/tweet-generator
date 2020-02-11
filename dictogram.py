class Dictogram:
    def __init__(self):
        self.histogram = {}
        
    def create_dictogram(self, text):
        for sentences in text:
            sentence = sentences.split()
            for word in sentence:
                self.histogram[word] = self.histogram.get(word, 0) + 1
        return self.histogram
        
with open('tintern_abbey.txt', 'r') as f:
        my_list = f.readlines()
        
bleee = Dictogram()
print(bleee.create_dictogram(my_list))