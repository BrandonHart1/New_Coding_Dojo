import random # to import random number(not auto in python)

def roll_dice(number_dice, number_sides, bonus):
    output = 0
    
    for i in range(0, number_dice):
        output += random.randint(1, number_sides)


    return output + bonus

def generate_classic_character():

    character = {}
    stats = ["STR", "CON", "DEX", "INT", "WIS", "CHA"]


    character[stats["STR"]] = roll_dice(3, 6)
    character[stats["CON"]] = roll_dice(3, 6)
    character[stats["DEX"]] = roll_dice(3, 6)
    character[stats["INT"]] = roll_dice(3, 6)
    character[stats["WIS"]] = roll_dice(3, 6)
    character[stats["CHA"]] = roll_dice(3, 6)

    return character



# -------------------------------------------------

# writing a for loop in Python
# x = [1, 6, 8, 19, -21, 7, 18, 5]

# for i in range(0, len(x)):
#     print(x[i])


# Python programmers write it like this
# for i in x:
#     print(i)