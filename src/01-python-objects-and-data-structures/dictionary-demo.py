'''
    students = {
        '120': {
            'first_name': 'Ali',
            'last_name': 'Yilmaz',
            'phone': '532 000 00 01'
        },
        '125': {
            'first_name': 'Can',
            'last_name': 'Korkmaz',
            'phone': '532 000 00 02'
        },
        '128': {
            'first_name': 'Volkan',
            'last_name': 'Yukselen',
            'phone': '532 000 00 03'
        },
    }

    1- Store the students above in a dictionary using info entered by the user.

    2- Ask the user for a student id and show that student's info.
'''

# Start with an empty dictionary -- {} with nothing inside creates a dict
# with zero key-value pairs, ready to have entries added to it.
students = {}

# input() always returns a string, no matter what the user types, so these
# will all be text values even if the id "looks like" a number.
student_id = input("student id: ")
first_name = input("student first name: ")
last_name = input("student last name: ")
phone = input("student phone: ")

# This commented-out approach would work too: assigning directly to a new
# key (students[student_id] = {...}) creates that key if it's missing.
# students[student_id] = {
#     'first_name': first_name,
#     'last_name': last_name,
#     'phone': phone
# }

# Learned that dict.update() can insert a new key or overwrite an
# existing one in a single call.
# update() takes another dict and merges its key-value pairs into this
# one: any key that doesn't exist yet gets added, and any key that already
# exists gets its value replaced. Here we pass a dict with exactly one
# key -- the student_id -- so this call adds (or replaces) just that one
# student record.
students.update({
    student_id: {
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone
    }
})

# Same pattern repeated for a second student.
student_id = input("student id: ")
first_name = input("student first name: ")
last_name = input("student last name: ")
phone = input("student phone: ")

students.update({
    student_id: {
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone
    }
})

# ...and a third student.
student_id = input("student id: ")
first_name = input("student first name: ")
last_name = input("student last name: ")
phone = input("student phone: ")

students.update({
    student_id: {
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone
    }
})

# '*' * 50 repeats the single-character string '*' fifty times, producing
# a horizontal divider line -- a common trick for making console output
# easier to read.
print('*'*50)

search_id = input('student id: ')
# Looking a key up with square brackets, e.g. students[search_id], raises
# a KeyError and crashes the program if that key isn't present in the
# dict -- there's no built-in "not found" fallback with this syntax
# (dict.get(key) is the safer alternative when a missing key is expected).
student = students[search_id]
print(student)

# f-strings can index into a dict right inside the {} -- note the quotes
# around the key have to be a different style ("first_name") from the
# quotes wrapping the whole f-string ('...') so Python doesn't get
# confused about where the string literal ends.
print(f"Student {search_id}: name {student['first_name']} {student['last_name']}, phone {student['phone']}")
