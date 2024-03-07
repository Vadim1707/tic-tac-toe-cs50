"""
Tic Tac Toe Player
"""

import math

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
    count = 0
    for row in board:
        for element in row:
            if element == X:
                count += 1
            elif element == O:
                count -= 1

    if count == 0:
        return X
    return O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i, row in enumerate(board):
        for j, element in enumerate(row):
            if element is EMPTY:
                tup = (i, j)
                possible_actions.update([tup])

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = [[EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]]
    sign = X if player(board) == X else O
    for i, row in enumerate(board):
        for j, element in enumerate(row):
            new_board[i][j] = board[i][j]
            if (i, j) == action:
                new_board[i][j] = sign

    return new_board

# board = [[X,X,X], [O, EMPTY,O], [EMPTY, EMPTY, EMPTY]]
# print(result(board, (2, 1)))



def  winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # horizontals
    for row in board:
        res = set(row)
        symb = res.pop()
        if len(res) == 0 and symb != EMPTY:
            # print(1, symb)
            return symb

    # verticals
    for i in range(3):
        res = set()
        for row in board:
            res.add(row[i])
        symb = res.pop()
        if len(res) == 0 and symb != EMPTY:
            # print(2, symb)
            return symb

    # diagonals
    diag1, diag2 = set(), set()
    for i in range(3):
        diag1.add(board[i][i])
        diag2.add(board[i][2-i])
    symb = diag1.pop()
    if len(diag1) == 0 and symb != EMPTY:
        # print(3, symb)
        return symb
    symb = diag2.pop()
    if len(diag2) == 0 and symb != EMPTY:
        # print(4, symb)
        return symb

    # else no rows are complete

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # if there's a winner
    if winner(board):
        # print('Winner')
        return True

    # if board is full
    s = set()
    for row in board:
        s.update(row)
    if EMPTY not in s:
        # print('Full')
        return True

    # otherwise
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    _winner = winner(board)
    if _winner == X:
        return 1
    elif _winner == O:
        return -1
    else:
        return 0


def min_value(board):
    if terminal(board):
        return utility(board)
    v = 1000000
    for action in actions(board):
        #print(v, max_value(result(board, action)))
        v = min(v, max_value(result(board, action)))
    return v


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -1000000
    for action in actions(board):
        #print(v, min_value(result(board, action)))
        v = max(v, min_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        # print(board)
        # print('None')
        return None

    for action in actions(board):
        if player(board) == X:
            value = max_value(board)
            if min_value(result(board, action)) == value:
                # print(action)
                return action
        elif player(board) == O:
            value = min_value(board)
            if max_value(result(board, action)) == value:
                # print(action)
                return action


