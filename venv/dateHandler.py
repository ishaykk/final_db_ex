def set_day(day):
    if 0 < day <= 31:
        return day
    else:
        return 1

def set_month(month):
    if 0 < month <= 12:
        return month
    else:
        return 1

def set_year(year):
    if 0 < year <= 9999:
        return year
    else:
        return 2019

def date_format():
    day, month, year = map(int, input('Enter start date in DD/MM/YYYY format: ').split('/'))
    day = set_day(day)
    month = set_month(month)
    year = set_year(year)
    print(str(year)+"-"+str(month)+"-"+str(day))
    return str(year)+"-"+str(month)+"-"+str(day)


