def translate(sentence):
    """
    The function transaltes a sentence in spanish to english - the sentence must include the words in the dictionary
    :param sentence: sentence in Spanish given by the user
    :type sentence:str
    :return: the sentence translated to english
    :rtype: str
    """
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    word_list = sentence.split(" ")
    translated = (words.get(i) for i in word_list if i in words.keys())
    translation = ''
    for i in translated:
        translation = translation + " " + i
    return translation


def main():
    print(translate('el gato esta en la casa la casa'))


if __name__ == "__main__":
    main()
