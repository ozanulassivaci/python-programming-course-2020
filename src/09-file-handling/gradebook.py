def calculate_grade(line):
    line = line[:-1]
    parts = line.split(':')

    student_name = parts[0]
    grades = parts[1].split(',')

    grade1 = int(grades[0])
    grade2 = int(grades[1])
    grade3 = int(grades[2])

    average = (grade1 + grade2 + grade3) / 3

    # Learned that chained range checks like this are basically a manual
    # switch statement for turning a number into a letter grade.
    if average >= 90 and average <= 100:
        letter = "AA"
    elif average >= 85 and average <= 89:
        letter = "BA"
    elif average >= 80 and average <= 84:
        letter = "BB"
    elif average >= 75 and average <= 79:
        letter = "CB"
    elif average >= 70 and average <= 74:
        letter = "CC"
    elif average >= 65 and average <= 69:
        letter = "DC"
    elif average >= 60 and average <= 64:
        letter = "DD"
    elif average >= 50 and average <= 59:
        letter = "FD"
    else:
        letter = "FF"

    return student_name + ": " + letter + "\n"


def read_grades():
    with open("exam_grades.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(calculate_grade(line))


def enter_grade():
    name = input('Student first name: ')
    surname = input('Student last name: ')
    grade1 = input('grade 1: ')
    grade2 = input('grade 2: ')
    grade3 = input('grade 3: ')

    with open("exam_grades.txt", "a", encoding="utf-8") as file:
        file.write(name + ' ' + surname + ':' + grade1 + ',' + grade2 + ',' + grade3 + '\n')


def save_results():
    with open('exam_grades.txt', "r", encoding="utf-8") as file:
        results = []

        for line in file:
            results.append(calculate_grade(line))

        with open("results.txt", "w", encoding="utf-8") as file2:
            for line in results:
                file2.write(line)

while True:
    choice = input('1- Read Grades\n2- Enter Grade\n3- Save Results\n4- Exit\n')

    if choice == '1':
        read_grades()
    elif choice == '2':
        enter_grade()
    elif choice == '3':
        save_results()
    else:
        break
