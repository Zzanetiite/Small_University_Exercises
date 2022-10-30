# To register the answers to the questions a class was made
# in a separate python file.
from Question import Question

# An array of questions
question_prompts = [
    "What colour are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What colour are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What colour are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]


def run_test(questions):
    '''
    function to keep track of user's answers
    :param questions: QA with correct answers
    :return: score
    '''
    # Keeping track of user's score
    score = 0
    # for every question in question array
    for question in questions:
        # ask user a question from array
        # and register their answer
        answer = input(question.prompt)
        # if answer is correct
        if answer == question.answer:
            # they gain a point
            score += 1
    # Tell the user what their result is
    print("You got " + str(score) + "/" + str(len(questions)) + " correct.")


run_test(questions)
# This function takes invalid inputs but
# takes them as answer is wrong
