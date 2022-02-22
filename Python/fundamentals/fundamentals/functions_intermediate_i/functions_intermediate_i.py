x = [[5, 2, 3], [10, 8, 9]]
students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
]
sports_directory = {
    "basketball": ["Kobe", "Jordan", "James", "Curry"],
    "soccer": ["Messi", "Ronaldo", "Rooney"],
}
z = [{"x": 10, "y": 20}]
#########################################################
# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].

# Out of range


#############################################################
x[1][0] = 15;
print(x)


#########################################################
# Change the last_name of the first student from 'Jordan' to 'Bryant'

students[0]["last_name"]="Bryant"
print(students)

#########################################################
# In the sports_directory, change 'Messi' to 'Andres'

sports_directory["soccer"] = ["Andres", "Ronaldo", "Rooney"]
print(sports_directory)

#########################################################
# Change the value 20 in z to 30

#Is this a trick question.  Couldn't find a more efficient way.

z = [{"x": 10, "y": 30}]
print(z)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

    def iterateDictionary2(students):
    for n in range(4):
        print("first_name " + students[n]["first_name"] + "last_name" + students[n]["last_name"])



# Where is the rest of my code?!?!?!?!?!?!?!?!?!?!?!?!?!?!


# iterateDictionary(students) 

# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


