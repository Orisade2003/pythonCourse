def inverse_dict(my_dict):
    """
    :param my_dict: a dictionary
    :return: an inverse dictionary so that each eky in this dictionary is a value from my_dict,
    the value of each key is a list of the keys from my_dict which had the value equal that to the one of key
    in the new dictionary
    """
    inversed = {}
    for val in my_dict.values():
        if val not in inversed.keys():
            inversed[val] = []
    for key in my_dict.keys():
        inversed[my_dict[key]].append(key)
    return inversed

def main():
    course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
    print(inverse_dict(course_dict))

if __name__ == '__main__':
    main()