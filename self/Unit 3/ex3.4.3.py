def capitalizeHalf():
    input_str = input('Enter a string')
    first_half = input_str[:len(input_str) // 2]
    second_half = input_str[len(input_str) // 2:]
    second_half = second_half.upper()
    print(first_half + second_half)


if __name__ == "__main__":
    capitalizeHalf()
