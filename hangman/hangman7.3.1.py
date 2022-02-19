
def show_hidden_word(secret_word, old_letters_guessed):
    """
    :param secret_word: the word the user is trying to guess
    :param old_letters_guessed: the letters that have already been guessed
    :return: a string, which is made od underscores and letters, and in the places where in the secret word
            there are letters that are in old_letters_guessed, the string has the letter in its right place
            letters which haven't been guessed yet are shown as '_'
    :rtype: Boolean
    """
    word_with_guesses=""
    for char in secret_word:
        if char in old_letters_guessed:
            word_with_guesses+=char + " "
        else:
            word_with_guesses+="_ "
    return word_with_guesses

