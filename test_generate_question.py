import random
from generate_question import generate_question # Import the question generator and question type functions

def test_generate_division(monkeypatch):
    values = [3,5,30,50]
    monkeypatch.setattr(random, 'randint', lambda x, y: values.pop(0))
    result = generate_question("division") 
    assert isinstance(result["answer"], int)
    assert isinstance(result["question_text"], str)
    assert result["answer"] == 5
    assert result["question_text"] == f"What is 15 divided by 3?\n"

def test_generate_multiplication(monkeypatch):
    values = [3,5,30,50]
    monkeypatch.setattr(random, 'randint', lambda x, y: values.pop(0))
    result = generate_question("multiplication") 
    assert isinstance(result["answer"], int)
    assert isinstance(result["question_text"], str)
    assert result["answer"] == 15
    assert result["question_text"] == f"What is 3 multiplied by 5?\n"

def test_generate_addition(monkeypatch):
    values = [3,5,30,50]
    monkeypatch.setattr(random, 'randint', lambda x, y: values.pop(0))
    result = generate_question("addition") 
    assert isinstance(result["answer"], int)
    assert isinstance(result["question_text"], str)
    assert result["answer"] == 80
    assert result["question_text"] == f"What is 30 plus 50?\n"

def test_generate_subtraction(monkeypatch):
    values = [3,5,30,50]
    monkeypatch.setattr(random, 'randint', lambda x, y: values.pop(0))
    result = generate_question("subtraction") 
    assert isinstance(result["answer"], int)
    assert isinstance(result["question_text"], str)
    assert result["answer"] == 50
    assert result["question_text"] == f"What is 80 minus 30?\n"