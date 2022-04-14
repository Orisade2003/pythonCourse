def squared_numbers(start, stop):
    """
    :param start: the bottom border number
    :type start: int
    :param stop: top border number
    :type stop: int
    the function prints the squares of all numbers between start and stop, including them both
    """
    i=start
    while i in range(start, stop + 1):
        print(i**2)
        i+=1

def main():
    start = input("Enter Bottom Border")
    stop = input("Enter Top Border")
    squared_numbers(start,stop)

if __name__ == '__main__':
    main()