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

    # check if string is all digits
    if not(type(strtInt) is int):
        raise TypeError("strtInt not integer")

    # create sorted versions of the digits string
    myBigLtlSortStr =
    myLtlBigSortStr =

    # call helpers to compute big and ltl
    myBigValue = myDiffDigitsBigLtlHlpr(myBigLtlSortStr)
    myLtlValue = myDiffDigitsBigLtlHlpr(myLtlBigSortStr)

    return (myBigValue - myLtlValue)


print(mkRngSpc(0, 5))
