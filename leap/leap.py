"""
Module to determine if a year is a Leap Year
"""
def is_leap_year(year):
    """
    Given: an int representing the year
    Returns: True if it is a leap year, False otherwise
    """
    if not isinstance(year, int):
        raise ValueError("is_leap_year requires a variable of type int")
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        return True
    return False
