#convert a string to a boolean value like "yes", "y", " " will be true otherwise false

def str_to_bool(val):
    true_vals = ["yes", "y", "true", "t", "1"]
    false_vals = ["no", "n", "false", "f", "0"]

    try:
        val = val.lower()
    except AttributeError:
        val = str(val).lower()
    if val in true_vals:
        return True
    elif val in false_vals:
        return False
    
def str_to_int(string):
    result = float(string)
    return int(result)

