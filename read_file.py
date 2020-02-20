import re

def read_file(source_text):
    with open(source_text, 'r') as f:
        words = f.readlines()
        words = "".join(words)
        source_text = re.sub(r'[^a-zA-Z\s]', '', words).lower()
        #source_text = source_text.split()
    return source_text