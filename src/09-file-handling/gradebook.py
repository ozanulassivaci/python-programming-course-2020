# This program reads/writes student grade data stored as plain text in
# exam_grades.txt, where each line looks like:
#   kerem deniz:90,70,60
# i.e. "name:grade1,grade2,grade3" followed by a newline.

# Converts one raw line from exam_grades.txt (like "kerem deniz:90,70,60\n")
# into a formatted result line (like "kerem deniz: CC\n").
def calculate_grade(line):
    # line[:-1] is a "slice": it takes every character of the string
    # EXCEPT the last one, which chops off the trailing "\n" newline
    # character that each line read from a file normally carries.
    line = line[:-1]
    # str.split(':') breaks the string into a list wherever ':' appears.
    # "kerem deniz:90,70,60" becomes ["kerem deniz", "90,70,60"].
    parts = line.split(':')

    student_name = parts[0]
    # parts[1] is the "90,70,60" part; splitting that by ',' gives
    # ["90", "70", "60"] -- the three grades, still as strings.
    grades = parts[1].split(',')

    # int() converts each grade string into an actual whole number so we
    # can do arithmetic with it (you can't average strings).
    grade1 = int(grades[0])
    grade2 = int(grades[1])
    grade3 = int(grades[2])

    average = (grade1 + grade2 + grade3) / 3

    # Learned that chained range checks like this are basically a manual
    # switch statement for turning a number into a letter grade.
    # Each elif checks a lower and lower band of scores, in descending
    # order, converting a numeric average into a Turkish-style letter
    # grade. Because these are elif (not separate independent if
    # statements), only ONE branch runs -- as soon as a matching range is
    # found, the rest are skipped.
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

    # Building the result string back up with + (string concatenation).
    # For "kerem deniz:90,70,60", average = (90+70+60)/3 = 220/3 = 73.33,
    # which falls in the 70-74 band, giving letter "CC" -- matching what
    # results.txt shows for this student.
    return student_name + ": " + letter + "\n"


# Opens exam_grades.txt for reading and prints every student's computed
# letter grade to the screen, one at a time.
def read_grades():
    # "with ... as file:" is a context manager -- it guarantees the file
    # gets closed automatically once the indented block finishes, even
    # if an error happens partway through. "r" mode requires the file to
    # already exist, and only allows reading, not writing.
    with open("exam_grades.txt", "r", encoding="utf-8") as file:
        # Looping directly over a file object yields it one line at a
        # time, in order, until the end of the file.
        for line in file:
            print(calculate_grade(line))


# Prompts the user for a new student's name and three grades, then
# appends a new correctly-formatted line to exam_grades.txt.
def enter_grade():
    name = input('Student first name: ')
    surname = input('Student last name: ')
    grade1 = input('grade 1: ')
    grade2 = input('grade 2: ')
    grade3 = input('grade 3: ')

    # "a" (append) mode adds new content at the END of the file without
    # touching anything already there -- unlike "w", which would erase
    # the whole file first. This builds a line in exactly the same
    # "name:grade1,grade2,grade3\n" format that calculate_grade() expects
    # to parse later.
    with open("exam_grades.txt", "a", encoding="utf-8") as file:
        file.write(name + ' ' + surname + ':' + grade1 + ',' + grade2 + ',' + grade3 + '\n')


# Reads every line from exam_grades.txt, computes each student's letter
# grade, and writes ALL of those results out to a separate file,
# results.txt.
def save_results():
    with open('exam_grades.txt', "r", encoding="utf-8") as file:
        results = []

        for line in file:
            # Building up a list of formatted result strings in memory
            # first, rather than writing straight to results.txt line by
            # line, so that all reading finishes before any writing
            # starts.
            results.append(calculate_grade(line))

        # A "with" block can be nested inside another "with" block: this
        # opens a SECOND file (results.txt) for writing while the first
        # file is still open for reading. "w" mode here means each time
        # save_results() runs, results.txt is fully overwritten with a
        # fresh set of results rather than growing indefinitely.
        with open("results.txt", "w", encoding="utf-8") as file2:
            for line in results:
                file2.write(line)

# A simple text menu loop: keep showing the options and running whatever
# the user picks, until they choose something other than '1', '2', or
# '3' (the `else: break` branch), which exits the while loop and ends
# the program.
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
