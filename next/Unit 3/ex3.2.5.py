def read_file(file_name):
    """
    the function returns a string which's value is __CONTENT_START__ and then if the file exists it adds to the string
    the content of the file
    otherwise it adds to the string __NO_SUCH_FILE__, then it adds __CONTENT_END__
    :param file_name: file path given by the user
    :type file_name: string
    return: the function returns a string which's value is __CONTENT_START__ and then if the file exists it adds to the
    string the content of the file
    otherwise it adds to the string __NO_SUCH_FILE__, then it adds __CONTENT_END__
    :rtype: str
    """
    output = "__CONTENT_START__"
    try:
        txt_file = open(file_name, 'r')
    except OSError:
        output += "\n__NO_SUCH_FILE__"
    else:
        output += '\n'
        output += txt_file.read()
        txt_file.close()
    finally:
        output += "\n__CONTENT_END__"
    return output


def main():
    file_path = input("Enter File Path")
    print(read_file(file_path))


if __name__ == '__main__':
    main()
