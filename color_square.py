# color_square.py
'''
Name: Jiawen Cai
Class: CS5001
This is the 3nd file
for #2 Programming in HW3: Booleans, Decision Making & Repetition
'''

#Create a list working as criteria to discuss different situation
aceg_list = ['a','c','e','g','A','C','E','G']

def black_or_white(row, column):
    '''
    Determine if a chessboard square is black or white.

    param row: Row identifier ('1' to '8' or 1 to 8)
    param column: Column identifier ('a' to 'h' or 'A' to 'H')
    return: 'BLACK' if the square is black, 'WHITE' if it's white
    return type: string

    '''
    row = int(row)
    if row % 2 != 0:
        if column in aceg_list:
            return "BLACK"
        else:
            return "WHITE"
    elif row % 2 == 0:
        if column in aceg_list:
            return "WHITE"
        else:
            return "BLACK"

