import random
from time import time


def simple_generate_solution(num_queens, max_run_time):
    start_time = time()
    board = create_board(num_queens)
    cands = create_cands(num_queens)

    row = 0
    while row < num_queens:
        while True:
            if time() - start_time > max_run_time:
                return simple_generate_solution(num_queens, max_run_time * 2)
            
            if len(cands[row]) == 0:
                cands[row] = list(range(num_queens))
                row -= 1
                board[row] = ['-'] * num_queens
                break

            guessed_x = random.choice(cands[row])
            cands[row].remove(guessed_x)
            board[row][guessed_x] = 'Q'

            if solution_valid(board, row):
                row += 1
                break
            else:
                board[row][guessed_x] = '-'

    return board


def create_board(num_queens):
    board = []
    for i in range(num_queens):
        board.append([])
        for j in range(num_queens):
            board[-1].append('-')
    return board


def create_cands(num_queens):
    cands = []
    for i in range(num_queens):
        cands.append([])
        for j in range(num_queens):
            cands[-1].append(j)
    return cands


def solution_valid(board, latest_row):
    for x in range(len(board)):
        if board[latest_row][x] == 'Q':
            if not queen_valid((x, latest_row), board):
                return False

    return True


def queen_valid(coord, board):
    start_x = coord[0]
    start_y = coord[1]

    for x in range(len(board)):
        if board[start_y][x] == 'Q' and x != start_x:
            return False

    for y in range(len(board)):
        if board[y][start_x] == 'Q' and y != start_y:
            return False

    x = start_x + 1
    y = start_y + 1
    while x < len(board) and y < len(board):
        if board[y][x] == 'Q':
            return False
        x += 1
        y += 1

    x = start_x - 1
    y = start_y - 1
    while x >= 0 and y >= 0:
        if board[y][x] == 'Q':
            return False
        x -= 1
        y -= 1

    x = start_x - 1
    y = start_y + 1
    while x >= 0 and y < len(board):
        if board[y][x] == 'Q':
            return False
        x -= 1
        y += 1

    x = start_x + 1
    y = start_y - 1
    while x < len(board) and y >= 0:
        if board[y][x] == 'Q':
            return False
        x += 1
        y -= 1

    return True


def print_board(board):
    print('+' + '---+' * len(board))
    for row in board:
        line = '|'
        for cell in row:
            line = line + ' ' + cell + ' |'
        print(line)
        print('+' + '---+' * len(board))
