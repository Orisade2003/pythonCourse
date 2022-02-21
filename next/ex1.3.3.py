import functools


def is_ha(string):
    """
    :param string:character given by user
    :type string: striing
    :return: True if character is 'a' or 'a' and False otherwise
    :rtype: bool
    """
    return string == 'a' or string == 'h'


def is_funny(string):
    """
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
