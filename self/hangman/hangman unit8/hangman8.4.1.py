
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


def print_hangman(num_of_tries):
    """
    :param num_of_tries: amount of wrong guesses the user has made
    the function prints the correct hangman photo according to how many wrong guesses the user made
    """
    tries_dict = {1: STATE1, 2: STATE2, 3: STATE3, 4: STATE4, 5: STATE5, 6: STATE6, 7: STATE7}
    print(tries_dict[num_of_tries])
