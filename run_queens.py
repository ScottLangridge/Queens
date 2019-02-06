import math

from solvers.simple_backtracking import simple_generate_solution
from time import time


def main():
    i = 221
    while True:
        print('Finding solution to', i, 'queens!')
        start = time()
        if i < 10:
            write_board('solutions/00' + str(i) + 'queens.csv',
                    simple_generate_solution(i, 99999))
        elif i < 100:
            write_board('solutions/0' + str(i) + 'queens.csv',
                    simple_generate_solution(i, 99999 ))
        else:
            write_board('solutions/' + str(i) + 'queens.csv',
                    simple_generate_solution(i,
                        99999))
        add_to_log(i, time() - start)
        i += 1
    

# Average time for a given number of runs and board size
def avg_time(queens, runs):
    times = []
    for run in range(runs):
        print('Run', run + 1, 'of', runs)
        times.append(time_solution(queens))

    mean = sum(times) / len(times)
    sd = math.sqrt(sum((i - mean) ** 2 for i in times) / len(times))

    print('\nAverage Time:', mean)
    print('Standard Dev:', sd)


# Run it once and return how long it took
def time_solution(queens):
    start = time()
    simple_generate_solution(queens)
    return time() - start


# Print a board to the terminal
def print_board(board):
    print('+' + '---+' * len(board))
    for row in board:
        line = '|'
        for cell in row:
            line = line + ' ' + cell + ' |'
        print(line)
        print('+' + '---+' * len(board))


# Write a board to CSV
def write_board(filename, board):
    out = ''
    for row in board:
        for val in row:
            out = out + val + ','
        out = out[:-1] + '\n'

    with open(filename, 'w') as f:
        f.write(out)


# Add the time taken to the log file
def add_to_log(queens, time):
    with open('solutions/time-log.txt', 'a') as f:
        f.write(str(queens) + ': ' + str(time) + '\n')


main()
