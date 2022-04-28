def parse_ranges(ranges_string):
    """
    :param ranges_string: a string representing the ranges of numbers
    :type ranges_string: str
    :return: a generator containing all the numbers in the given ranges
    :rtype: generator
    """
    all_ranges = ranges_string.split(",")
    range_list = []
    ranges = (i for r in all_ranges for i in range(int(r[0:r.find('-')]), int(r[r.find('-')+1:])+1))
    return ranges





def main():
    print(list(parse_ranges("1-2,4-4,8-10")))
    print(list(parse_ranges("0-0,4-8,20-21,43-45")))

if __name__ == "__main__":
    main()