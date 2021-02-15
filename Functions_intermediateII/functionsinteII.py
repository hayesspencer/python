x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
# print(x)
# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
# print(students)
# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
# print(sports_directory)
# Change the value 20 in z to 30
z[0]['y'] = 30
# print(z)


def iterateDictionary(some_list):
    for idx in range(len(some_list)):
        student_dict = some_list[idx]
        for key in student_dict:
            print(key, '-', student_dict[key])


students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
# iterateDictionary(students)


def iterateDictionary2(key_name, some_list):
    for idx in range(len(some_list)):
        print(some_list[idx][key_name])

# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)
# users = [
#     {'name':'Todd', 'location':'Spokane'},
#     {'name':'John', 'location':'Seattle'},
#     {'name':'Jane', 'location':'Chicago'}
# ]
# iterateDictionary2('location', users)


def printInfo(some_dict):
    for key in some_dict:
        print(len(some_dict[key]), key.upper())
        for val in some_dict[key]:
            print(val)


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)

# 7 LOCATIONS
# LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
