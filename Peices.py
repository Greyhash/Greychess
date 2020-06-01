import os
import sys

import Board

# 1 == pawn, 2 == knight, 3 == bishop, 4 == rook, 5 == queen, 6 == king

# Black
# 7 == pawn, 8 == knight....

def move(board, f, t):
    f_column = f[0]
    f_row    = f[1]

    t_column = t[0]
    t_row    = t[1]
    
  
    # if it is a white pawn in row 7 to row 8, then pawn gets promoted to queen
    if Board.get_peice(board, (f_column, f_row)) == 1 and f_row == 7 and t_row == 8:
           board[t_column, t_row] = 5
           board[f_column, f_row] = 0
        
     # if it is a black pawn in row 2 to row 1, then pawn gets promoted to queen
    if Board.get_peice(board, (f_column, f_row)) == 0 and f_row == 2 and t_row == 1:
           board[t_column, t_row] = 11
           board[f_column, f_row] = 0 
    else:
        board[t_column, t_row] = board[f_column, f_row]
        board[f_column, f_row] = 0
        

    
def is_valid_move(board, f, t, color):
    # if color == 0 or color == 1
    if not (color == 0 and color == 1):
        return False

    peice = Board.get_peice(board, f)
    current_color = Board.get_peice_color(board, f)

    to_position_color = Board.get_peice_color(board, t)
   

    if current_color == to_position_color:
        print ("Tried to move to a squared occupied by another of our peices")
        return False
    
    if peice == 1:
        if not pawn(f, t, 1, board):
            return False
        
    if peice == 7:
        if not pawn(f, t, 0, board):
            return False

    if peice == 2 or peice == 8:
        if not knight(f, t, board):
            return False

    if peice == 3 or peice == 9:
        if not bishop(f, t, board):
            return False

    if peice == 4 or peice == 10:
        if not rook(f, t, board):
            return False

    if peice == 5 or peice == 11:
        if not queen(f, t, board):
            return False

    if peice == 6 or peice == 12:
        if not king(f, t, board):
            return False

    return True

def bishop(f, t, board):
    f_column = f[0]
    f_row    = f[1]

    t_column = t[0]
    t_row    = t[1]

    current_color = Board.get_peice_color(board, f)
    
    if not abs(f_column - t_column) == abs(f_row - t_row):
        return False

    if f_column > t_column and f_row > t_row:
        for x in range(1, abs(f_column - f_column)):
            if Board.get_peice(board, (f_column-x, f_row-x)) > -1:
                return False
        
    elif f_column > t_column and f_row < t_row:
        for x in range(1, abs(f_column - f_column)):
            if Board.get_peice(board, (f_column-x, f_row+x)) > -1:
                return False

    elif f_column < t_column and f_row > t_row:
        for x in range(1, abs(f_column - f_column)):
            if Board.get_peice(board, (f_column+x, f_row-x)) > -1:
                return False

    elif f_column < t_column and f_row < t_row:
        for x in range(1, abs(f_column - f_column)):
            if Board.get_peice(board, (f_column+x, f_row+x)) > -1:
                return False

    return True

def rook(f, t, board):
    f_column = f[0]
    f_row    = f[1]

    t_column = t[0]
    t_row    = t[1]

    current_color = Board.get_peice_color(board, f)
    
    if (f_column == t_column and f_row != t_row) \
       or (f_column != t_column and f_row == t_row):
        return True


    if f_column > t_column and f_row == t_row:
        for x in range(1, abs(f_column - f_column)):
            if Board.get_peice(board, (f_column-x, f_row)) > -1:
                return False
        
    elif f_column < t_column and f_row == t_row:
        for x in range(1, abs(f_column - f_column)):
            if Board.get_peice(board, (f_column+x, f_row)) > -1:
                return False

    elif f_column == t_column and f_row > t_row:
        for x in range(1, abs(f_row - f_row)):
            if Board.get_peice(board, (f_column, f_row-x)) > -1:
                return False

    elif f_column == t_column and f_row < t_row:
        for x in range(1, abs(f_row - f_row)):
            if Board.get_peice(board, (f_column, f_row+x)) > -1:
                return False

    
    # FIX castling
    
    return False
    
def knight(f, t, board):
    f_column = f[0]
    f_row    = f[1]

    t_column = t[0]
    t_row    = t[1]

    if (abs(f_column - t_column) == 2 and abs(f_row - t_row) == 1 \
        or abs(f_column - t_column) == 1 and abs(f_row - t_row) == 2):
        return True

    return False

def queen(f, t, board):
    if bishop(f, t, board) or rook(f, t, board):
        return True

    return False

def king(f, t, board):
    f_column = f[0]
    f_row    = f[1]

    t_column = t[0]
    t_row    = t[1]

    if (abs(f_row - t_row) == 1 and abs(f_column - t_column) == 1) \
       or (abs(f_row - t_row) == 0 and abs(f_column - t_column) == 1) \
       or (abs(f_row - t_row) == 1 and abs(f_column - t_column) == 0):
        return True

    # FIX castling
    
    return False

def pawn(f, t, color, board):
    if color == 1:
        return pawn_white(f, t, board)

    # FIX promote to queen/knight/bishop
      
    return pawn_black(f, t, board)

def pawn_white(f, t, board):
    f_column = f[0]
    f_row    = f[1]

    t_column = t[0]
    t_row    = t[1]

    current_color = Board.get_peice_color(board, f)

    if f_row +2 == t_row and f_column == t_column and f_row == 2:

        if Board.get_peice_color(board, (f_column, f_row+1)) > -1:
            return False
        if Board.get_peice_color(board, (f_column, f_row+2)) > -1:
            return False
        
        return True

    if f_row +1 == t_row and f_column == t_column:
        if Board.get_peice_color(board, (f_column, f_row+1)) > -1:
            return False
        
        return True

    # When capturing other peices
    if f_row +1 == t_row and abs(f_column - t_column) == 1:
        if Board.get_peice_color(board, (t_column, t_row)) == 0:
            return True

    # TODO fix promotion
    if f_row == 7 and t_row == 8 and f_column == t_column:
        if Board.get_peice_color(board, (t_column, t_row)) > -1:
            return False

        return True

     
    # TODO fix an'passant
      
    return False
    
def pawn_black(f, t, board):
    f_column = f[0]
    f_row    = f[1]

    t_column = t[0]
    t_row    = t[1]

    # Move two steps
    if f_row -2 == t_row and f_column == t_column and f_row == 6:
        if Board.get_peice_color(board, (f_column, f_row-1)) > -1:
            return False
        if Board.get_peice_color(board, (f_column, f_row-2)) > -1:
            return False

        return True

    if f_row -1 == t_row and f_column == t_column:
        if Board.get_peice_color(board, (f_column, f_row-1)) > -1:
            return False

    # Capturing other peices
    if f_row -1 == t_row and abs(f_column - t_column) == 1:
        if Board.get_peice_color(board, (t_column, t_row)) == 1:
            return True

    if f_row == 2 and t_row == 1 and f_column == t_column \
        and Board.get_peice_color(board, t) == -1:
            board[t_column, t_row] = 11 
                


    return False

board = Board.setup_board()


Board.print_board(board)
print ()
if is_valid_move(board, (4,2), (4,4), 1):
    move(board, (4,2), (4,4))
  
if is_valid_move(board, (2,1), (3,3), 2):
    move(board, (2,1), (3,3))
    #pawn_promotion((4,7), (4,8), board)

Board.print_board(board)
#pawn_white((4,2), (4,4), board)


