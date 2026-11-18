"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = 0
    count_o = 0

    for row in board:
        for cell in row:
            if cell == X:
                count_x += 1
            elif cell == O:
                count_o += 1

    if count_x == count_o:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i , j = action

    if i > len(board[0]) or j > len(board[0]):

        raise Exception 

    if board[i][j] != EMPTY  :

        raise Exception
    
    deepcopy_board = copy.deepcopy(board)

    symbol = player(deepcopy_board)

    deepcopy_board[i][j] = symbol 

    return deepcopy_board



    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check if we have a winner in each row 
    for row in board :
        if row[0] == row[1] == row[2] and row[0] is not EMPTY :

            return row[0]
        
    # Check if we have a winner in each column 

    for j in range(3):

        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not EMPTY :

            return board[0][j]

    # Check if we have a winner in the diagonals
    # board[0][0] == board[1][1] == board[2][2]
    # board[0][2] == board[1][1] == board[2][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY :

        return board[0][2]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY :

        return board[0][0]

    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    return not actions(board)   # no empty cells left = tie


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    check = winner(board)

    if check == X :
        return 1
    elif check == O :
        return -1
    else :
        return 0
    
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    def value(b):
        """Score of board b if both players play perfectly."""
        if terminal(b):
            return utility(b)
        scores = [value(result(b, a)) for a in actions(b)]
        return max(scores) if player(b) == X else min(scores)

    turn = player(board)
    best_action = None
    best_score = -math.inf if turn == X else math.inf

    for action in actions(board):
        score = value(result(board, action))
        if turn == X and score > best_score:
            best_score, best_action = score, action
        elif turn == O and score < best_score:
            best_score, best_action = score, action

    return best_action
