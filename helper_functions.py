def get_index(word, histogram):
    """Helper function
    """
    current_index = 0
    for item in histogram:
        if item[0] == word:
            return current_index
        current_index += 1 
    return -1