def numbers_letters_count(my_str):
    """
    :param my_str: a string given by the user
    :type my_str: string
    :return: a list, in which the first number represents the amount of digits in my_str and the second number
             represents the number of any other characters
    :rtype: list
    """
    letters_counter = 0
    digit_counter = 0
    for char in my_str:
        if char.isnumeric():
            digit_counter += 1
        else:
            letters_counter += 1
    return [digit_counter,letters_counter]


def main():
    print(numbers_letters_count("Python 3.6.3"))

if __name__ == '__main__':
    main()

