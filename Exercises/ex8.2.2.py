def tuple_key(my_tuple):
    """
    :param my_tuple:price tuple, where the first item in the tuple is the name of the item and the
    second item is its price
    :return:the price of the item in the price_tuple
    """
    return my_tuple[1]
def sort_prices(list_of_tuples):
    """
    :param list_of_tuples: list of tuples, in each tuple there are 2 items, the first representing the name
    of the item and the second the price
    :return: a list of the tuples, sorted by price from highest to lowest
    """
    sorted_list_of_tuples = sorted(list_of_tuples,key=tuple_key, reverse=True)
    return sorted_list_of_tuples


def main():
    products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
    print(sort_prices(products))

if __name__ == '__main__':
    main()