"""
Panagram Module 
"""
NUM_LETTERS = 24
LOWER_CASE_A = ord('a')

def is_pangram(input_str):
    """
    Determins if the input string is a Pangram
    Given: string input_str
    Return: boolean
    """
    if not isinstance(input_str, str):
        raise ValueError("Input parameter requires string")
    if len(input_str)<NUM_LETTERS:
        return False
    
    input_str_lower =  input_str.lower()
    for i in range(NUM_LETTERS):
        if not chr(LOWER_CASE_A+i) in input_str_lower:
            return False
    return True

