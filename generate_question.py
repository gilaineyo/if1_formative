import random # Generate random numbers

def generate_question():
    question_types = [ "division", "multiplication", "addition", "subtraction" ]
    q_type = question_types[random.randint(0, len(question_types) - 1)] # Chooses a random question type from the list

    match q_type:
        case "division":
            # Defining the multiplier rather than the value to be divided ensures the answer will be a valid integer
            number = random.randint(2,12)
            multiplier = random.randint(2,12)
            question = create_division(number, multiplier)
        case "multiplication":
            first = random.randint(2,12)
            second = random.randint(2,12)
            question = create_multiplication(first, second)
        case "addition":
            first = random.randint(2,50)
            second = random.randint(2,50)
            question = create_addition(first, second)
        case "subtraction":
            first = random.randint(2,50)
            second = random.randint(2,50)
            question = create_subtraction(first, second)
    return question

def create_division(number, multiplier):
    return {
        "answer": multiplier,
        "question_text": f"What is {number * multiplier} divided by {number}?\n"
    }

def create_multiplication(first, second):
    return {
        "answer": first * second,
        "question_text": f"What is {first} multiplied by {second}?\n"
    }

def create_addition(first, second):
    return {
        "answer": first + second,
        "question_text": f"What is {first} plus {second}?\n"
    }

def create_subtraction(first, second):
    return {
        "answer": second,
        "question_text": f"What is {first + second} minus {first}?\n"
    }
