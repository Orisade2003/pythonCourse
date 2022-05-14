def gen_secs():
    """
    The function returns a generator of all numbers between 0 and 59
    Yields the numbers between 0 and 59, each calls it yields the next number
    :return:a generator of all numbers between 0 and 59
    :rtype: generator
    """
    for i in range(60):
        yield i


def gen_minutes():
    """
        The function returns a generator of all numbers between 0 and 59
        Yields the numbers between 0 and 59, each calls it yields the next number
        :return:a generator of all numbers between 0 and 59
        :rtype: generator
        """
    for i in range(60):
        yield i


def gen_hours():
    """
        A generator function which yields all the numbers between 0 23
        :return:a generator of all numbers between 0 and 23
        :rtype: generator
        """
    for i in range(0, 24):
        yield i


def gen_time():
    """
    A generator function which yields all the different possible combinations
    of hour, minute and second in a day
    :return:a generator function which yields all the different possible combinations
    of hour, minute and second in a day
    :rtype: generator
    """
    hour_gen = gen_hours()
    for hour in hour_gen:
        min_gen = gen_minutes()
        for minute in min_gen:
            sec_gen = gen_secs()
            for sec in sec_gen:
                time_tup = (hour, minute, sec)
                yield "%02d:%02d:%02d" % time_tup


def gen_year(start=2022):
    """
    A generator function which yields all years starting from the current one
    :param start: the starting year
    :type start: int
    :return: a generator function which yields all years from the current one until infinity
    :rtype: generator
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
    for month in range(1, 13):
        yield month


def gen_days(month, leap_year=True):
    """
    The function returns a generator containing the days in the given month, takes into account if the year is a leap
     year or not
    :param month: the month given to the function
    :type month: int
    :param leap_year: if the year is a leap year or not
    :type leap_year: bool
    :return: a generator containing the days in the given month, takes into account if the year is a leap year or not
    :rtype generator
    """
    months_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if leap_year and month == 2:
        for i in range(1, months_dict.get(month) + 2):
            yield i
    else:
        for i in range(1, months_dict.get(month) + 1):
            yield i


def gen_date():
    """
    A generator function which yields all the different possible times in
        dd/mm/yy hh:mm:ss format from the start of the given year until infinity
    :return: the function is a generator function which returns all the different possible times in
        dd/mm/yy hh:mm:ss format from the start of the given year until infinity
    :rtype: generator
    """
    year_gen = gen_year()
    while True:
        is_leap_year = False
        year = next(year_gen)
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
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
        if i % 1000000 == 0 and i != 0:
            print(g)
        i += 1


if __name__ == "__main__":
    main()
