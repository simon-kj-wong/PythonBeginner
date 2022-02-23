def cross(A, B):
    # Returns cross product for elements in A and elements in B
    return [a+b for a in A for b in B]


def stringToBoard(string):
    # Upon given a string, represent the board as a dictionary with keys
    # corresponding to crossproducts between 'ABCDEFGHI' and '123456789'
    # Rows represented as A1 A2 A3|A4 A5 A6|A7 A8 A9
    # Columns represented vertically as A1 B1 C1|D1 E1 F1|G1 H1 I1

    # Assumes that the string given is of length 9*9=81

    rows = "ABCDEFGHI"
    columns = "123456789"
    keys = cross(rows, columns)
    index = 0
    board = {}
    while index < 81:
        board[keys[index]] = string[index]
        index += 1
    print(board)

    return board
