import random


# Create a board object to represent the minesweeper game
# This is so that we can interact with the object directly
class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # Create the board using a helper function
        self.board = self.make_new_board()
        self.assign_values()

        # Create a set that keeps track of what locations have been uncovered
        self.dug = set()

    def make_new_board(self):
        # Construct a new board based on dimension size and number of bombs
        # Create a list of lists to represent squares

        board = [[None for _ in range(self.dim_size)]
                 for _ in range(self.dim_size)]

        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            randx = random.randint(0, self.dim_size - 1)
            randy = random.randint(0, self.dim_size - 1)

            if board[randx][randy] == '*':
                # A bomb already exists here
                continue
            board[randx][randy] = '*'
            bombs_planted += 1

        return board

    def assign_values(self):
        # Assigns values to board to indicate how many neighbouring bombs
        # to a square
        for r in range(0, self.dim_size):
            for c in range(0, self.dim_size):
                if self.board[r][c] == '*':
                    # We have a bomb
                    continue
                self.board[r][c] = self.find_neighbouring_bombs(r, c)

    def find_neighbouring_bombs(self, row, col):
        num_neighbouring_bombs = 0
        for r in range(max(0, row - 1), min(self.dim_size, (row + 1) + 1)):
            for c in range(max(0, col - 1), min(self.dim_size, (col + 1) + 1)):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_neighbouring_bombs += 1

        self.board[row][col] = num_neighbouring_bombs
        return num_neighbouring_bombs

    def dig(self, row, col):
        # Returns False if a bomb is dug up
        # Returns True if we dig a coordinate with neighbouring bombs

        # Add the coordinate of where we dug to the set
        self.dug.add((row, col))

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        # Recursively dig until we find a square with neighbouring bombs
        for r in range(max(0, row - 1), min(self.dim_size, (row + 1) + 1)):
            for c in range(max(0, col - 1), min(self.dim_size, (col + 1) + 1)):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)

        return True

    def __str__(self):
        # Used to print out the board
        boardstring = ""

        # First line of grid
        line = " "
        index = 0
        while index < self.dim_size:
            line += (" " + str(index))
            index += 1
        line += '\n'
        boardstring += line

        # Second line of grid
        boardstring += len(boardstring) * '_' + '\n'

        for i in range(self.dim_size):
            line = str(i)
            for j in range(self.dim_size):
                if (i, j) in self.dug:
                    line += '|' + str(self.board[i][j])
                else:
                    line += '| '
            boardstring += line + '\n'
        return boardstring

    def check(self):
        if len(self.dug) == self.dim_size**2 - self.num_bombs:
            return True
        else:
            return False


# play the game
def play(dim_size=10, num_bombs=10):
    # Step 1: create the board and plant the bombs
    board = Board(dim_size, num_bombs)

    # Step 2: show the user the board and ask where they want to dig
    # Step 3a: if location is a bomb, show game over message
    # Step 3b: if location is not a bomb dig recusively until each square is
    #          at least next to a bomb
    # Step 4: repeat steps 2 and 3 until there are no more places to dig
    while board.check() is False:
        print(board)
        entry = input('Enter coordinate that wants to be dug (row, column): ')
        r = int(entry[0])
        c = int(entry[2])
        if (r, c) in board.dug:
            print('Enter coordinates that haven\'t been dug up')
            continue
        elif board.dig(r, c) is False:
            return print("You dug up a bomb!!!")
    print("You won!!!")


if __name__ == '__main__':
    play()
