# Question
class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def check_answer(self, answer):
        return self.answer == answer

# Quiz
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.question_index = 0

    def get_question(self):
        return self.questions[self.question_index]

    def display_question(self):
        question = self.get_question()
        print(f'Question {self.question_index + 1}: {question.text}')

        for q in question.choices:
            print('-' + q)

        answer = input('answer: ')
        self.guess(answer)
        self.load_question()

    def guess(self, answer):
        question = self.get_question()

        if question.check_answer(answer):
            self.score += 1
        self.question_index += 1

    def load_question(self):
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

        if question_number > total_questions:
            print('Quiz finished.')
        else:
            print(f'Question {question_number} of {total_questions}'.center(100, '*'))

# Learned that a class can hold a list of other objects (here, Question objects) as its data.
q1 = Question('what is the best programming language?', ['C#', 'python', 'javascript', 'java'], 'python')
q2 = Question('what is the most popular programming language?', ['python', 'javascript', 'C#', 'java'], 'python')
q3 = Question('what is the highest paying programming language?', ['C#', 'javascript', 'java', 'python'], 'python')
q4 = Question('what is the most loved programming language?', ['C#', 'javascript', 'java', 'python'], 'python')
q5 = Question('what is the easiest programming language?', ['C#', 'javascript', 'java', 'python'], 'python')

questions = [q1, q2, q3, q4, q5]

quiz = Quiz(questions)

quiz.load_question()
