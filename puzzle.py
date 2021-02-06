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

    return check_uniqueness_in_rows(board) and check_uniqueness_in_cols(board) and \
                                                                    check_uniqueness_colors(board)


def check_uniqueness_in_rows(board: list):
    """
    Check if all the numbers in each row are unique within that row.

    >>> board = ["**** ****",
    ... "***1 ****",
    ... "**  3****",
    ... "* 4 1****",
    ... "     9 5 ",
    ... " 6  83  *",
    ... "3   1  **",
    ... "  8  2***",
    ... "  2  ****"]
    >>> check_uniqueness_in_rows(board)
    True
    >>> board = [
    ... '12',
    ... '33']
    >>> check_uniqueness_in_rows(board)
    False
    >>> board = [
    ... '1**',
    ... '12*',
    ... '123']
    >>> check_uniqueness_in_rows(board)
    True
    """

    for row in board:
        if not check_row(row):
            return False

    return True


def check_row(row: str):
    """
    Check if all the digits, which are greater than 0, in row are unique.

    >>> check_row('3132')
    False
    >>> check_row('****')
    True
    >>> check_row('9')
    True
    >>> check_row('66')
    False
    >>> check_row('563784192')
    True
    """

    nums_set = set()

    for char in row:
        if char.isdigit() and char != '0':
            if char in nums_set:
                return False
            nums_set.add(char)

    return True


def check_uniqueness_in_cols(board: list):

    return False


def transpose_board(board: list):
    """
    Transpose a given board so that each column becomes a row and each row becomes a column.

    Precondition: a board has at least one row and one column.

    >>> transpose_board(['1'])
    ['1']
    >>> transpose_board(['12', '34'])
    ['13', '24']
    >>> transpose_board(['123', '456', '789'])
    ['147', '258', '369']
    >>> transpose_board(['22', '43', '10'])
    ['241', '230']
    """

    transposed_board = []

    for row in range(len(board[0])):
        transposed_board.append("")
        for column in board:
            transposed_board[-1] += column[row]

    return transposed_board

if __name__ == '__main__':
    import doctest
    doctest.testmod()
