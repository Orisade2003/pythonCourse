def mult_tuple(tuple1, tuple2):
    """
    :param tuple1: the first tuple given by the user
    :type tuple1: tuple
    :param tuple2: the second tuple given by the user
    :type tuple2: tuple
    :return: the function returns a tuple in which each item is a tuple, each tuple is a possible combination
            of 2 items, one from tuple1 and one from tuple2, the function returns a tuple which contains all
            the possible combinations
    :rtype: tuple
    """
    tup_of_tups = ()
    for i in tuple1:
        for j in tuple2:
            tup_of_tups = tup_of_tups + ((i,j),)
            tup_of_tups = tup_of_tups + ((j,i),)
    return tup_of_tups

def main():
    first_tuple = (1,2,3)
    second_tuple = (4,5,6)
    print(mult_tuple(first_tuple, second_tuple))

if __name__ == '__main__':
    main()
