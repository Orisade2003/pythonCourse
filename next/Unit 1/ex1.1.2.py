def mult_letter(char):
    """
    The function multiplies a character
    :param char:character given by the user
    :type char: string
    :return: char concatenated twice
    :rtype: string
    """
    return char * 2


def double_letter(my_str):
    """
    The function gets a string and doubles each character
    :param my_str: a string given by the user
    :rtype : string
    :return: the function returns the given string but each character is doubled, for example the string 'ab'
            would return 'abab'
    """
    return ''.join(list(map(mult_letter, my_str)))


def main():
    print(str(double_letter("we are the champions!")))


if __name__ == '__main__':
    main()
