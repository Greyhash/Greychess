import os
import sys
import numpy as np

def setup_board():
    board = np.zeros((9,9), dtype=int)
    
    # Add whites peices 
    board[:, 2] = 1
    board[1, 1] = 4
    board[2, 1] = 2
    board[3, 1] = 3
    board[4, 1] = 5
    board[5, 1] = 6
    board[6, 1] = 3
    board[7, 1] = 2
    board[8, 1] = 4

    # Blacks pecies
    """
    board[:, 7] = 7
    board[1, 8] = 10
    board[2, 8] = 8
    board[3, 8] = 9
    board[4, 8] = 11
    board[5, 8] = 12
    board[6, 8] = 9
    board[7, 8] = 8
    board[8, 8] = 10
    """

    return board

def get_peice_color(board, p):
    column = p[0]
    row    = p[1]

    #print (p)
    
    if board[column, row] >= 7:
        return 0
    if board[column, row] > 0:
        return 1
    return -1

def get_peice(board, p):
    column = p[0]
    row    = p[1]

    return board[column, row]

def print_board(board):
    for index in range(len(board)-1, 0, -1):
        print (board[1:, index])

