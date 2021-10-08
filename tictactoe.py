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
    num_x = 0
    num_o = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == O:
                num_o += 1
            elif board[i][j] == X:
                num_x += 1

    if num_x == num_o:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                available_actions.add((i,j))
    return available_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise Exception("Invalid action.")

    p = player(board)
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = p
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check diagonally
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    
    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] is not None:
        return board[2][0]

    # Check horizontally
    for i in range(3):
        player = board[i][i]
        if player is not None:
            win = 0
            for j in range(3):
                if board[i][j] == player:
                    win += 1
            if win == 3:
                return player
    
    return None

    # Check vertically
    for j in range(3):
        player = board[i][i]
        win = 0
        for i in range(3):
            if board[i][j] == player:
                win += 1
        if win == 3:
            return player

    # No winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # There is a winner
    if winner(board) is not None:
        return True
    
    # Check whether the board is filled
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    available_actions = actions(board)

    p = player(board)
    if p == O:
        best_result = 2
    else:
        best_result = -2

    for a in available_actions:
        new_board = result(board, a)

        m_a = minimax(new_board)
        print(m_a)

        if m_a is not None:
            new_board = result(new_board, m_a)

        r = utility(new_board)
        if p == O and r < best_result:
            best_result = r
            best_action = a
        elif p == X and r > best_result:
            best_result = r
            best_action = a 

    return best_action

