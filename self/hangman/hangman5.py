def is_valid_input(letter_guessed):
    """
    :param letter_guessed: input letter from user
    :type: string
    :return: True if the string is a single letter in the english alphabet and False otherwise
    """
    if(len(letter_guessed)>1 or not letter_guessed.isalpha()):
        return False
    return True