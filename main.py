# Python Containers
# Lists, Tuples & Dictionaries

# student = {
#     'name': 'Maria',
#     'course': 'SEI',
#     'current_week': 7,
# }

# name = student['name']
# print(name)
# student['name'] = 'Tina'

# # print(student.get('skills', 'No Skills'))
# print(student.get('skills', {
#     'HTML': 5,
#     'JAVASCRIPT': 4
# }))

# student['age'] = 21
# print(student)

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

# where_my_things_are = {
#     'car': 'in the garage',
#     'phone': 'in my pocket',
#     'money': 'in the bank'
# }

# for thing, location in where_my_things_are.items():
#     print( f" My {thing} is kept {location}")

#  LISTS (Like JavaScript arrays)
# colors = ['red', 'green', 'blue']
# colors[-1] = 'brown'
# colors.append('purple')
# colors.extend(['orange', 'black'])
# colors += ['white', 'yellow']
# colors.insert(1, 'pink')
# colors.pop(2)
# colors.remove('orange')
# print(colors)

# odds = [1, 3, 5]
# evens = [2, 4, 6]
# nums = odds + evens
# print(nums)

# colors = ['red', 'green', 'blue']
# for color in colors:
#   print(color)

# what if you need the index value? this is not best practice
# idx = 0
# for color in colors:
#   print( idx, color )
#   idx += 1

# for item in enumerate(colors):
#     print( item )

# This is considered best practice if you need access to the index of the iteration
# for idx, color in enumerate(colors):
#     print( idx, color )

# scores = [
#     {
#         # 'name': 'name of the player',
#         'name': 'Kaitlin',
#         'points': 25  # points the player scored
#     }
# ]

# scores.append({
#     'name': 'Jim', 
#     'points': '15'
#     })

# print(scores)

# for score in scores:
#     print( f"{score['name']} scored {score['points']} points." )

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# squares = []
# for n in nums:
#   squares.append(n * n)

# let's replace with this
# squares = [n * n for n in nums]
#     print(squares)
# even_squares = [n * n for n in nums if (n * n) % 2 == 0]
#     print(even_squares)

# colors = ('red', 'green', 'blue')
# print(colors)

# short_name = 'Alexandria'[3]
# short_name = 'Alexandria'[0:4]
# print(short_name)

# colors = ('red', 'green', 'blue')
# print( colors[:2])
# print( colors[1:])

chars = ['a', 'b', 'x', 'y', 'd']
chars[2:4] = 'c'
print(chars)
