# Question
# This class models a single quiz question: the text of the question,
# the list of possible choices shown to the user, and the correct answer.
# It has no logic for running a whole quiz -- that's Quiz's job below.
# Splitting responsibilities like this (one class per concept) is a core
# OOP idea: each class should represent one clear "thing".
class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    # A regular instance method: it takes "self" (the specific Question
    # object it was called on) plus whatever the caller passes in. It
    # compares the caller's guess against the answer stored on THIS
    # question and returns True/False.
    def check_answer(self, answer):
        return self.answer == answer

# Quiz
# Quiz is built OUT OF Question objects: this is called "composition" --
# instead of a Quiz inheriting from Question, a Quiz simply HAS a list of
# Question objects and coordinates them. Composition is often described
# as a "has-a" relationship, versus inheritance's "is-a" relationship.
class Quiz:
    def __init__(self, questions):
        # self.questions is a list of Question objects (see the bottom of
        # this file, where q1..q5 are built and collected into a list).
        self.questions = questions
        self.score = 0
        # question_index tracks which question we're currently on, as a
        # position into the self.questions list (0 = first question).
        self.question_index = 0

    # Returns the Question object the quiz is currently on, by indexing
    # into the list with the current question_index.
    def get_question(self):
        return self.questions[self.question_index]

    def display_question(self):
        question = self.get_question()
        # question_index is 0-based (0, 1, 2, ...) but that's awkward to
        # show a human, so +1 makes the very first question print as
        # "Question 1" instead of "Question 0".
        print(f'Question {self.question_index + 1}: {question.text}')

        # question.choices is a list of strings; looping over it prints
        # each one on its own line, prefixed with a dash to look like a
        # bullet list.
        for q in question.choices:
            print('-' + q)

        # input() pauses the program and waits for the user to type
        # something and press Enter; whatever they typed comes back as a
        # string.
        answer = input('answer: ')
        self.guess(answer)
        # After scoring this answer, immediately move on to loading the
        # next question (or ending the quiz). This creates a chain:
        # display_question -> guess -> load_question -> (display_question
        # again, or show_score) -- the quiz keeps driving itself forward
        # until load_question decides there are no questions left.
        self.load_question()

    def guess(self, answer):
        question = self.get_question()

        # check_answer() is the method defined on Question above; it
        # compares the stored correct answer to what the user typed.
        if question.check_answer(answer):
            self.score += 1
        # Move the pointer to the next question regardless of whether the
        # guess was right or wrong -- everyone gets exactly one attempt
        # per question here.
        self.question_index += 1

    def load_question(self):
        # Once question_index has been incremented past the last valid
        # index, its value equals len(self.questions) (there is no
        # question at that position any more), so the quiz is over.
        if len(self.questions) == self.question_index:
            self.show_score()
        else:
            self.display_progress()
            self.display_question()

    def show_score(self):
        print('score: ', self.score)

    def display_progress(self):
        total_questions = len(self.questions)
        question_number = self.question_index + 1

        # This branch is actually unreachable in normal use: load_question
        # already checks "question_index == len(questions)" and calls
        # show_score() instead of display_progress() in that case, so by
        # the time display_progress() runs, question_number can never
        # exceed total_questions. It's defensive code that would only
        # matter if display_progress() were called from somewhere else.
        if question_number > total_questions:
            print('Quiz finished.')
        else:
            # str.center(width, fillchar) returns a new string padded with
            # fillchar on both sides so the original text sits in the
            # middle of a string that is `width` characters wide. Here it
            # takes something like "Question 2 of 5" and pads it with '*'
            # characters until the whole line is 100 characters long,
            # producing a banner like "****...Question 2 of 5...****".
            print(f'Question {question_number} of {total_questions}'.center(100, '*'))

# Learned that a class can hold a list of other objects (here, Question objects) as its data.
# Five separate Question objects, each with its own text/choices/answer.
# Every one of them happens to have 'python' as the correct answer here.
q1 = Question('what is the best programming language?', ['C#', 'python', 'javascript', 'java'], 'python')
q2 = Question('what is the most popular programming language?', ['python', 'javascript', 'C#', 'java'], 'python')
q3 = Question('what is the highest paying programming language?', ['C#', 'javascript', 'java', 'python'], 'python')
q4 = Question('what is the most loved programming language?', ['C#', 'javascript', 'java', 'python'], 'python')
q5 = Question('what is the easiest programming language?', ['C#', 'javascript', 'java', 'python'], 'python')

# Collecting the five Question objects into a plain Python list -- this
# is the "questions" argument that Quiz's __init__ expects.
questions = [q1, q2, q3, q4, q5]

quiz = Quiz(questions)

# Kicks off the whole interactive quiz. Since question_index starts at 0
# and len(questions) is 5, the "quiz finished" check (0 == 5) is False,
# so this immediately shows progress and displays the first question,
# then the chain of methods described above keeps the quiz running until
# all 5 questions have been answered.
quiz.load_question()
