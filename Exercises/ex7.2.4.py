def num_contains_seven(number):
    """
    :param number: a number
    :return: True if the number contains the digit 7 in it and False otherwise
    :rtype Boolean
    """
    while number != 0:
        if number % 10 == 7:
            return True
        number //= 10
    return False


def seven_boom(end_number):
    """
    :param end_number: the top border number for the seven boom game
    the function prints all numbers from 1 to end number, if the number is divisible by 7, or has
    the digit 7 in it, instead of printing the number the function prints the string "Boom"
    """
    for i in range(0, end_number + 1):
        if i % 7 == 0 or num_contains_seven(i):
            print("BOOM")
        else:
            print(i)


def main():
    seven_boom(17)


if __name__ == '__main__':
    main()
