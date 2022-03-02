from sudokuGraphics import drawGrid, setBoard
from sudokuBoard import parseGrid, propagateBoard


grid = '000000907000420180000705026100904000050000040000507009920108000034059000507000000'


# Need to ask if importing own sudoku or randomly generate one
def main():
    win = drawGrid()
    values = parseGrid(grid)
    # Primitive way to continually propagate board
    while values != propagateBoard(values):
        values = propagateBoard(values)
        print(values.items())
        print("***********")
    win = setBoard(values, win)
    print(win.getMouse())


if __name__ == '__main__':
    main()
