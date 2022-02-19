def are_files_equal(file1, file2):
    """
    :param file1: first file given by the user
    :param file2: second file given by the user
    :return: True if the content of both files are the same and False otherwise
    """
    opened_file = open(file1, "r")
    opened_file2 = open(file2, "r")
    file1_content = opened_file.read()
    file2_content = opened_file2.read()
    opened_file.close()
    opened_file2.close()
    return file1_content == file2_content

def main():
    file1 = r"C:\Users\ORI\PycharmProjects\sigitCourse\file1"
    file2 = r"C:\Users\ORI\PycharmProjects\sigitCourse\file2"
    print(are_files_equal(file1,file2))

if __name__ == '__main__':
    main()