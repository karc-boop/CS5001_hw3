# chessboard.py
'''
Name: Jiawen Cai
Class: CS5001
This is the 1st file
for #2 Programming in HW3: Booleans, Decision Making & Repetition
'''

def check_valid_row(row):
    '''
    Check if a row identifier is valid for a standard chessboard.

    valid parathesis: Standard Row Identifier ('1' to '8' or 1 to 8)
    return: True if the row is valid, False otherwise
    return type: boolean value

    '''
    valid_rows = (1,2,3,4,5,6,7,8,\
                  '1','2','3','4','5','6','7','8')
    return row in valid_rows

def check_valid_column(column):
    '''
    Check if a column identifier is valid for a standard chessboard.

    valid parathesis: Standard Row Identifier ('a' to 'h' or 'A' to 'H')
    return: True if the column is valid, False otherwise
    return type: boolean value
    '''
    valid_columns = ('a','b','c','d','e','f','g','h',\
                     'A','B','C','D','E','F','G','H')
    return column in valid_columns

