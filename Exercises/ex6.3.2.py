def longest(my_list):
    """
    :param my_list:the list in which we want to find the longest string, all items must be of type string
    :return: the longest string in the list
    :rtype: string
    """
    sorted_by_len = sorted(my_list, key=len)
    return sorted_by_len[-1]

if __name__ == '__main__':
    list1 = ["111", "234", "2000", "goru", "birthday", "09"]
    print(longest(list1))