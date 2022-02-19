def func1(num1,num2):
    """
    the function adds num1 and num2, and divides them by(num1-num2)
    :param num1: a number
    :type num1: int
    :param num2: a number
    :type num2: int
    :return: the function returns (num1+num2)/(num1-num2)
    :rtype: int
    """
    return (num1+num2)//(num1-num2)

def main():
    num1 = input("Enter the first number")
    num2 = input("Enter the second number")
    print(func1(int(num1),int(num2)))

if __name__ == "__main__":
    main()
