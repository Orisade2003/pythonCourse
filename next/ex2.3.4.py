class Pixel:
    def __init__(self, x, y, red = 0, green = 0, blue = 0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        """
        :param x: x cord given by user
        :type x: int
        :param y: y cord given by user
        the function sets the coordinates of this instances to the given coordinates
        """
        self._x = x
        self._y = y

    def set_grayscale(self):
        """
        the function sets each of the colord of this instance to the average of its previous red, green and blue attributes
        """
        gray = self._blue + self._red + self._green
        gray //= 3
        self._red = gray
        self._blue = gray
        self._green = gray

    def print_pixel_info(self):
        """
        the function prints the attributes of the pixel and its color if only one of its color attributes has
        a value higher than 0
        """
        non_zero = ''
        if self._blue == 0 and self._green == 0:
            non_zero = 'Red'
        elif self._red == 0 and self._green == 0:
            non_zero = 'Blue'
        if self._blue == 0 and self._red == 0:
            non_zero = 'Green'
        print("X:", self._x, "Y:", self._y, "Color: (", str(self._red) + ", " + str(self._green) + ", " + str(self._blue) + ")",non_zero)


def main():
    p = Pixel(5,6, 250)
    p.print_pixel_info()
    p.set_grayscale()
    p.print_pixel_info()


if __name__ == '__main__':
    main()
