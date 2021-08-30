# Functions for Kaprekar's Constant Investigations

import functools
from logging import *
from sys import *


# ###############################################
# Find DiffDigit Stoppers
# 1.  myFindDiffDigitStoppers = myFindDiffDigitStoppers(myStartInt, myEndInt, myNumDigits, myNTimes)
#       if myStartInt >= myEndInt
#       if myStartInt or myEndInt not positive integers
#       if myNumDigits not an integer > 1
#       if myNTimes not an integer > 0

#        if myNumDigits not int and < 1 then error
#        if myDigitStr empty, then error
#        if myDigitStr not all digits then error
#        if myNTimes not int not > 0 then error
#        if result(N+1) == result (N), stops immediately
#        return(result of doing myDiffDigitsBigLtl on arguments N times, "found end", number of diffDigit done)


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
