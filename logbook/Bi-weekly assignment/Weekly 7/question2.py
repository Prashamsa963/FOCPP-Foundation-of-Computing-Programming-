def letters_in_either(word1, word2):
    return sorted(set(word1) | set(word2))

def letters_in_both(word1, word2):
    return sorted(set(word1) & set(word2))

def letters_in_one_only(word1, word2):
    return sorted(set(word1) ^ set(word2))