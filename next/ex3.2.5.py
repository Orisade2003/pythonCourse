def read_file(file_name):
    """
    :param file_name: file path given by the user
    :type file_name: string
    the function prints __CONTENT_START__ and then if the file exists it prints the content of the file
    otherwise it prints __NO_SUCH_FILE__, then it prints __CONTENT_END__
    """
    print("__CONTENT_START__")
    try:
        with open(file_name, "r") as txt_file:
            print(txt_file.read())
    except OSError:
        print("__NO_SUCH_FILE__")
    finally:
        print("__CONTENT_END__")


def main():
    file_path = input("Enter File Path")
    read_file(file_path)

if __name__ == '__main__':
    main()


