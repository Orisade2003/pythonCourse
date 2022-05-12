def iter_error():
    """
        this function provides an example of an iteration error
    """
    lst = [1, 2, 3]
    iterat = iter(lst)
    for i in range(4):
        print(next(iterat))


def zero_div():
    """
        this function provides an example of a Zero Division Error
    """
    return 5 / 0


def assertion_error():
    """
       this function provides an example of an Assertion Error
    """
    y = 0
    assert y != 0
    print(y)


def import_error():
    """
           this function provides an example of an Import Error
       """
    from math import fjds


def key_error():
    """
           this function provides an example of a Key Error
       """
    my_dict = {1: 2, 3: 4, 5: 6}
    print(my_dict[9])


def syntax_error():
    """
           this function provides an example of a Syntax Error
       """
    print
    "hello"


def indentation_error():
    """
           this function provides an example of an Indentation Error
       """
    if 6 > 5:
        print("hello")


def type_error():
    """
           this function provides an example of a type error
       """
    a = 1
    my_str = "hello world"
    print(a + my_str)


def main():
    # iter_error()
    # zero_div()
    # assertion_error()
    #import_error()
    # key_error()
    # syntax_error()
    # indentation_error()
    # type_error()

if __name__ == '__main__':
    main()
