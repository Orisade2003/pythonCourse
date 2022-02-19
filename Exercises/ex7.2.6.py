def print_menu():
    """
    the function prints the main menu 
    """
    menu = """
    1.Print Grocery List
    2.Print Size Of List
    3.Is item in list?
    4.How Many Times is Item In List?
    5.Delete Item from list
    6.Add item to list
    7.Print non valid Items
    8.Delete duplicates from list
    9.Exit
    """
    print(menu)


def list_manager(grocery_list):
    """
    
    :param grocery_list: grocery list given by the user
    :return: the function lets the user do different action regarding the grocery
    """
    print_menu()
    option = input("Enter The number of the option you want to choose:\n")
    option = int(option)
    while option != 9:
        list_groceries = grocery_list.split(",")
        if option == 1:
            print(grocery_list)
        elif option == 2:
            print(grocery_list.count(",") + 1)
        elif option == 3:
            item = input("Enter the name of the item you are looking for")
            if (item in list_groceries):
                print("Yes")
            else:
                print("No")

        elif option == 4:
            item = input("Enter the name of the item you are looking for")
            print(list_groceries.count(item))

        elif option == 5:
            item = input("Enter the name of the item you want to remove from list")
            if item in list_groceries:
                list_groceries.remove(item)
                grocery_list = ",".join(grocery_list)
            else:
                print("Item not in list")

        elif option == 6:
            item = input("Enter the name of the item you want to add to the list")
            list_groceries.append(item)
            grocery_list = ".".join(list_groceries)

        elif option == 7:
            for item in list_groceries:
                if (len(item) < 3 or not item.isalpha()):
                    print(item)

        elif option == 8:
            for item in list_groceries:
                if(list_groceries.count(item)>1):
                    list_groceries.remove(item)

        print_menu()
        option = int(input("Enter The number of the option you want to choose:\n"))


def main():
    grocery_list_manager = input("Enter list, Seperate items with ',' and no spaces")
    list_manager(grocery_list_manager)

if __name__ == '__main__':
    main()