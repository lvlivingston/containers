# Python Containers
# Lists, Tuples & Dictionaries

student = {
    'name': 'Maria',
    'course': 'SEI',
    'current_week': 7,
}

name = student['name']
# print(name)
student['name'] = 'Tina'

# # print(student.get('skills', 'No Skills'))
# print(student.get('skills', {
#     'HTML': 5,
#     'JAVASCRIPT': 4
# }))

student['age'] = 21
print(student)

# del student['course']

# if 'course' in student:
#   print( f"{student['name']} is enrolled in {student['course']}")
# else:
#   print( f"{student['name']} is not enrolled in a course")

# len(student)
# len({})

#  not the best practice because it's an anti-pattern
# for tuna in student:
#     print(f"{tuna} = {student[tuna]}")

# this is a baby step towards where we want to go
# for item_tuple in student.items():
#     # print( item_tuple )
#     print( f"key = {item_tuple[0]} / value = {item_tuple[1]}" )

# Best practice "unpack" the tuples just like destructuring assignment in JavaScript
# for key, value in student.items():
#     print( f"key = {key} / value = {value}" )

where_my_things_are = {
    'car': 'in the garage',
    'cell phone': 'by my side at all times'
}

for thing, location in where_my_things_are.items():
    print( f" My {thing} is kept {location}")