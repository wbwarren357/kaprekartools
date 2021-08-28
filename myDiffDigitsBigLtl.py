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


def myDiffDigitsBigLtl(myDigitStr):
    """Calculate difference between the largest and the
    smallest numbers that can be formed from the given 
    string of digits.

    Args:
        myDigitStr (str): String of digits in any order

    Raises:
        TypeError: myDigitStr is not a string of digits only

    Returns:
        int: the value of the biggest and littlest integers that can be formed
        by using all of the digits in the string once
    """

    # check if string is all digits
    if not(myDigitStr.isdecimal()):
        raise TypeError("digitStr is not all decimals")

    # create sorted versions of the digits string
    myBigLtlSortStr = ''.join(sorted(myDigitStr))
    myLtlBigSortStr = ''.join(sorted(myDigitStr, reverse=True))

    # call helpers to compute big and ltl
    myBigValue = myDiffDigitsBigLtlHlpr(myBigLtlSortStr)
    myLtlValue = myDiffDigitsBigLtlHlpr(myLtlBigSortStr)

    return (myBigValue - myLtlValue)


# ###############################################
# Helper function


def myDiffDigitsBigLtlHlpr(myDigitStr):
    """Calculate difference between the largest and the
    smallest numbers that can be formed from the given 
    string of digits.

    Args:
        myDigitStr (str): String of digits in any order

    Raises:
        TypeError: myDigitStr is not a string of digits only

    Returns:
        int: the value of the biggest and littlest integers that can be formed
        by using all of the digits in the string once
    """

    # check if string is all digits
    if not(myDigitStr.isdecimal()):
        raise TypeError("digitStr is not all decimals")

    # create sorted versions of the digits string
    myBigLtlSortStr = ''.join(sorted(myDigitStr))
    myLtlBigSortStr = ''.join(sorted(myDigitStr, reverse=True))

    # call helpers to compute big and ltl
    myBigValue = myDiffDigitsBigLtlHlpr(myBigLtlSortStr)
    myLtlValue = myDiffDigitsBigLtlHlpr(myLtlBigSortStr)

    return (myBigValue - myLtlValue)


print(myDiffDigitsBigLtl("0"))
print(myDiffDigitsBigLtl("19"))
print(myDiffDigitsBigLtl("828"))
print(myDiffDigitsBigLtl("6174"))
print(myDiffDigitsBigLtl("07824"))
print(myDiffDigitsBigLtl("777777"))
