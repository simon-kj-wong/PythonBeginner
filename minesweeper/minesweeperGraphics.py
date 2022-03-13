from graphics import GraphWin, Rectangle, Point, Line, Text


def drawGrid(dim_size, dug):
    # Set the window size and coordinates
    win = GraphWin(width=600, height=600)
    win.setCoords(0, dim_size+1, dim_size+1, 0)

    # Draw the coordinate lines
    line = Line(Point(1, 0), Point(1, dim_size+1))
    line.draw(win)
    line = Line(Point(0, 1), Point(dim_size + 1, 1))
    line.draw(win)

    # Draw the vertical lines and the horizontal lines
    for i in range(2, dim_size + 1):
        line = Line(Point(i, 1), Point(i, dim_size + 1))
        line.setOutline('grey')
        line.draw(win)

        line = Line(Point(1, i), Point(dim_size + 1, i))
        line.setOutline('grey')
        line.draw(win)

    return win
