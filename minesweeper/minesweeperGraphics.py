from graphics import GraphWin, Rectangle, Point, Line, Text


def drawGrid(board):
    # Set the window size and coordinates
    win = GraphWin(width=1000, height=1000)
    win.setCoords(0, board.dim_size+1, board.dim_size+1, 0)

    # Draw the coordinate lines
    line = Line(Point(1, 0), Point(1, board.dim_size+1))
    line.draw(win)
    line = Line(Point(0, 1), Point(board.dim_size + 1, 1))
    line.draw(win)

    # Draw the vertical lines and the horizontal lines
    for i in range(2, board.dim_size + 1):
        line = Line(Point(i, 1), Point(i, board.dim_size + 1))
        line.setOutline('grey')
        line.draw(win)

        line = Line(Point(1, i), Point(board.dim_size + 1, i))
        line.setOutline('grey')
        line.draw(win)

    # Entering entries of coordinates that have been dug
    for i in range(board.dim_size):
        number = Text(Point(i + 1.5, 0.5), i)
        number.draw(win)

        number = Text(Point(0.5, i + 1.5), i)
        number.draw(win)

        for j in range(board.dim_size):
            if (i, j) in board.dug:
                number = Text(Point(j + 1.5, i + 1.5), str(board.board[i][j]))
                number.draw(win)

    return win
