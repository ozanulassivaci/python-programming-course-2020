class Student:
    def __init__(self, id,studentNumber,name,surname,birthdate,gender,classid):
        # A Student that hasn't been inserted into the database yet has no
        # real id (the database assigns that automatically). Passing
        # id=None here means "not saved yet", and we store 0 as a
        # placeholder until it's actually written to the table and gets a
        # real id back.
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.classid = classid

    @staticmethod
    def CreateStudent(obj):
        # Converts raw database results into Student objects, so the rest
        # of the app can use named attributes (student.name) instead of
        # tuple indexes (student[2]).
        list = []

        # cursor.fetchone() returns a single tuple (or None), while
        # cursor.fetchall() returns a list of tuples. This method has to
        # handle both shapes: if `obj` is one tuple (fetchone's result), we
        # wrap it in a single-item list; otherwise we assume it's an
        # iterable of tuples (fetchall's result) and build one Student per
        # tuple. Either way, each tuple's values are unpacked in the
        # table's column order: (id, studentNumber, name, surname,
        # birthdate, gender, classid).
        if isinstance(obj, tuple):
            list.append(Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6]))
        else:
            for i in obj:
                list.append(Student(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        return list
