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
    myBigLtlSortStr = ''.join(sorted(myDigitStr, reverse=True))
    myLtlBigSortStr = ''.join(sorted(myDigitStr))

    # call helpers to compute big and ltl
    myBigValue = int(myBigLtlSortStr)
    myLtlValue = int(myLtlBigSortStr)

    return (myBigValue - myLtlValue)


myTest = "0"
print("diff of " + myTest + " = " + str(myDiffDigitsBigLtl(myTest)))
myTest = "12"
print("diff of " + myTest + " = " + str(myDiffDigitsBigLtl(myTest)))
myTest = "312"
print("diff of " + myTest + " = " + str(myDiffDigitsBigLtl(myTest)))
myTest = "4716"
print("diff of " + myTest + " = " + str(myDiffDigitsBigLtl(myTest)))
myTest = "09988"
print("diff of " + myTest + " = " + str(myDiffDigitsBigLtl(myTest)))
myTest = "777711"
print("diff of " + myTest + " = " + str(myDiffDigitsBigLtl(myTest)))
