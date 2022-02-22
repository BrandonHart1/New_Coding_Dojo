# Basic - Print all integers from 0 to 150.

from functools import total_ordering


for n in range(151):
    print(n)


# -------------------------------------------
# Multiples of Five - Print all the multiples of 5 from 5 to 1,000

for n in range(5, 1005, 5):
    print(n)

# -------------------------------------------
# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

for n in range(1,100):
    if n % 5 == 0:
        print("Coding")
    if n % 10 == 0:
        print("Coding Dojo")
    else:
        print(n)

# ---------------------------------------------------------------------------------
# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
total = 0

for n in range(1, 500000, 2):
        total += n
print(total)

# ----------------------------------------------------------------------------------
# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for n in range(2018, 0, -4):
    print(n)


# -------------------------------------------------------------------------------
# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

lowNum = 150
highNum = 900
mult = 15

for n in range(lowNum, highNum, mult):
    print(n)