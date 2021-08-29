# Design for Investigating 6174 constant

***bold text*** not bold

Functions:
- calcDiff(int) returns diff as a number
- findRepeating(numDigits, startInt) returns repeating number and num of diffs needed
- doRange(startNum, endNum, numDigits)


I need to find some way to explore this space.
- I want to explore all numbers 4-gigit from 0 to 9999.  I want to dewtermine if there is more than one number that repeats - and the answer is yes, of course because once you get to 6174, you go into a repeating pattern
- When dealing with 3 digit numbers, are there repeaing patterns?  What does a repeating pattern mean?
- When dealing with 5 digit numbers, are there repeating patterns?
  
# What does a repating pattern mean?
A repeating pattern means that you enter a loop with a start
number that goes around for a few steps (0 to n) but then comes back to the first start number.  So,
if you keep a list of numbers in the sequence, the moment you see a repeated number come up
then that is the entry point for a terminal loop.

The depth at which you need to go to get to the entry point of a loop is
the number of times you need to calculate the big/little difference  So,
the depth of 6174 is 0 and the depth of any other number from 0 to 9999 is 1 or more to 7 as a max.

Note that starting with 9721 or 7921 is the same because you are going to rearrange the digits.

This  is a test
