def read_file(source_text):
    with open(source_text, 'r') as f:
        source_text = f.readlines()
        return source_text