def main():
    board = board_init()
    board_incomplete = True
    while board_incomplete:
        board_incomplete = solve_board(board)
    print_board(board)


def board_init():
    board = []
    print("Please type each row of the sudoku board, with '0' in place of unknown numbers.")
    for row in range(1, 10):
        column = 1
        print("Row ", row, ": ", sep="", end="")
        usr_input = input()
        for num in usr_input:
            num_info = board_filler(num, row, column)
            board.append(num_info)
            column += 1
    return board


def board_filler(digit, row, column):
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
    return [digit, row, column, square]


def solve_board(board):
    solved_tiles = 0
    for tile in board:
        if tile[0] == "0":
            solved_tile = solve_tile(tile, board)
            if solved_tile != "0":
                tile[0] = solved_tile
                print(tile)
                solved_tiles += 1
    if solved_tiles > 0:
        return True
    else:
        return False


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


def check_digit_possibility(tile, board, value):
    # Checks the location of every number on the board
    for num in board:
        # If the location of a number on the board matches the location of the tile
        if (num[1] == tile[1]) or (num[2] == tile[2]) or (num[3] == tile[3]):
            # If the value of the number matches the current number check
            if int(num[0]) == value:
                return False
    return True


def print_board(board):
    output_row = ""
    for tile in board:
        output_row += (tile[0])
        if (int(tile[2]) % 9) == 0:
            print(output_row)
            output_row = ""


main()
