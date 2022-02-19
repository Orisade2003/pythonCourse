def shift_left(my_list):
    """
    :param my_list: a list with a length of 3
    the function shifts the list one shift left
    """
    my_list[0], my_list[1], my_list[2] = my_list[1], my_list[2],my_list[0]

def main():
    l = [0,1,2]
    shift_left(l)
    print(l)

if __name__ == '__main__':
    main()