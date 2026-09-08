class Class:
    def __init__(self, id,name,teacherid):
        # A brand-new Class that hasn't been saved to the database yet has
        # no real id (the database itself assigns one, e.g. via
        # AUTO_INCREMENT, when the row is inserted). So we allow the caller
        # to pass id=None and store 0 as a placeholder until the row exists
        # and has a real id.
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.name = name
        self.teacherid = teacherid

    @staticmethod
    def CreateClass(obj):
        # This converts raw database rows into Class objects. `obj` is
        # expected to be an iterable of tuples coming straight from a
        # cursor.fetchall() call (e.g. from "select * from class"), where
        # each tuple's values are in column order: (id, name, teacherid).
        # Turning them into Class objects lets the rest of the program work
        # with named attributes like c.name instead of raw tuple indexes
        # like c[1].
        list = []

        for i in obj:
            list.append(Class(i[0],i[1],i[2]))

        return list
