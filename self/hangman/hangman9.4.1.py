def choose_word(file_path, index):
    """
    :param file_path: path to words file
    :type file_path: string
    :param index: word index in file
    :type index: int
    """
    hangman_file = open(file_path,'r')
    hangman_words = hangman_file.read()
    word_list = hangman_words.split('\n')
    all_words = []
    for line in word_list:
        line = line.replace('\n',' ')
        all_words += line.split(' ')
    unique_words = []
    for word in all_words:
        if word not in unique_words:
            unique_words.append(word)
    tup = (len(unique_words),all_words[(index%len(all_words))-1])
    return tup[1]
