HANGMAN_ASCII_ART = """ 
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

STATE1 = "x-------x"
STATE2 = """  
    x-------x
    |
    |
    |
    |
    |
    """
STATE3 = """ 
    x-------x
    |       |
    |       0
    |
    |
    |"""
STATE4 = """
   x-------x
    |       |
    |       0
    |       |
    |
    |
"""
STATE5 = """

    x-------x
    |       |
    |       0
    |      /|\
    |
    |
"""

STATE6 = """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |

"""

STATE7 = """ 
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    """
HANGMAN_PHOTS = [STATE1, STATE2, STATE3, STATE4, STATE5, STATE6, STATE7]


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
    |
    """)


def printHangman():
    print(HANGMAN_ASCII_ART)
    print(MAX_TRIES)


def guessLetter():
    first_letter = input("Guess A Letter:\n")
    first_letter = first_letter.lower()
    print(first_letter)


def printLines():
    word = input('Enter a Word')
    print("_ " * len(word))


def checkValidity():
    letter = input("Enter A Letter: ")
    if (len(letter) > 1 and not letter.isalpha()):
        print("E3")
    elif not letter.isalpha():
        print("E2")
    elif len(letter) > 1:
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
    if (len(letter_guessed) > 1 or not letter_guessed.isalpha() or letter_guessed in old_letters):
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
    if (is_valid_input(letter_guessed, old_letters_guessed)):
        old_letters_guessed.append(letter_guessed)
        return True
    print("X")
    print("->".join(old_letters_guessed))
    return False


def show_hidden_word(secret_word, old_letters_guessed):
    """
    :param secret_word: the word the user is trying to guess
    :param old_letters_guessed: the letters that have already been guessed
    :return: a string, which is made of underscores and letters, and in the places where in the secret word
            there are letters that are in old_letters_guessed, the string has the letter in its right place
            letters which haven't been guessed yet are shown as '_'
    :rtype: Boolean
    """
    word_with_guesses = ""
    for char in secret_word:
        if char in old_letters_guessed:
            word_with_guesses += char + " "
        else:
            word_with_guesses += "_ "
    return word_with_guesses


def check_win(secret_word, old_letters_guessed):
    """
    :param secret_word: the secret word the user is trying to guess
    :param old_letters_guessed: a list of all the letters that have already been guessed
    :return: True if all the letters in secret_word are in old_letters_guessed and False otherwise
    :rtype: Boolean
    """
    for letter in secret_word:
        if (letter not in old_letters_guessed):
            return False
    return True


def print_hangman(num_of_tries):
    """
    :param num_of_tries: amount of wrong guesses the user has made
    the function prints the correct hangman photo according to how many wrong guesses the user made
    """
    tries_dict = {1: STATE1, 2: STATE2, 3: STATE3, 4: STATE4, 5: STATE5, 6: STATE6, 7: STATE7}
    print(tries_dict[num_of_tries])


def choose_word(file_path, index):
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


def main():
    file_input = input("Enter File Path to words file")
    word_index = int(input("Enter a word index"))
    secret_word = choose_word(file_input,word_index)
    print(file_input)
    old_letters_guessed = []
    turn_counter = 0
    win = False
    while turn_counter <= MAX_TRIES and not win:
        print(show_hidden_word(secret_word,old_letters_guessed))
        guess = input("Guess A letter")

        while not is_valid_input(guess, old_letters_guessed):
            if try_update_letters_guessed(guess,old_letters_guessed):
                break
            print("Please Enter a valid input")
            guess = input("Guess A letter")

        try_update_letters_guessed(guess, old_letters_guessed)
        win = check_win(secret_word,old_letters_guessed)
        if guess not in secret_word:
            turn_counter+=1
            print_hangman(turn_counter)

    if(win):
        print("You Won!")
    else:
        print("You Lost :(")





if __name__ == '__main__':
    main()
