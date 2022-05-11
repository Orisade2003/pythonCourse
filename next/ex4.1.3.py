def is_prime(n):
    """
    The function checks if a given number is a prime number
    :param n: number given by the user
    :type n: int
    :return:The function returns True if the number is prime and False otherwise
    :rtype:bool
    """
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def first_prime_over(n):
    """
    The function returns the next prime number after a given number
    :param n: number givrn by the user
    :type n: int
    :return: the next prime number above n
    :rtype: int
    """
    first_prime_above_n = (i for i in range(n + 1, 2 * n + 1) if is_prime(i))
    return next(first_prime_above_n)


def main():
    print(first_prime_over(13))


if __name__ == "__main__":
    main()
