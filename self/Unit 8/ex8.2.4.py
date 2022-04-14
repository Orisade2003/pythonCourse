def are_anagrams(string1, string2):
    """
    :param string1: first string
    :type string1: string
    :param string2: second string
    :type string2: string
    :return: if the strings are Anagrams of one another, the function returns True, otherwise it returns False
    :rtype: Boolean
    """
    for char in string1:
        if (string1.count(char) != string2.count(char)):
            return False
    return True

def sort_anagrams(list_of_strings):
    """
    :param list_of_strings: list of strings
    :type list_of_strings: list
    :return: the function returns a list of lists, each list inside the list, contains the words from
    list_of_strings which are anagrams of one another
    :rtype: list
    """
    anagram_list = []
    for string in list_of_strings:
        anagrams_of_string = [string]
        for maybe_anagram in list_of_strings:
            if are_anagrams(string,maybe_anagram):
                anagrams_of_string.append(maybe_anagram)
                list_of_strings.remove(maybe_anagram)
        anagram_list.append(anagrams_of_string)
    return anagram_list

def main():
    list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters',
                     'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
    print(sort_anagrams(list_of_words))

if __name__ == '__main__':
    main()