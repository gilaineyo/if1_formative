from validate_inputs import is_positive_integer

def is_positive_integer_happy():
    assert is_positive_integer("2") == True
    assert is_positive_integer("27") == True

def test_validate_input_unhappy():
    assert is_positive_integer("not a num") == False
    assert is_positive_integer("-2") == False
    assert is_positive_integer("0") == False

