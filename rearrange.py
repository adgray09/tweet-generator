import random
import sys as sys

if __name__ == "__main__":
    args = sys.argv[1:]
    
    for rand_arg in args:
        randomize = random.randint(0, len(args)-1)
        random_word = args[randomize]
        print(random_word)

