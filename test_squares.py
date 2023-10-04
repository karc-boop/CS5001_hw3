# test_squares.py
'''
Name: Jiawen Cai
Class: CS5001
This is the 3rd file
for #2 Programming in HW3: Booleans, Decision Making & Repetition
'''

import doctest
from chessboard import check_valid_row, check_valid_column
from color_square import black_or_white

def run_tests():
    
    #Test cases for check_valid_row()
    test_cases_check_valid_row = [
        ('1', True),
        ('h', False),
        ('A', True),
        (5, True),
        ('9', False),
        (123, False)  
    ]

    # Test cases for check_valid_column()
    test_cases_check_valid_col = [
        ('a', True),
        ('h', True),
        ('A', True),
        ('z', False),
        (0, False),
        (999, False)  
    ]

    # Test cases for black_or_white()
    test_cases_black_or_white = [
        ((8, 'G'), 'WHITE'),
        (('1', 'a'), 'BLACK'),
        (('4', 'G'), 'WHITE'),
        (('7', 'c'), 'BLACK')
    ]

    for input_val, expected_result in test_cases_check_valid_row:
        result = check_valid_row(input_val)
        print(f"Row you enter: {input_val}, Expected: {expected_result}, Got: {result}")

    for input_val, expected_result in test_cases_check_valid_col:
        result = check_valid_column(input_val)
        print(f"Column you enter: {input_val}, Expected: {expected_result}, Got: {result}")

    for input_val, expected_result in test_cases_black_or_white:
        result = black_or_white(*input_val)
        print(f"Position you enter: {input_val}, Expected: {expected_result}, Got: {result}")

    # Run the doctests
    results = doctest.testmod(verbose=True)

    if results.failed == 0:
        print("All doctests passed successfully.")
    else:
        print(f"{results.failed} doctest(s) failed out of {results.attempted} attempted.")

run_tests()