import functools


def char_to_num(char, char2):
    """
    The function adds the sum of the last digits and the most recent one
    :param char: character given by the user, must be a digit
    :type char: str
    :param char2: character given by the user, must be a digit
    :type char2: str
    :return: the sum of both characters when after they are converted to int
    :rtype: str
    """
    return str(int(char) + int(char2))


def sum_of_digits(number):
    """
    :param number: number given by the user
    :type number: int
    :return: the sum of the digits of the number
    :rtype: int
    """
    return functools.reduce(char_to_num, str(number))


def main():
    print(sum_of_digits(1347))


if __name__ == '__main__':
    main()
