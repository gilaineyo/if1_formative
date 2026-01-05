from generate_question import generate_question, create_division, create_multiplication, create_addition, create_subtraction # Import the question generator and question type functions

def test_create_division():
    result = create_division(3, 5) 
    assert isinstance(result["answer"], int)
    assert isinstance(result["question_text"], str)
    assert result["answer"] == 5
    assert result["question_text"] == f"What is 15 divided by 3?\n"

def test_create_multiplication():
    result = create_multiplication(3,5)
    assert isinstance(result["answer"], int)
    assert isinstance(result["question_text"], str)
    assert result["answer"] == 15
    assert result["question_text"] == f"What is 3 multiplied by 5?\n"

def test_create_addition():
    result = create_addition(3,5)
    assert isinstance(result["answer"], int)
    assert isinstance(result["question_text"], str)
    assert result["answer"] == 8
    assert result["question_text"] == f"What is 3 plus 5?\n"

def test_create_subtraction():
    result = create_subtraction(3,5)
    assert isinstance(result["answer"], int)
    assert isinstance(result["question_text"], str)
    assert result["answer"] == 5
    assert result["question_text"] == f"What is 8 minus 3?\n"