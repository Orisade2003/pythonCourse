import calendar


def weekday():
    date_input = input("Enter A date")
    day = int(date_input[:2])
    month = int(date_input[3:5])
    year = int(date_input[6:])
    day_of_week = calendar.weekday(year, month, day)
    if day_of_week == 0:
        print("Monday")
    if day_of_week == 1:
        print("Tuesday")
    if day_of_week == 2:
        print("Wednesday")
    if day_of_week == 3:
        print("Thursday")
    if day_of_week == 4:
        print("Friday")
    if day_of_week == 5:
        print("Saturday")
    if day_of_week == 6:
        print("Sunday")


if __name__ == "__main__":
    weekday()
