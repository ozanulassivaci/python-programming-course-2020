class Teacher:
    def __init__(self, id,branch,name,surname,birthdate,gender,classid):
        # A Teacher not yet saved to the database has no real id, so we let
        # the caller pass id=None and fall back to 0 as a placeholder value
        # until a real id is assigned by the database on insert.
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.branch = branch
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        # Note: __init__ takes a `classid` parameter, but it's never stored
        # onto self here (there's no self.classid = classid line), so that
        # value is silently discarded whenever a Teacher is constructed.
        # This class also has no CreateTeacher()-style helper the way Class
        # and Student do (see dbmanager.py's editTeacher(), which is left
        # as an unimplemented `pass`), suggesting Teacher support in this
        # app was left unfinished.
