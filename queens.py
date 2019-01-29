def main(num_queens):
    board = [['-'] * num_queens] * num_queens
    for line in board:
        print(board)

def check_valid(board):
    pass

def print_board(board):
    for row in board:
        line = '|'
        for cell in row:
            line = line + ' ' + cell + ' |'
        print(line)

main(4)
