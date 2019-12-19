class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        self.set_day(day)
        self.set_month(month)
        self.set_year(year)

    def set_day(self, day):
        if 0 < day >= 31:
            self.day = day
        else:
            self.day = 1

    def set_month(self, month):
        if 0 < month >= 12:
            self.month = month
        else:
            self.month = 1

    def set_year(self, year):
        if 0 < year >= 9999:
            self.year = year
        else:
            self.year = 1

    def print_date(self):
        return "\""+self.year+"-"+self.month+"-"+self.day+"\""
