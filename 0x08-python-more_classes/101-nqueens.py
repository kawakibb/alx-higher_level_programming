#!/usr/bin/python3
"""Solves the N-queens puzzle.
Determines possible solutions to placing N
N non-attacking queens on NxN chessboard.
Example:
    $ ./101-nqueens.py N
N must be integer greater than orequal to 4.
Attributes:
    board (list): list of lists representing chessboard.
    solutions (list): list of lists containing solutions.
Solutions are represented in format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent row and column, respectively, where a
queen must be placed on chessboard.
"""
import sys


def init_board(n):
    """Initialize `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """Return deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """Return list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)


def xout(board, row, col):
    """X out spots on a chessboard.
    All spots where non-attacking queens can no
    longer be played are X-ed out.
    Args:
        board (list): current working chessboard.
        row (int): row where queen was last played.
        col (int): column where a queen was last played.
    """
    # X out all forward spots
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # X out all backwards spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # X out all spots below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # X out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    # X out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solve N-queens puzzle.
    Args:
        board (list): current working chessboard.
        row (int): current working row.
        queens (int): current number of placed queens.
        solutions (list): list of lists of solutions.
    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
