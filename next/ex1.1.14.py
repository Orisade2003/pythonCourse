import functools
def char_to_num(char, char2):
    """
    :param char: character given by the user, must be a digit
    :type char: string
    :param char2: character given by the user, must be a digit
    :type char2: string
    :return: the sum of both characters when after they are converted to int
    :rtype: int
    """
    return int(char) + int(char2)


def sum_of_digits(number):
    """
    :param number: number given by the user
    :type number: int
    :return: the sum of the digits of the number
    """
    return functools.reduce(char_to_num, str(number))


def main():
    print(sum_of_digits(134))


if __name__ == '__main__':
    main()
