def cross(A, B):
    # Returns cross product for elements in A and elements in B
    return [a+b for a in A for b in B]


rows = "ABCDEFGHI"
columns = "123456789"
digits = "123456789"

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


def parseGrid(string):
    # Upon given a string, represent the board as a dictionary with keys
    # A1, A2, ..., I8, I9
    # Values correspond to either possible values or set values
    # Used to solve the board

    index = 0
    values = {}
    assert len(string) == 81
    while index < 81:
        if string[index] in '0.':
            values[squares[index]] = '123456789'
        else:
            values[squares[index]] = string[index]
        index += 1
    return values


def propagateBoard(values):
    tempValues = values.copy()
    for s1, d1 in tempValues.items():
        if len(d1) == 1:
            # Only one value exists
            # Want to remove d1 from all other peers
            for peer in peers[s1]:
                tempValues[peer] = tempValues[peer].replace(d1, "")
        else:
            for d2 in d1:
                for unit in units[s1]:
                    dplaces = [s for s in unit if d2 in values[s]]
                    if len(dplaces) == 1:
                        tempValues[s1] = d2
                        for peer in unit:
                            tempValues[peer] = tempValues[peer].replace(d1, "")
    return tempValues
