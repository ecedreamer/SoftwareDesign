
class Assignment:
    def __init__(self, title, given_by, given_to, deadline, question):
        self.title = title
        self.teacher = given_by
        self.batch = given_to
        self.deadline = deadline
        self.question = question

    def get_question(self):
        return self.question

ass1 = Assignment("fist assignment", "Dipak", "Batch 36", 5, "Write a new program")
ass2 = Assignment("secvond assignment", "Abhin", "Batch 36", 7, "Write another program")

ass1_question = ass1.get_question()
ass2_question = ass2.get_question()
print(ass1_question, ass2_question)