num1 = 42 # variable declaration
num2 = 2.3 # variable declaration
boolean = True # boolean
string = 'Hello World' # string


pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # array/all strings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # array/strings and boolean
fruit = ('blueberry', 'strawberry', 'banana')
print(type(fruit))
print(pizza_toppings[1]) # access value
pizza_toppings.append('Mushrooms') # change value
print(person['name'])
person['name'] = 'George' # add value
person['eye_color'] = 'blue' # add value
print(fruit[2])

if num1 > 45: # conditional
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5: # length check - conditional
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): # for loop - start
    print(x)
for x in range(2,5): # for loop
    print(x)
for x in range(2,10,3): # for loop
    print(x)  
x = 0
while(x < 5): # while loop
    print(x) 
    x += 1

pizza_toppings.pop() # delete value
pizza_toppings.pop(1) # delete value

print(person)
person.pop('eye_color') # delete value
print(person)

for topping in pizza_toppings: # for loop
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10): # for loop
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3) 
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)