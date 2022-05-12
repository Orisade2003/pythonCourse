def iter_practice():
    """
    the function prints the number between 1 and 100 (including) in jumps of 3
    """
    numbers = iter(list(range(1, 101)))
    for i in numbers:
        try:
            i = next(numbers)
            i = next(numbers)
            print(i)
        except StopIteration as e:
            print('Done')


def main():
    iter_practice()


if __name__ == "__main__":
    main()
