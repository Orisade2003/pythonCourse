def intersection(list_1, list_2):
    """
    :param list_1: first list given by the user
    :type list_1:list
    :param list_2: second list given by the user
    :type list_2:list
    :return: a list which is the intersection of both other lists without duplicates
    :rtype: list
    """
    intersected = [i for i in list_1 if i in list_2]
    return list(set(intersected))


def main():
    print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))


if __name__ == '__main__':
    main()
