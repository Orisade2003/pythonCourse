def is_divisible_by_four(num):
    """
    :param num:number given by the user
    :type num:int
    :return: true if the number is divisible by four and false otherwise
    :rtype: Boolean
    """
    return num % 4 == 0

def four_dividers(num):
    """
    :param num:number given by the user
    :return: a list of all numbers in range 1 to number+1 which are divisible by 4
    """
    return list(filter(is_divisible_by_four, range(1, num + 1)))


def main():
    print(four_dividers(30))

if __name__ == '__main__':
    main()

