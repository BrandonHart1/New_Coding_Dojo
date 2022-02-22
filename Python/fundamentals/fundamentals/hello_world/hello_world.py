# 1. TASK: print "Hello World"
from tkinter import _TakeFocusValue


print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print("Hello," + name)	# with a comma
print("Hello " + name)	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello, " + str(name))	# with a comma
print( your code here )	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}").format(fave_food1, fave_food2) # with .format()
print( f"I love to eat {fave_food1} and {fave_food2}." ) # with an f string

#Not sure where my error is coming from on the f-string.


# -------------------------------------------------------------------

name = "Brandon"
print("Hello, ", name)
print("Hello " + name)

number = 24
print("Hello, ", number)
print("Hello " + str(number))

food_one = "lasagna"
food_two = "tacos"
print("I love to eat {} and {}".format(food_one, food_two))
print( f"I love to eat {food_one} and {food_two}." )