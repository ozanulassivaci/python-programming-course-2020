class Lesson:
    def __init__(self, id,name):
        # A Lesson not yet saved to the database has no real id yet, so we
        # let the caller pass id=None and fall back to 0 as a placeholder
        # until the database assigns a real one on insert.
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.name = name
