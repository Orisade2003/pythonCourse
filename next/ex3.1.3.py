
def iterError():
    """
    this function provides an example of an iteration error
    """
    lst = [1,2,3]
    iterat = iter(lst)
    for i in range(4):
        print(next(iterat))

def zeroDiv():
    """
        this function provides an example of a Zero Division Error
    """
    return 5/0


def assertionError():
    """
           this function provides an example of an Assertion Error
       """
    y = 0
    assert y!=0
    print(y)

def importError():
    """
           this function provides an example of an Import Error
       """
    from math import fjds

def keyError():
    """
           this function provides an example of a Key Error
       """
    my_dict = {1:2, 3:4,5:6}
    print(my_dict[9])

def syntaxError():
    """
           this function provides an example of a Syntax Error
       """
    print "hello"

def indentationError():
    """
           this function provides an example of an Indentation Error
       """
    if 6 > 5:
    print("hello")

def typeError():
    """
           this function provides an example of a type error
       """
    a = 1
    my_str = "hello world"
    print(a + my_str)

def main():
    """
    iterError()
    zeroDiv()
    assertionError()
    importError()
    keyError()
   syntaxError()
   indentationError()
   typeError()
   """
if __name__ == '__main__':
    main()