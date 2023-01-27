import string

def is_pangram(sentence):
    # remove spaces and punctuation
    sentence = sentence.replace(" ", "").translate(str.maketrans('', '', string.punctuation))
    # convert to lowercase
    sentence = sentence.lower()
    # create a set of the unique characters in the sentence
    unique_chars = set(sentence)
    # check if the set contains all 26 letters of the alphabet
    return len(unique_chars) == 26

print(is_pangram("The quick brown fox jumps over the lazy dog")) # True
print(is_pangram("This is not a pangram")) # False
