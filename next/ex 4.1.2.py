def translate(sentence):
    """
    :param sentence: sentence in Spanish given by the user
    :type sentence:str
    :return: the sentence translated to english
    :rtype: str
    """
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    word_list = sentence.split(" ")
    translated = (words.get(i) for i in word_list)
    str = ''
    for i in range(len(word_list)):
        current = next(translated)
        str = str + " " + current
    return str


def main():
    print(translate('el gato esta en la casa la casa'))


if __name__ == "__main__":
    main()
