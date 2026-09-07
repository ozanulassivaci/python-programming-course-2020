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

students = {}

student_id = input("student id: ")
first_name = input("student first name: ")
last_name = input("student last name: ")
phone = input("student phone: ")

# students[student_id] = {
#     'first_name': first_name,
#     'last_name': last_name,
#     'phone': phone
# }

# Learned that dict.update() can insert a new key or overwrite an
# existing one in a single call.
students.update({
    student_id: {
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone
    }
})

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

print('*'*50)

search_id = input('student id: ')
student = students[search_id]
print(student)

print(f"Student {search_id}: name {student['first_name']} {student['last_name']}, phone {student['phone']}")
