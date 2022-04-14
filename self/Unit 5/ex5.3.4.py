def last_early(my_str):
    my_str = my_str.lower()
    if my_str[-1] in my_str[:len(my_str)-1]:
        return True
    return False

if __name__ == "__main__":
    print(last_early("Wow"))