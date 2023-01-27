def sort_words(sequence):
    # split the sequence into a list of words
    words = sequence.split("-")
    # sort the words alphabetically
    words.sort()
    # join the sorted words with hyphens
    sorted_sequence = "-".join(words)
    # print the sorted sequence
    print(sorted_sequence)

sort_words("green-red-yellow-black-white") # black-green-red-white-yellow
