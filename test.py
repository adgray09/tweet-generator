from random import randint

filename = "/Users/alex/Desktop/words.txt"

my_file = open(filename, "r")

lines = my_file.readlines()

random_index = randint(0, len(lines)-1)

print(random_index)