def is_positive_integer(input):
    try:
        input_int = int(input)
        if input_int <= 0:
            return False
        else:
            return True 
    except:
        return False
    
