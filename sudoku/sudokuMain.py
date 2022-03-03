from sudokuGraphics import drawGrid, setBoard
from sudokuBoard import parseGrid, reduceBoard, checkBoard, searchBoard


grid = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'


# Need to ask if importing own sudoku or randomly generate one
def main():
    win = drawGrid()
    values = parseGrid(grid)
    # Primitive way to continually propagate board
    while values != reduceBoard(values):
        values = reduceBoard(values)
    """if not checkBoard(values):
        # If board isn't complete
        values = searchBoard(values)"""
    win = setBoard(values, win)
    print(win.getMouse())


if __name__ == '__main__':
    main()
