def format_list(my_list):
    """
    :param my_list: list given by the user
    :type my_list: list
    :return: the function returns all the items at an even index seperated by commas, and
    the last word in the list with the an 'and' before it
    """
    even_list = my_list[:len(my_list) - 1:2]
    even_list = ",".join(even_list)
    return even_list + " and " + my_list[-1]

if __name__ == '__main__':
    my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
    print(format_list(my_list))