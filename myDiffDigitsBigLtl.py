# Functions for Kaprekar's Constant Investigations

import functools
from logging import *
from sys import *


# ###############################################
# Calculate biggest minus littlest from digits
# 1.  myDiffDigitsBigLtl = myDiffDigitsBigLtl(digitStr)
#        if digitStr empty, then error
#        if digitStr not all digits then error
#        return diffInt


def myDiffDigitsBigLtl(digitsStr):
    """Calculate difference between the largest and the
    smallest numbers that can be formed from the given 
    string of digits.

    Args:
        digitStr (str): String of digits in any order

    Raises:
        TypeError: digitStr is not a string of digits only

    Returns:
        int: the value of the biggest and littlest integers that can be formed
        by using all of the digits in the string once
    """
    if not(type(strtInt) is int):
        raise TypeError("strtInt not integer")
    if not(type(lnInt) is int):
        raise TypeError("lnInt not integer")
    if lnInt < 0:
        raise ValueError("lnInt not >= 0")
    return {"strt": strtInt, "ln": lnInt}


print(mkRngSpc(0, 5))
