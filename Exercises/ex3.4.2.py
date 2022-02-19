def replaceLetter():
    input_str = input("enter a string")
    first_char = input_str[0]
    input_str = input_str[0] + input_str[1:].replace(first_char,'e')
    print(input_str)
if __name__ == '__main__':
    replaceLetter()