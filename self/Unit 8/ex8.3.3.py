def count_chars(my_str):
    """
    :param my_str: a string given by the user
    :type my_str: string
    :return: a dictionary where each letter that appears in the string is the key and the amount
             of times it appeared is the index
    :rtype: dict
    """
    chars_dict= {}
    for char in my_str:
        if char != " " and char not in chars_dict.keys():
            chars_dict[char] = my_str.count(char)
    return chars_dict

def main():
    magic_str = "abra cadabra"
    print(count_chars(magic_str))

if __name__ == '__main__':
    main()
