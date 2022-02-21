def is_prime(num):
    """
    :param num: number entered by user
    :type: int
    :return: True if num is prime and False otherwise
    :rtype: boolean
    """
    return [i for i in range(2, num) if num % i == 0] == []


def main():
    print(is_prime(42))
    print(is_prime(43))


if __name__ == '__main__':
    main()
