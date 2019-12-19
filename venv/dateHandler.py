def set_day(day):
    """
    Method receive an int and validate that it's between 1-31
    :param day: day of the month
    :return: day if it's valid, else return 1 by default
    """
    if 0 < day <= 31:
        return day
    else:
        return 1

def set_month(month):
    """
    Method receive an int and validate that it's between 1-12
    :param month: month of the year
    :return: month if it's valid, else return 1 by default
    """
    if 0 < month <= 12:
        return month
    else:
        return 1

def set_year(year):
    """
    Method receive an int and validate that it's between 1-9999
    :param year: year number
    :return: year if it's valid, else return 2019 by default
    """
    if 0 < year <= 9999:
        return year
    else:
        return 2019

def date_format():
    """
    Method get Date input from user in DD/MM/YYYY format, validate it and return it in YYYY-MM-DD
    :return: a string of date in YYYY-MM-DD format
    """
    day, month, year = map(int, input('Enter start date in DD/MM/YYYY format: ').split('/'))
    day = set_day(day)
    month = set_month(month)
    year = set_year(year)
    return str(year)+"-"+str(month)+"-"+str(day)


