def is_valid_input(letter_guessed, old_letters):
    """
    :param letter_guessed: input letter from user
    :param old_letters: letters that have already been guessed
    :type: string
    :return: True if the string is a single letter in the english alphabet and isn't in the old_letters list and False otherwise
    """
    if len(letter_guessed)>1 or not letter_guessed.isalpha() or letter_guessed in old_letters:
        return False
    return True
