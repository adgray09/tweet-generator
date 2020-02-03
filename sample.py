import sys
import random
from histogram import histogram

def random_word(histogram): 
    for word in histogram:
        word = random.randint(0, len(histogram))
    return word

if __name__ == "__main__":
    args = sys.argv[:1]

