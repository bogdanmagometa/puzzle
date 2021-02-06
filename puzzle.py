"""
puzzle.py

Module for checking if the board is ready.
"""

def validate_board(board: list):
    """
    Check if a given board is ready.
    Return True if ready, False otherwise.

    >>> board = ["**** ****",
    ... "***1 ****",
    ... "**  3****",
    ... "* 4 1****",
    ... "     9 5 ",
    ... " 6  83  *",
    ... "3   1  **",
    ... "  8  2***",
    ... "  2  ****"]
    >>> validate_board(board)
    False
    """

    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()
