"""
Word Count

"""
import re
def word_count(input_str):
    """
    Returns a dictionary of words in a given string
    """
    words_dict = {}
    for word in  re.split('[\W_]+', input_str):
        if word:
            word = word.lower()
            if word in words_dict:
                words_dict[word]+=1
            else:
                words_dict[word] = 1
    return words_dict

