from sudokuGraphics import drawGrid, setBoard
from sudokuBoard import parseGrid, reduceBoard, propagateBoard


grid = '0030206009003050010018064000081029007' \
        '00000008006708200002609500800203009005010300'


# Need to ask if importing own sudoku or randomly generate one
def main():
    win = drawGrid()
    values = parseGrid(grid)
    # Primitive way to continually propagate board
    while values != propagateBoard(values):
        values = propagateBoard(values)
    win = setBoard(values, win)
    print(win.getMouse())


if __name__ == '__main__':
    main()
