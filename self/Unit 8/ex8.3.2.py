def print_options():
    """
    the function prints mariah's menu
    """
    options = """
    1.Print Mariah's Family name
    2.Print Mariah's birth month
    3.Print Number of hobbies
    4.Print last hobby in hobby list
    5.Add "Cocking" as a hobby
    6.Make DOB a tuple and print it
    7.Add a new age key to the dictionary and print it    
    """


def age_calc(current_date, birthdate):
    """
    :param current_date: the current date
    :type current_date: tuple
    :param birthdate: the birth date of the person whose age we want to calculate
    :type birthdate:tuple
    :return: the function returns the age of the person whose age we want to calculate
    :rtype: int
    """
    current_date_day = int(current_date[0])
    current_date_month = int(current_date[1])
    current_date_year = int(current_date[2])
    birthdate_day = int(birthdate[0])
    birthdate_month = int(birthdate[1])
    birthdate_year = int(birthdate[2])

    if (current_date_month > birthdate_month):
        return current_date_year - birthdate_year
    elif current_date_month == birthdate_month:
        if (current_date_day >= birthdate_day):
            return current_date_year - birthdate_year
    return current_date_year - birthdate_year - 1


def mariah_dict():
    """
     the function lets the user see information and interact with the data about Mariah Carey
    """
    mariah_carey = {"first_name": "Mariah", "last_name": "Carey", "birth_date": "27.03.1970",
                    "hobbies": ["Sing", "Compose", "Act"]}
    current_date = (19,2,2022)
    print_options()
    action = int(input("Enter the action you want to do"))
    while 0 < action < 8:
        if action == 1:
            print(mariah_carey["last_name"])
        elif action == 2:
            print(mariah_carey["birth_date"][3:5])
        elif action == 3:
            print(len(mariah_carey["hobbies"]))
        elif action == 4:
            print(mariah_carey["hobbies"][-1])
        elif action == 5:
            mariah_carey["hobbies"].append("Cooking")
        elif action == 6:
            mariah_birthdate = mariah_carey["birth_date"]
            mariah_carey["birth_date"] = mariah_birthdate[:2], mariah_birthdate[:3:5], mariah_birthdate[6:10]
            print(mariah_carey["birth_date"])
        elif action == 7:
            mariah_birthdate = mariah_carey["birth_date"]
            if type(mariah_carey["birth_date"]) is str:
                mariah_carey_age = age_calc(current_date,(mariah_birthdate[:2], mariah_birthdate[:3:5], mariah_birthdate[6:10]))
                mariah_carey["Age"] = mariah_carey_age
                print(mariah_carey["Age"])
            else:
                mariah_carey["Age"] = age_calc(current_date,mariah_carey["birth_date"])
                print(mariah_carey["Age"])
        print_options()
        action = int(input("Enter the action you want to do"))

def main():
    mariah_dict()



if __name__ == '__main__':
    main()