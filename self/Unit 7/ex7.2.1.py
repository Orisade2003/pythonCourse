def is_greater(my_list, n):
    """

    :param my_list: a list given by the user
    :type my_list: list
    :param n: a number given by the user
    :type n: int
    :return: the function return a new list which contains all the numbers which are in the original list
            and are larger than n
    :rtype: list
    """
    new_list = []
    for i in my_list:
        if i > n:
            new_list.append(i)
    return new_list


def main():
    my_list = [42,13,43,54,12,4]
    new_l = is_greater(my_list,10)
    print(new_l)

if __name__ == '__main__':
    main()