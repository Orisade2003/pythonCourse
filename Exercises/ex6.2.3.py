def format_list(my_list):
    even_list = my_list[:len(my_list) - 1:2]
    even_list = ",".join(even_list)
    print(even_list + " and " + my_list[-1])

if __name__ == '__main__':
    my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
    format_list(my_list)