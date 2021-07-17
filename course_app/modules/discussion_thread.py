from modules.question import Question


class DiscussionThread:
    questions: list
    answers: list

    def __init__(self, question: Question):
        self.questions = [question]
        self.answers = []

    def getDiscussion(self):
        return [self.questions, self.answers]

    def addQuestion(self, question: Question):
        self.questions.append(question)
        self.answers.append('Unanswered')

    def addAnswer(self, qNumber: int, answer: str):
        self.answers[qNumber - 1] = answer
