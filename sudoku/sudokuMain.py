from sudokuGraphics import drawGrid, setBoard
from sudokuBoard import stringToBoard


# Need to ask if importing own sudoku or randomly generate one
def main():
    win = drawGrid()
    board = stringToBoard("123456789" +
                          "123456789" +
                          "123456789" +
                          "123456789" +
                          "123456789" +
                          "123456789" +
                          "123456789" +
                          "123456789" +
                          "123456789")
    win = setBoard(board, win)
    print(win.getMouse())


if __name__ == '__main__':
    main()
