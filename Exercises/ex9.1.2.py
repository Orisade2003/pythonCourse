def file_funcs():
    """
    The function gets a file path from the user, and lets the user do different tasks on the file such as
    print each line in reverse order, sort the words in the file alphabetically with no duplicates and print
    the last n(number, input by the user) lines in the file
    sort - sort the words as stated above
    rev - print each line in reverse order
    last - print last n lines
    """
    file1 = input("Enter a File Path")
    task = input("Enter a task")
    opened_file = open(file1,'r')
    read_file = opened_file.read()
    if task == "sort":
        sorted_words = []
        for word in read_file.split():
            if word not in sorted_words:
                sorted_words.append(word)
        sorted_words.sort()
        print(sorted_words)
        return sorted_words
    if task == "rev":
        read_file = read_file.splitlines()
        for line in read_file:
            print(line[::-1])
    if task == "last":
        read_file = read_file.splitlines()
        n = int(input("Enter n please"))
        last_n_lines = read_file[len(read_file)-n:]
        for n in last_n_lines:
            print(n)
    opened_file.close()
def main():
    file_funcs()

if __name__ == '__main__':
    main()