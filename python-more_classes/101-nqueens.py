#!/usr/bin/python3
"""Solves the N queens puzzle using backtracking."""
import sys


def parse_args():
    """Validate command line arguments and return N.

    Exits with status 1 and prints an error message on invalid input.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n


def is_safe(board, row, col):
    """Check if a queen can be placed at (row, col).

    Args:
        board (list): List where board[i] is the column of the queen
            placed in row i (for rows already filled).
        row (int): The row to check.
        col (int): The column to check.

    Returns:
        bool: True if placing a queen at (row, col) is safe.
    """
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve(n):
    """Find and print all solutions to the N queens puzzle.

    Args:
        n (int): The size of the board and number of queens.
    """
    board = [-1] * n

    def backtrack(row):
        if row == n:
            solution = [[i, board[i]] for i in range(n)]
            print(solution)
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)


if __name__ == "__main__":
    N = parse_args()
    solve(N)
