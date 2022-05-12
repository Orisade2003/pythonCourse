import functools

def is_ha(string):
    """
    The function checks is a character is either 'a' or 'h'
    :param string:character given by user
    :type string: string
    :return: True if character is 'a' or 'h' and False otherwise
    :rtype: bool
    """
    return string == 'a' or string == 'h'


def is_funny(string):
    """
    The function checks if a string is made only of the characters 'a' and 'h'
    :param string: string given by the user
    :type string: string
    :return: True if string is made only of the characters 'a' and 'h' and False otherwise
    :rtype: bool
    """
    return len(list(filter(is_ha, string))) == len(string)


def main():
    print(is_funny("hello"))


if __name__ == '__main__':
    main()
