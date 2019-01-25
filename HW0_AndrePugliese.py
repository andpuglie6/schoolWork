print("#Andre Pugliese")
print("#CS 100-H01")
print("#HW 0, Sept 6, 2017")
print("")

print("#Exercise 5b")
months = 12
days = 365
hours = 8760

print("#Exercise 5c")
height = 1.7526
weight = 79.3787
price = 2.99

print("#Exercise 5d")
desertAnimal = 'Camel'
polarBird = 'Penguin'
operatingSystemCat = 'Cheetah'

# Exercise 1.1
# A. If you leave out one of the parentheses, you get a syntax error reading “SyntaxError: unexpected EOF while parsing”. If you leave out both of the parentheses, you get a syntax error reading “SyntaxError: invalid syntax”.
# B. If you leave out one of the quotation marks, you get a syntax error reading “SyntaxError: EOL while scanning string literal”. If you leave out both of the quotation marks, you get a semantics error reading “NameError: name 'cat' is not defined”.
# C. If you put a plus sign before a number, the number when printed will read as a positive integer or float when printed. 2++2 will print as a sum (4).

# Exercise 1.2
exerciseOneTwoA = (42*60)+42
print(exerciseOneTwoA)
# A. There are 2562 seconds in 42 minutes 42 seconds.

exerciseOneTwoB = 10 / 1.61
print(exerciseOneTwoB)
# B. There are 6.2111801242236018 miles in 10 kilometers.

exerciseOneTwoCA = exerciseOneTwoA / exerciseOneTwoB # seconds per mile
print(exerciseOneTwoCA)

exerciseOneTwoCB = exerciseOneTwoCA / 60 # minutes per mile (seconds divided by 60)
print(exerciseOneTwoCB)

exerciseOneTwoCC = 60 / exerciseOneTwoCB # miles per hour
print(exerciseOneTwoCC)
# C. Your average pace in seconds per mile is 412.482 and your average pace in minutes per mile is 6.874700000000001. Your average speed in miles per hour is 8.727653570337614.

# Exercise 2.1
# A. “42 - n” is not legal as it has no defined value and results in a name error. It is essentially a variable with no value.
# B. x = y = 1 is legal as it has a defined value across two variables. They are equivalent.
# C. Nothing happens if you put a semicolon at the end of a Python statement. The program runs as if nothing changed.
# D. A period at the end of statement (excluding a float value) will run an error reading “SyntaxError: invalid syntax”.
# E. If you try that in Python, an error will read “NameError: name 'xy' is not defined” as python understands the syntax as a separate variable. In order to multiply you need the notation x*y.

# Exercise 2.2
exerciseTwoTwoA = (4/3) * (3.14) * (5**3)
print(exerciseTwoTwoA)
# A. The volume of a sphere with radius 5 is about 523.3333333333334 units^3.

exerciseTwoTwoB = ((24.95-(24.95*40.0/100.0))*60) + 3 + (0.75*59)
print(exerciseTwoTwoB)
# B. The total wholesale cost of the books is $945.45.

startTime = (((6*60)+52)*60) # in seconds
easyPace = ((8*60+15)*2) # minutes-seconds*number of times
fastPace = ((7*60+12)*3)
hour = (startTime + easyPace + fastPace)/(60*60.0) #cumulative time divided by seconds to minutes to hours
minuteDif = (startTime + easyPace + fastPace)//(60*60) # not going to lie I had to look this one up, i'm pretty sure floored allows you to change from a float to an int
minute = (hour - minuteDif)*60
print(int (hour),":", int (minute))
# B. The arrival time is 7:30 AM.

