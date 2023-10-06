# Import question lists from an external module
from questions import student_questions, parent_questions, teacher_questions

# Define a function to determine the user's role and ask relevant questions
def who_are_you():
    while True:
        try:
            # Prompt the user to choose their role and handle input exceptions
            question = input("Which group do you represent? (to end the survey press 'q') Please enter a number:\n1) Student\n2) Parent\n3) Teacher\nYour answer: ")
            if question == 'q':
                break
            question = int(question)
        except:
            # Handle non-integer input gracefully
            print('Please enter a number')
            continue
        if question == 1:
            # If the user chose '1' (Student), call the 'answer_questions' function with student questions
            result = answer_questions(student_questions)
            print('Your score is, ' + str(result) + '\nThis is your satisfaction percentage, ' + str(convert_to_percentage(result)) + '%')
        elif question == 2:
            # If the user chose '2' (Parent), call the 'answer_questions' function with parent questions
            result = answer_questions(parent_questions)
            print('Your score is, ' + str(result) + '\nThis is your satisfaction percentage, ' + str(convert_to_percentage(result)) + '%')
        elif question == 3:
            # If the user chose '3' (Teacher), call the 'answer_questions' function with teacher questions
            result = answer_questions(teacher_questions)
            print('Your score is, ' + str(result) + '\nThis is your satisfaction percentage, ' + str(convert_to_percentage(result)) + '%')
        else:
            # Handle invalid input
            print("Please enter the correct number (1/2/3).")
            continue
        break  # Exit the loop once the user has answered the questions

    
# Function to ask and score questions
def answer_questions(questions):
    point = 0  # Initialize the total score
    for q in questions:  # Iterate through each question in the list
        while True:  # Start a loop to ensure the user provides a valid response
            print('Please enter your answer as a number between 1 and 5')
            try:
                answer = int(input(q + '\nAnswer: '))  # Get the user's answer and attempt to convert it to an integer
                if answer <= 0 or answer > 5:
                    print('[!!!] Please enter a number between 1 and 5.')
                    continue  # If the answer is not between 1 and 5, display an error message and restart the loop
                else:
                    point = point + answer  # Add the answer to the total score
                    break  # End the loop when a valid answer is obtained
            except:
                print('[!!!] Please enter a number.')  # Display an error message if the answer is not a number
    return point  # Return the total score


def convert_to_percentage(number):
    # Calculate the percentage value of the given number.
    # Since there are a total of 10 questions and a maximum of 5 points can be awarded,
    # the formula used here is: (number / 10) / 5 * 100
    percentage = int((number / 10) / 5 * 100)
    return percentage

convert_to_percentage(21)
# Call the main function to start the program
who_are_you()