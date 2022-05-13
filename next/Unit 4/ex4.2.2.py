def parse_ranges(ranges_string):
    """
    The function returns a generator containing all the numbers in the given ranges
    :param ranges_string: a string representing the ranges of numbers
    :type ranges_string: str
    :return: a generator containing all the numbers in the given ranges
    :rtype: generator
    """
    all_ranges = ranges_string.split(",")
    ranges = (i.split('-') for i in ranges_string.split(','))
    result = (i for start, end in ranges for i in range(int(start),int(end)+1))
    return result


def main():
    print(list(parse_ranges("1-2,4-4,8-10")))
    print(list(parse_ranges("0-0,4-8,20-21,43-45")))


if __name__ == "__main__":
    main()
