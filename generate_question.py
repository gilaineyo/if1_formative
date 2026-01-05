import random # Generate random numbers

def generate_question(question_type):
    # Random numbers between 2 and 12 inclusive for division and multiplication
    first = random.randint(2,12) 
    second = random.randint(2,12)

    # Random numbers between 2 and 50 inclusive for addition and subtraction
    first_large = random.randint(2,50)
    second_large = random.randint(2,50)

    match question_type:
        case "division":
            return {
                "answer": second,
                "question_text": f"What is {first * second} divided by {first}?\n"
            }   
        case "multiplication":
            return {
                "answer": first * second,
                "question_text": f"What is {first} multiplied by {second}?\n"
            }
        case "addition":
            return {
                "answer": first_large + second_large,
                "question_text": f"What is {first_large} plus {second_large}?\n"
            }
        case "subtraction":
            return {
                "answer": second_large,
                "question_text": f"What is {first_large + second_large} minus {first_large}?\n"
            }