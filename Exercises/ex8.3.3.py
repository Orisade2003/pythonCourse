def count_chars(my_str):
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
