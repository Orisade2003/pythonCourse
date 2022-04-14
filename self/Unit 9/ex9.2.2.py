def copy_file_content(source, destination):
    """
    :param source: source file
    :type source: string
    :param destination: destination file
    :type destination: string
    the function copies the content of source file to the destination file
     """
    source_file = open(source, 'r')
    source_content = source_file.read()
    source_file.close()
    dest_file = open(destination, 'w')
    dest_file.write(source_content)
    dest_file.close()


def main():
    src = r"/file1"
    dest = r"C:\Users\ORI\PycharmProjects\sigitCourse\file2"
    copy_file_content(src, dest)


if __name__ == '__main__':
    main()
