from histogram import histogram
from sample import random_word

def generate_sentence():
    my_file = open("./tintern_abbey.txt", "r")
    lines =  my_file.readlines()
    my_histogram = histogram(lines)
    
    sentence = ""
    num_words = 10
    for i in range(num_words):
        word = random_word(my_histogram)
        sentence += " " + word
    return sentence