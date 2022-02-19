def are_lists_equal(list1, list2):
    """
    :param list1:the first list, all items in list must be of type int or float
    :param list2: the second list, all items in list must be of type int or float
    :return: True if both list contain the same items and false otherwise
    """
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    return False

if __name__ == '__main__':
    l = [1,2,3,4]
    l2 = [4,2,3,3]
    print(are_lists_equal(l,l2))