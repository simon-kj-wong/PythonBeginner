from sudokuGraphics import drawGrid, addNumber
from graphics import Point
from sudokuBoard import stringToBoard


# Need to ask if importing own sudoku or randomly generate one
def main():
    """board = input("Enter board state as a string")"""
    win = drawGrid()
    stringToBoard("123456789123456789123456789123456789123456789123456789123456789123456789123456789")
    win.getMouse()


if __name__ == '__main__':
    main()
