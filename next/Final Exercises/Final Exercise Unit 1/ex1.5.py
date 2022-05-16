import functools


def longest_name(file_path):
    """
    The function returns the longest name in the file
    :param file_path: file path of names.txt, each name must be on a different line
    :type file_path: string
    :return: the longest name in the file
    :rtype: str
    """
    with open(file_path, 'r') as names_list:
        print(functools.reduce(lambda a, b: a if len(a) >= len(b) else b, names_list.read().split("\n")))


def sum_lens(file_path):
    """
    The function calculates the sum of the lengths of the names in the file
    :param file_path:  file path of names.txt, each name must be on a different line
    :type file_path: string
    :return: the sum of all the lengths of the names
    :rtype: int
    """
    with open(file_path, 'r') as names_list:
        print(functools.reduce(lambda a, b: len(a) + len(b) if type(a) is str else a + len(b), names_list.read().split("\n")))


def shortest_names(file_path):
    """
    The function prints the shortest names in the given file
    :param file_path: file path of names.txt, each name must be on a different line
    :type file_path: string
    the function prints the names with the least amount of letters
    """
    with open(file_path, 'r') as names_list:
        shortest_len = functools.reduce(lambda a, b: min(a, len(b)) if type(a) is int else (min(len(a), len(b))), names_list.read().split("\n"))
        names_list.seek(0)
        print("\n".join(list(filter(lambda x: len(x) == shortest_len, names_list.read().split("\n")))))


def write_name_len(file_path):
    """
    The function writes in a new file the length of the names in the given file
    :param file_path: file path of names.txt, each name must be on a different line
    :type file_path: string
    the function writes to a file called name_length.txt the length of each of the names
    """
    with open(file_path, 'r') as names_list:
        open("name_length.txt", 'w').write("\n".join(list(map(lambda x: str(len(x)), names_list.read().split("\n")))))


def names_with_len(file_path, wanted_len):
    """
    The function finds all the names with the wanted length and prints them
    :param file_path:file path of names.txt, each name must be on a different line
    :type file_path: string
    :param wanted_len: the length of the names the user wants to print
    the function prints the names that are in the file_path with the given names
    """
    with open(file_path, 'r') as names_list:
        print("\n".join(list(filter(lambda x: len(x) == wanted_len, names_list.read().split("\n")))))


def main():
    longest_name(r"names")
    sum_lens(r"names")
    shortest_names(r"names")
    write_name_len(r"names")
    length = int(input("Enter The Length of the name: "))
    names_with_len(r"names", 4)


if __name__ == '__main__':
    main()
