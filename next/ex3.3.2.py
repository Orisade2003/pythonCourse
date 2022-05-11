class UnderAgeException(Exception):
    def __init__(self, arg):
        """
        The function initializes an UnderAgeException
        :param arg: the age of the user
        :type arg: int
        """
        self._arg = arg

    def __str__(self):
        """
        the function tells the user that they can't gp to Ido's birthday party, it tells them their age
        and in how many years they will be able to go
        """
        params = (self._arg, 18 - self._arg)
        return "You are younger than 18, you are now %s, so you can't go to Ido's Birthday Party, " \
               "you will be able to go in %s years" % params

    def get_arg(self):
        """
        The function returns the age of the user
        :return: the age of the user for whom the exception was thrown
        :rtype: int
        """
        return self._arg


def send_invitation(name, age):
    """
    the function tells Ido he should invite the person if their age is 18 or above,
    the function throws and exception to show to any user who isn't yet 18, and tells them
    their age and in how many years they will be able to go to Ido's birthday party
    :param name: the name of the person who Ido might invite
    :type name: str
    :param age: the age of the person Ido might invite
    :type age: int
    """
    try:
        if int(age) < 18:
            raise UnderAgeException(age)
        print("You should send an invite to " + name)
    except UnderAgeException as e:
        print(e)


def main():
    send_invitation("Moshe", 20)
    send_invitation("Yonatan", 17)


if __name__ == "__main__":
    main()
