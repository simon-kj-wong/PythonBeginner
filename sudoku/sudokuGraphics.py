from graphics import GraphWin, Rectangle, Point, Line


def drawGrid():

    # Set the window size and coordinates
    win = GraphWin(width=600, height=600)
    win.setCoords(0, 0, 11, 11)

    # Draw the outer square
    square = Rectangle(Point(1, 1), Point(10, 10))
    square.draw(win)

    # Draw the broad lines
    # Vertical and then horizontal
    line = Line(Point(4, 1), Point(4, 10))
    line.draw(win)
    line = Line(Point(7, 1), Point(7, 10))
    line.draw(win)

    line = Line(Point(1, 4), Point(10, 4))
    line.draw(win)
    line = Line(Point(1, 7), Point(10, 7))
    line.draw(win)

    # Draw the faint lines
    # Vertical and then horizontal
    line = Line(Point(2, 1), Point(2, 10))
    line.setOutline('grey')
    line.draw(win)
    line = Line(Point(3, 1), Point(3, 10))
    line.setOutline('grey')
    line.draw(win)
    line = Line(Point(5, 1), Point(5, 10))
    line.setOutline('grey')
    line.draw(win)
    line = Line(Point(6, 1), Point(6, 10))
    line.setOutline('grey')
    line.draw(win)
    line = Line(Point(8, 1), Point(8, 10))
    line.setOutline('grey')
    line.draw(win)
    line = Line(Point(9, 1), Point(9, 10))
    line.setOutline('grey')
    line.draw(win)

    line = Line(Point(1, 2), Point(10, 2))
    line.setOutline('grey')
    line.draw(win)
    line = Line(Point(1, 3), Point(10, 3))
    line.setOutline('grey')
    line.draw(win)
    line = Line(Point(1, 5), Point(10, 5))
    line.setOutline('grey')
    line.draw(win)
    line = Line(Point(1, 6), Point(10, 6))
    line.setOutline('grey')
    line.draw(win)
    line = Line(Point(1, 8), Point(10, 8))
    line.setOutline('grey')
    line.draw(win)
    line = Line(Point(1, 9), Point(10, 9))
    line.setOutline('grey')
    line.draw(win)

    win.getMouse()
