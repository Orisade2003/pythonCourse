def who_is_missing(file_name):
    """
    :param file_name: file containing non sorted numbers from 1 to n, with one number missing
    the function finds the missing numbers and writes it to a file called found.txt
    """
    missing_file = open(file_name,'r')
    file_content = missing_file.read()
    file_numbers = file_content.split(",")

    found = False
    for i in file_numbers:
        i = int(i)
    max_num = int(max(file_numbers))
    for i in range(1, max_num+1):
        if i not in file_numbers:
            found_file = open("found.txt", "w")
            found_file.write(str(i))
            Found = True
    if not found:
        found_file = open("found.txt", "w")
        found_file.write(str(max_num+1))

def main():
    who_is_missing(r"C:\Users\ORI\PycharmProjects\sigitCourse\file1")

if __name__ == '__main__':
    main()