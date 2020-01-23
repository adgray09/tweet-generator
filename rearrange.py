import random
import sys as sys

args = sys.argv[1:]
    
def rearrange():
    
    for rand_arg in args:
        randomize = random.randint(0, len(args)-1)
        random_word = args[randomize]
        print(random_word)
    return rand_arg
        
rearrange()

