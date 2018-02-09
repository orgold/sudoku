import csv
import sys
import math

EMPTY_CELL = 0
BLOCK_SIZE = 3
BOARD_SIZE = BLOCK_SIZE**2


def find_missing_cells(board):
    return [(i, j) for j in range(len(board[0])) for i in range(len(board)) if not board[i][j]]


def numerize_line(line):
    ''' make numeric line from characters' line.
    :param line: the line of chars
    :return:     line of ints, replace empty slots with 0
    '''
    return [(int(c) if c else EMPTY_CELL) for c in line]


def numerize_board(board):
    return [numerize_line(line) for line in board]


def is_valid_in_list(l, value):
    return not value in l


def get_block_indices(idx):
    return [i for i in range(BOARD_SIZE) if i//BLOCK_SIZE == idx//BLOCK_SIZE]


def is_valid_in_row(board, row_idx, value):
    return is_valid_in_list(board[row_idx], value)


def is_valid_in_col(board, col_idx, value):
    col = [line[col_idx] for line in board]
    return is_valid_in_list(col, value)


def is_valid_in_block(board, row_idx, col_idx, value):
    block_row_indices = get_block_indices(row_idx)
    block_col_indices = get_block_indices(col_idx)
    block = [board[i][j] for i in block_row_indices for j in block_col_indices]
    return is_valid_in_list(block, value)


def is_valid_in_board(board, row_idx, col_idx, value):
    return is_valid_in_row(board, row_idx, value) and\
           is_valid_in_col(board, col_idx, value) and\
           is_valid_in_block(board, row_idx, col_idx, value)


def rec_solve(board, missing_cells, curr_i):
    if curr_i == len(missing_cells):
        return True
    row_idx, col_idx = missing_cells[curr_i]
    for curr_val in range(1, BOARD_SIZE+1):
        if is_valid_in_board(board, row_idx, col_idx, curr_val):
            board[row_idx][col_idx] = curr_val
            if rec_solve(board, missing_cells, curr_i + 1):
                return True
    board[row_idx][col_idx] = 0
    return False


def main(args):
    with open(args[0]) as f:
        reader = csv.reader(f.readlines())
        board = [r for r in reader]
    missing_cells = find_missing_cells(board)
    num_board = numerize_board(board)  # from text to int
    solved = rec_solve(num_board, missing_cells, 0)
    if not solved:
        print("couldn't solve it")
    else:
        for i, j in missing_cells:
            print('{},{} -> {}'.format(i+1, j+1, num_board[i][j]))


if __name__ == '__main__':
    main(sys.argv[1:])
