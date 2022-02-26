def cross(A, B):
    # Returns cross product for elements in A and elements in B
    return [a+b for a in A for b in B]


rows = "ABCDEFGHI"
columns = "123456789"

# squares represents all unique square coordinates
squares = cross(rows, columns)

# unitlist represents all rows, columns and 3x3 squares across the grid
unitlist = ([cross(rows, c) for c in columns] +
            [cross(r, columns) for r in rows] +
            [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI')
            for cs in ('123', '456', '789')])

# units is a dictionary with keys representing each of the 81 squares and
# values equal to the row, column and 3x3 square that the key is a part of
units = dict((s, [u for u in unitlist if s in u]) for s in squares)

# peers is a dictionary with keys representing each of the 81 squares and
# values equal to all other squares that it will be compared against
peers = dict((s, set(sum(units[s], [])) - set([s])) for s in squares)


def stringToBoard(string):
    # Upon given a string, represent the board as a dictionary with keys
    # corresponding to crossproducts between 'ABCDEFGHI' and '123456789'
    # Rows represented as A1 A2 A3|A4 A5 A6|A7 A8 A9
    # Columns represented vertically as A1 B1 C1|D1 E1 F1|G1 H1 I1

    # Assumes that the string given is of length 9*9=81

    index = 0
    board = {}
    while index < 81:
        if string[index] == '0':
            board[squares[index]] = '.'
        else:
            board[squares[index]] = string[index]
        index += 1
    return board
