def main():
    board = board_init()
    board_incomplete = True
    # Repeats the cycle of checking every space on the board until either
    # the board is complete or no further progress can be made
    while board_incomplete:
        board_incomplete = solve_board(board)
    print_board(board)


# Launches a prompt to input a sudoku board
def board_init():
    board = []
    print("Please type each row of the sudoku board, with '0' in place of unknown numbers.")
    for row in range(1, 10):
        column = 1
        while True:
            print("Row ", row, ": ", sep="", end="")
            usr_input = input()
            if not usr_input.isdigit():
                print("Invalid row! Row must contain only numbers.")
            elif len(usr_input) != 9:
                print("Invalid row! Row must contain exactly 9 numbers.")
            else:
                break
        # Takes each inputted character in the row and records its positional data
        for num in usr_input:
            square = square_identifier(row, column)
            board.append([num, row, column, square])
            column += 1
    return board


# Identifies the 3x3 square a given value is in
def square_identifier(row, column):
    if column <= 3:
        if row <= 3:
            square = 1
        elif (row >= 4) and (row <= 6):
            square = 4
        else:
            square = 7
    elif (column >= 4) and (column <= 6):
        if row <= 3:
            square = 2
        elif (row >= 4) and (row <= 6):
            square = 5
        else:
            square = 8
    else:
        if row <= 3:
            square = 3
        elif (row >= 4) and (row <= 6):
            square = 6
        else:
            square = 9
    return square


# Checks every tile to see if it is filled in, and if not, attempts to fill it in
def solve_board(board):
    solved_tiles = 0
    for tile in board:
        if tile[0] == "0":
            solved_tile = solve_tile(tile, board)
            if solved_tile != "0":
                tile[0] = solved_tile
                solved_tiles += 1
    if solved_tiles > 0:
        return True
    else:
        return False


# Checks to see if there a single possible solution to a tile, and if so, fills it in
def solve_tile(tile, board):
    possible_values = []
    for value in range(1, 10):
        digit_possibility = check_digit_possibility(tile, board, value)
        if digit_possibility:
            possible_values.append(str(value))
    if len(possible_values) == 1:
        return possible_values[0]
    else:
        return str(0)


# Checks adjacent tiles to see if the inputted solution is valid
def check_digit_possibility(tile, board, value):
    # Checks the location of every number on the board
    for num in board:
        # If the location of a number on the board matches the location of the tile
        if (num[1] == tile[1]) or (num[2] == tile[2]) or (num[3] == tile[3]):
            # If the value of the number matches the current number check
            if int(num[0]) == value:
                return False
    return True


# Parses the board list and outputs the completed sudoku puzzle
def print_board(board):
    output_row = ""
    for tile in board:
        output_row += (tile[0])
        if (int(tile[2]) % 9) == 0:
            print(output_row)
            output_row = ""


main()
