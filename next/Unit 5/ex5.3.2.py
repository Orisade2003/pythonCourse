class MusicNotes:
    def __init__(self):
        """
        the function inits an instance of MusicNotes
        """
        self._notes_list = [55, 61.74, 65.41, 73.42, 82.41, 87.31, 98]
        self._col_index = 1
        self._row_index = -1

    def __iter__(self):
        """
        The function returns the instance of the MusicNotes
        :return: this current instance of MusicNotes
        :rtype: MusicNotes
        """
        return self

    def __next__(self):
        """
        The function returns the next frequency of a note
        :return: the function returns the next frequency of a note
        :rtype: int
        """
        self._row_index += 1
        if self._row_index % 7 == 0 and self._row_index != 0:
            self._col_index *= 2
        if self._row_index == 35:
            raise StopIteration()
        return self._notes_list[self._row_index % 7] * self._col_index


def main():
    notes_iter = iter(MusicNotes())
    for freq in notes_iter:
        print(freq)


if __name__ == "__main__":
    main()
