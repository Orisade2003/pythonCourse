def extend_list_x(list_x, list_y):
    """
    :param list_x: the list you want to extend
    :type list_x: list
    :param list_y: the list you want to add to list_x
    :type list_y: list
    :return: a new list which adds list_y at the start of list_X
    :rtype: list
    """
    list_x[:0] = list_y
    return list_x


if __name__ == '__main__':
    l = [5, 6, 7, 8]
    l2 = [1, 2, 3, 4]
    extend_list_x(l, l2)
    print(l)
