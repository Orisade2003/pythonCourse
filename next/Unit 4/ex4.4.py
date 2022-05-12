def gen_secs():
    """
    The function returns a generator of all numbers between 0 and 60 (non-inclusive)
    :return:a generator of all numbers between 0 and 60 (non-inclusive)
    :rtype: generator
    """
    sec_gen = (i for i in range(60))
    return sec_gen


def gen_minutes():
    """
    The function returns a generator of all numbers between 0 and 60 (non-inclusive)
        :return:a generator of all numbers between 0 and 60 (non-inclusive)
        :rtype: generator
        """
    min_gen = (i for i in range(60))
    return min_gen


def gen_hours():
    """
    The function returns a generator of all numbers between 0 and 24 (non-inclusive)
        :return:a generator of all numbers between 0 and 24 (non-inclusive)
        :rtype: generator
        """
    hour_gen = (i for i in range(0, 24))
    return hour_gen


def gen_time():
    """
    A generator function which yields all the different possible combinations
    of hour, minute and second in a day
    :return:a generator function which yields all the different possible combinations
    of hour, minute and second in a day
    :rtype: str
    """
    hour_gen = gen_hours()
    for i in range(24):
        min_gen = gen_minutes()
        hour = next(hour_gen)
        for j in range(60):
            sec_gen = gen_secs()
            minute = next(min_gen)
            for k in range(60):
                sec = next(sec_gen)
                time_tup = (hour, minute, sec)
                yield "%02d:%02d:%02d" % time_tup


def gen_year(start=2022):
    """
    A generator function which yields all years starting from the current one
    :param start: the starting year
    :type start: int
    :return: a generator function which yields all years from the current one until infinity
    :rtype: int
    """
    while True:
        yield start
        start += 1


def gen_months():
    """
    The function returns a generator of all the possible months numbers (1-13, not inclusive)
    :return: a generator of all the possible months numbers (1-13, not inclusive)
    :rtype: int
    """
    months_gen = (month for month in range(1, 13))
    return months_gen


def gen_days(month, leap_year=True):
    """
    The function returns a generator containing the days in the given month, takes into account if the year is a leap year or not
    :param month: the month given to the function
    :type month: int
    :param leap_year: if the year is a leap year or not
    :type leap_year: bool
    :return: a generator containing the days in the given month, takes into account if the year is a leap year or not
    :rtype generator
    """
    if month <= 7:
        if month % 2 == 1:
            return (i for i in range(1, 32))
        if month != 2:
            return (i for i in range(1, 31))
        if month == 2 and leap_year:
            return (i for i in range(1, 30))
        return (i for i in range(1, 29))
    else:
        if month % 2 == 1:
            return (i for i in range(1, 31))
        else:
            return (i for i in range(1, 32))


def gen_date():
    """
    A generator function which returns all the different possible times in
        dd/mm/yy hh:mm:ss format from the start of the given year until infinity
    :return: the function is a generator function which returns all the different possible times in
        dd/mm/yy hh:mm:ss format from the start of the given year until infinity
    :rtype: str
    """
    year_gen = gen_year()
    while True:
        is_leap_year = False
        year = next(year_gen)
        if year % 4 == 0 and year % 100 != 0 and year % 400 == 0:
            is_leap_year = True
        months_gen = gen_months()
        for month in months_gen:
            days_gen = gen_days(month, is_leap_year)
            for day in days_gen:
                for gt in gen_time():
                    date = (day, month, year)
                    yield ("%02d/%02d/%d " % date) + gt


def main():
    date_gen = gen_date()
    i = 0
    for g in date_gen:
        if i == 1000000:
            print(g)
            i = 0
        i += 1


if __name__ == "__main__":
    main()
