class Turtle:
    def __init__(self):
        """
        the function sets the default values to the turtle's attributes
        """
        self.name = 'Master Oogway'
        self.age = 0

    def birthday(self):
        """
        the function increases the age of the turtle by one
        """
        self.age += 1

    def get_age(self):
        """
        :return: the age of this instance of the turtle
        :rtype int
        """
        return self.age


def main():
    t1 = Turtle()
    t2 = Turtle()
    t1.birthday()
    print(t1.get_age())
    print(t2.get_age())


if __name__ == '__main__':
    main()
