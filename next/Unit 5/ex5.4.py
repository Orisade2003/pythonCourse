import functools


def check_id_valid(id_number):
    """
     The function checks if a number is a valid id NUMBER
    :param id_number: number given by the user
    :type id_number: int
    :return: True if id_number is a valid id number and False otherwise
    :rtype: bool
    """
    num_list = []
    iter_count = 1
    while id_number > 0:
        if iter_count % 2 == 1:
            num_list.append(id_number % 10)
        else:
            num_list.append((id_number % 10) * 2)
        iter_count += 1
        id_number //= 10
    id_sum = functools.reduce(lambda a, b: a + b // 10 + b % 10,
                              num_list)  # the lambda function adds the numbers created after multiplying each digit
    # in the ID nuber by 1 or two according the rules, if after the multiplication a digit becomes a number larger
    # than 9, it adds its 2 digits and uses them for the calculation
    return id_sum % 10 == 0 and len(num_list) == 9


class IDIterator:
    """
    The class represents an IDIterator, which creates valid ID's starting from a given one
    """

    def __init__(self, id):
        """
        The function initializes an IDIterator
        :param id: Id number given to the function
        :type id: int
        """
        self._id = id

    def __iter__(self):
        """
        :return: this current instance of IDIterator
        :rtype: IDIterator
        """
        return self

    def __next__(self):
        """
        :return: the function returns the legal ID number after self._id
        :rtype: int
        :raise StopIteration: raises an exception
        """
        for num in range(self._id + 1, 999999999 + 1):
            if check_id_valid(num):
                self._id = num
                return num
        raise StopIteration


def id_generator(id_num):
    """
    A generator function that finds the next legal ID number after id_num
    :param id_num:an ID number given by to the function
    :type id_num: int
    :return: The next legal ID num after id_num
    :rtype: int
    """
    for num in range(id_num + 1, 1000000000):
        if check_id_valid(num):
            id_num = num
            yield id_num


def main():
    """print(check_id_valid(123456780))
    print(check_id_valid(123456782))
    id_num = int(input("Please Enter ID"))
    id_iter = IDIterator(id_num)
    for i in range(10):
        print(next(id_iter))
    id_gen = id_generator(id_num)
    for i in range(10):
        print(next(id_gen))"""
    id_num = int(input("Enter ID "))
    mode = input("Generator or Iterator? (gen/it)? ")
    if mode == "gen":
        id_gen = id_generator(id_num)
        for i in range(10):
            print(next(id_gen))
    elif mode == "it":
        id_iter = IDIterator(id_num)
        for i in range(10):
            print(next(id_iter))


if __name__ == "__main__":
    main()
