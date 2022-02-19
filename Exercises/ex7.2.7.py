def arrow(my_char, max_length):
    """
    :param my_char: the character the user wants the arrow to be made of, type str
    :param max_length: How long the user want the longest line in the arrow to be, type int
    the function prints an arrow shape, made of my_char with a length of max_length
    """
    for i in range(1, max_length + 1):
        print(my_char * i)
    for i in range(max_length - 1, 0, -1):
        print(my_char * i)


def main():
    arrow('*',5)

if __name__ == '__main__':
    main()