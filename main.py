import random # Generate random numbers

from validate_inputs import is_positive_integer # Checks if a user input is a positive integer
from generate_question import generate_question # Generates a question of the selected type

# Enter a maximum number of questions below - the user can set their own number of questions up to this limit
max_questions = 10
question_types = [ "division", "multiplication", "addition", "subtraction" ]
score = 0

print("Welcome to your interactive maths quiz!")
name = input("Please enter your name: ")

number_of_questions = input(f"Hi, {name}! How many questions do you want to answer? Enter a number from 1 to {max_questions}: ")

if not is_positive_integer(number_of_questions) or int(number_of_questions) > max_questions:
    number_of_questions = input(f"Oops! That's not a valid number of questions, please enter a number from 1 to {max_questions}: ")

print(f"You'll be asked {number_of_questions} simple maths questions.\nEnter each answer and you will get your score at the end.\nGood luck {name}!")
input("Press enter to start...")

# Ask the user-defined number of questions, with each randomly generated from the four question types
for i in range(int(number_of_questions)):
    question_type = question_types[random.randint(0, len(question_types) - 1)] # Chooses a random question type from the list
    question = generate_question(question_type)

    while True:
        try:
            response = int(input(question["question_text"]))
        except ValueError:
            print("Please enter an integer as your answer!")
            continue
        else:
            break

    if int(response) == question["answer"]:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")

print(f"Well done {name}! Your score is {score} out of {number_of_questions}")