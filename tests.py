from tictactoe import winner, X, O, EMPTY, minimax


s = set()
s.add(X)
s.add(None)
assert len(s) == 2

assert X == winner([[X, X, X],
         [O, EMPTY, O],
         [EMPTY, EMPTY, EMPTY]])
assert X == winner([[X, O, X],
         [X, O, O],
         [X, EMPTY, EMPTY]])
assert X == winner([[X, O, X],
         [O, X, O],
         [X, EMPTY, O]])
assert X != winner([[None, None, None], [None, 'X', None], [None, None, 'O']])

assert minimax([[X, None, None], [None, 'X', None], [None, None, 'O']]) == (0, 1)
assert minimax([[X, None, None], [None, 'X', None], [None, None, 'O']]) == (0, 1)