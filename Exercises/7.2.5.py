def sequence_del(my_str):
    """
    :param my_str:a string given by the user
    :return: a new string which keeps only one character from sequences of the same character in my_str
    :rtype: string
    """
    no_seq = ""
    no_seq += my_str[0]
    for char in range(1, len(my_str)):
        if my_str[char] != my_str[char - 1]:
            no_seq += my_str[char]
    return no_seq


def main():
    print(sequence_del("ppyyyyythhhhhooonnnnn"))


if __name__ == '__main__':
    main()
