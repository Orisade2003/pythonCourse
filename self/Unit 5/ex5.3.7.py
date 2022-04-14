def chocolate_maker(small, big, x):
    if type(x) is int:
        if x <= small:
            return True
        if x % 5 == 0 and x // 5 <= big:
            return True
        if (x - 5 * big >= 0) and x % 5 <= small:
            return True
        max_fives = x // 5
        if 0 <= x - max_fives * 5 <= small:
            return True
    return False


if __name__ == "__main__":
    print(chocolate_maker(3, 1, 7))
