class Animal:
    def __init__(self, name, hunger=0):
        """
        :param name:name of animal
        :type name: string
        :param hunger: hunger attribute of animal, 0 by default
        type hunger: int
        the function sets the attributes of the animal and creates a new instance

        """
        self._hunger = hunger
        self._name = name
        self._zoo_name = "Hayaton"

    def get_name(self):
        """
        :return:name of the animal
        :rtype name: string
        """
        return self._name

    def is_hungry(self):
        """
        :return: True if animal is hungry and False otherwise
        :rtype: bool
        """
        return self._hunger > 0

    def feed(self):
        """
        feeds the animal and decreases its feed attribute by 1
        """
        self._hunger -= 1

    def talk(self):
        pass


class Dog(Animal):
    def __init__(self, name, hunger):
        """
        :param name:name of the dog
        :type name: string
        :param hunger: hunger attribute of dog
        :type hunger: int
        """
        super().__init__(name, hunger)

    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        """
        the function prints 'There you go, sir!'
        """
        print("There you go, Sir!")


class Cat(Animal):
    def __init__(self, name, hunger):
        """
            :param name:name of the cat
            :type name: string
            :param hunger: hunger attribute of the cat
            :type hunger: int
        """
        super().__init__(name, hunger)

    def talk(self):
        print("meow")

    def chase_laser(self):
        """
        the function prints 'Meeeeow'
        """
        print("Meeeeow")


class Skunk(Animal):
    def __init__(self, name, hunger):
        """
            :param name:name of the skunk
            :type name: string
            :param hunger: hunger attribute of the skunk
            :type hunger: int
            the function sets the stink_count attribute of the skunk to 6
               """
        super().__init__(name, hunger)
        self._stink_count = 6

    def talk(self):
        print("tsssss")

    def stink(self):
        """
        the function prints 'Dear lord!'
        """
        print("Dear lord!")

class Unicorn(Animal):
    def __init__(self, name, hunger):
        """
           :param name:name of the unicorn
           :type name: string
           :param hunger: hunger attribute of the uniorn
           :type hunger: int
       """
        super().__init__(name, hunger)

    def talk(self):
        print("Good day, darling")

    def sing(self):
        """
                the function prints "I'm not your toy"
        """
        print("I’m not your toy...	")


class Dragon(Animal):
    def __init__(self, name, hunger):
        """
           :param name:name of the dragon
           :type name: string
           :param hunger: hunger attribute of the dragon
           :type hunger: int
           the function sets the color attribute of the dragon to 'Green'
        """
        super().__init__(name, hunger)
        self._color = "Green"

    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        """
        the function prints '$@#$#@$'
        """
        print("$@#$#@$	")


def main():
    dog = Dog("Brownie", 10)
    cat = Cat("Zelda", 3)
    skunk = Skunk("Stinky", 0)
    uni = Unicorn("Keith", 7)
    drag = Dragon("Lizzy", 1450)
    doggo = Dog("Doggo",80)
    kitty = Cat("kitty", 80)
    stinkyjr = Skunk("Stinky Jr.",80)
    clair = Unicorn("Clair", 80)
    mcfly = Dragon("McFly",80)
    zoo_lst = [dog, cat, skunk, uni, drag, doggo, kitty, stinkyjr, clair, mcfly]
    for animal in zoo_lst:
        if animal.is_hungry():
            print(animal.__class__.__name__, animal.get_name())
            animal.talk()
            if isinstance(animal, Dog):
                animal.fetch_stick()
            if isinstance(animal, Cat):
                animal.chase_laser()
            if isinstance(animal, Skunk):
                animal.stink()
            if isinstance(animal, Unicorn):
                animal.sing()
            if isinstance(animal, Dragon):
                animal.breath_fire()
        while animal.is_hungry():
            animal.feed()
    print(mcfly._zoo_name)


if __name__ == '__main__':
    main()
