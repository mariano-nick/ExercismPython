# http://exercism.io/exercises/python/leap/readme
class LeapYearChecker:
    def __init__(self, year):
        self.DivisibleByFour = False
        self.DivisibleByOneHundred = False
        self.DivisibleByFourHundred = False
        self.IsALeapYear = False
        try:
            year + 1
            self.Year = year
        except TypeError:
            raise Exception("Year is not addable, thus not an int")

    # there's probably a way to make this more efficient with only one is_div_by method
    def check_divisibility(self):
        self.is_divisible_by_four()
        self.is_divisible_by_one_hundred()
        self.is_divisible_by_four_hundred()

    def determine_if_leap_year(self):
        if self.DivisibleByFour:
            self.IsALeapYear = True

        if self.DivisibleByOneHundred:
            if self.DivisibleByFourHundred:
                self.IsALeapYear = True
            else:
                self.IsALeapYear = False

    def is_divisible_by_four(self):
        if self.Year % 4 == 0:
            self.DivisibleByFour = True

    def is_divisible_by_one_hundred(self):
        if self.Year % 100 == 0:
            self.DivisibleByOneHundred = True

    def is_divisible_by_four_hundred(self):
        if self.Year % 400 == 0:
            self.DivisibleByFourHundred = True


def is_leap_year(year):
    leap_year_checker = LeapYearChecker(year)
    leap_year_checker.check_divisibility()
    leap_year_checker.determine_if_leap_year()

    return leap_year_checker.IsALeapYear
