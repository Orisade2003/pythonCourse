HANGMAN_ASCII_ART =  """ 
      Welcome To The Game Hangman
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/"""
MAX_TRIES = 6


def printStates():
    print(r"""picture 1:
    x-------x

picture 2:
    x-------x
    |
    |
    |
    |
    |

picture 3:
    x-------x
    |       |
    |       0
    |
    |
    |

picture 4:
    x-------x
    |       |
    |       0
    |       |
    |
    |

picture 5:
    x-------x
    |       |
    |       0
    |      /|\
    |
    |

picture 6:
    x-------x
    |       |
    |       0
    |      /|\
    |      /
    |

picture 7:
    x-------x
    |       |
    |       0
    |      /|\
    |      / \
    |""")

def printHangman():
    print(HANGMAN_ASCII_ART)
    print(MAX_TRIES)

def guessLetter():
    first_letter = input("Guess A Letter:\n")
    first_letter=first_letter.lower()
    print(first_letter)

def printLines():
    word = input('Enter a Word')
    print("_ "* len(word))

def checkValidity():
    letter = input("Enter A Letter: ")
    if(len(letter) > 1 and not letter.isalpha()):
        print("E3")
    elif not letter.isalpha():
        print("E2")
    elif len(letter)>1:
        print("E1")
    else:
        print(letter.lower())


def is_valid_input(letter_guessed, old_letters):
    """
    :param letter_guessed: input letter from user
    :param old_letters: letters that have already been guessed
    :type: string
    :return: True if the string is a single letter in the english alphabet and isn't in the old_letters list and False otherwise
    """
    if(len(letter_guessed)>1 or not letter_guessed.isalpha() or letter_guessed in old_letters):
        return False
    return True


def try_update_letters_guessed(letter_guessed, old_letters_guessed):
    """
    :param letter_guessed: letter guessed by user
    :param old_letters_guessed: a list containing all the letters that have been gussed
    :return: True if letter_guessed isn't in old_letters_guessed and is a single letter in the english alphabet,
            and False otherwise.
             if the function returns False it prints X, and all the letters that have already been guessed
             if the function returns True, letter_guessed is added to old_letters_guessed.
    """
    if(is_valid_input(letter_guessed,old_letters_guessed)):
        old_letters_guessed.append(letter_guessed)
        return True
    print("X")
    print("->".join(old_letters_guessed))
    return False

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




if __name__ == '__main__':
    old_letters_guessed = ['a', 'p', 'j', 'i', 'm', 'k','a','l']
    secret_word = "mammals"
    print(check_win(secret_word, old_letters_guessed))
