import sys
import random
from histogram import histogram
from text import read_text

def random_word(text): 
    random_index = random.randint(0, sum(text.values()))
    total = 0
    for word,count in text.items():
        total += count
        if total >= random_index:
            # if total >= random_index return the word at that spot
            return word

if __name__ == "__main__":
    lines = read_text()
    text = histogram(lines)
    args = sys.argv[:1]
    print(random_word(text))

