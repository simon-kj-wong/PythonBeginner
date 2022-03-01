from sudokuGraphics import drawGrid, setBoard
from sudokuBoard import parseGrid, reduceBoard


grid = '0030206009003050010018064000081029007' \
        '00000008006708200002609500800203009005010300'


# Need to ask if importing own sudoku or randomly generate one
def main():
    win = drawGrid()
    values = parseGrid(grid)
    values = reduceBoard(values)
    win = setBoard(values, win)
    values['A1'] = values['A1'].replace('1', "")
    print(win.getMouse())


if __name__ == '__main__':
    main()
