class Turtle:
    count_animals = 0

    def __init__(self, name='Octavio'):
        """
        the function sets the default values to the turtle's attributes
        """
        self._name = name
        self._age = 0
        Turtle.count_animals += 1

    def birthday(self):
        """
        the function increases the age of the turtle by one
        """
        self._age += 1

    def get_age(self):
        """
        :return: the age of this instance of the turtle
        :rtype int
        """
        return self._age

    def set_name(self, name):
        """
        :param name: name given by the user
        :type name: string
        the function changes the name of this instance to name
        """
        self._name = name

    def get_name(self):
        """
        :return: the function returns the name of this instance of the class
        :rtype: string
        """
        return self._name


def main():
    t1 = Turtle("Oogway")
    t2 = Turtle()
    print(t1.get_name())
    t2.set_name("Turtle2")
    print(t2.get_name())
    print(Turtle.count_animals)


if __name__ == '__main__':
    main()
