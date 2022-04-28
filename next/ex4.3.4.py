def get_fibo():
    """
    creates a generator which contains all numbers in the fibo sequence
    :yield type: int
    """
    first = 0
    second = 1
    while True:
        yield first
        yield second
        first += second
        second += first

def main():
    fibo_gen = get_fibo()
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))



if __name__ == "__main__":
    main()