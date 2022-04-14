class BigThing:
    def __init__(self, param):
            self._obj = param

    def size(self):
        """
        :return: if self._0bj is of type int, the function returns it, else it returns the length of the self._obj
        :rtype: int
        """
        if isinstance(self._obj, int):
            return self._obj
        return len(self._obj)


class BigCat(BigThing):
    def __init__(self, param, weight):
        super().__init__(param)
        self._weight = weight

    def size(self):
        """
        :return: The string 'Very Fat' if the weight of this instance of the cat is higher than 20, 'Fat' if it is higher than 15 and 'OK
         otherwise
        """
        if self._weight > 20:
            return "Very Fat"
        if self._weight > 15:
            return "Fat"
        return "Ok"

def main():
    my_thing = BigThing(12)
    print(my_thing.size())
    cutie = BigCat("mitzy", 22)
    print(cutie.size())
if __name__ == '__main__':
    main()