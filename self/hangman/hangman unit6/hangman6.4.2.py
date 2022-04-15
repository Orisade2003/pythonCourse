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


def try_update_letters_guessed(letter_guessed, old_letters_guessed):
    """
    :param letter_guessed: letter guessed by user
    :type letter_guessed: string
    :param old_letters_guessed: a list containing all the letters that have been guessed
    :type old_letters_guessed: list
    :return: True if letter_guessed isn't in old_letters_guessed and is a single letter in the english alphabet,
            and False otherwise.
             if the function returns False it prints X, and all the letters that have already been guessed
             if the function returns True, letter_guessed is added to old_letters_guessed.
    :rtype bool
    """
    if is_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    print("X")
    print("->".join(old_letters_guessed))
    return False

def main():
    print(try_update_letters_guessed('a', ['a','t','y']))

if __name__ == "__main__":
    main()