# Import question lists from an external module
from questions import student_questions, parent_questions, teacher_questions

# Define a function to determine the user's role and ask relevant questions
def who_are_you():
    while True:
        try:
            # Prompt the user to choose their role and handle input exceptions
            question = int(input("Which group do you represent? Please enter a number:\n1) Student\n2) Parent\n3) Teacher\nYour answer: "))
        except:
            # Handle non-integer input gracefully
            print('Please enter a number')
            continue
        if question == 1:
            # If the user is a student, ask them the student-related questions
            for q in student_questions:
                answer = input(q + '\n')
        elif question == 2:
            # If the user is a parent, ask them the parent-related questions
            for q in parent_questions:
                answer = input(q + "\n")
        elif question == 3:
            # If the user is a teacher, ask them the teacher-related questions
            for q in teacher_questions:
                answer = input(q + "\n")
        else:
            # Handle invalid input
            print("Please enter the correct number (1/2/3).")
            continue
        break  # Exit the loop once the user has answered the questions


who_are_you()