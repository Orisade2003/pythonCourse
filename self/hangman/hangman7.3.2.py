
def check_win(secret_word, old_letters_guessed):
    """
    :param secret_word: the secret word the user is trying to guess
    :param old_letters_guessed: a list of all the letters that have already been guessed
    :return: True if all the letters in secret_word are in old_letters_guessed and False otherwise
    :rtype: Boolean
    """
    for letter in secret_word:
        if(letter not in old_letters_guessed):
            return False
    return True