import math

from solvers.simple_backtracking import generate_solution
from time import time


def main():
    avg_time(32, 10)


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
    generate_solution(queens)
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


main()
