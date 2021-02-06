"""
puzzle.py

Module for checking if the board is ready.

Github repository:
https://github.com/bogdanmagometa/puzzle
"""

def validate_board(board: list) -> bool:
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


def check_uniqueness_in_rows(board: list) -> bool:
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


def check_row(row: str) -> bool:
    """
    Check if all the digits, which are greater than 0, in row are unique.
    Return True if unique, False otherwise.

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


def check_uniqueness_in_cols(board: list) -> bool:
    """
    Check if all the numbers in each column are unique within that column.
    Return True if unique, False otherwise.

    >>> board = ["**** ****",
    ... "***1 ****",
    ... "**  3****",
    ... "* 4 1****",
    ... "     9 5 ",
    ... " 6  83  *",
    ... "3   1  **",
    ... "  8  2***",
    ... "  2  ****"]
    >>> check_uniqueness_in_cols(board)
    False
    >>> board = [
    ... '12',
    ... '33']
    >>> check_uniqueness_in_cols(board)
    True
    >>> board = [
    ... '1**',
    ... '12*',
    ... '123']
    >>> check_uniqueness_in_cols(board)
    False
    """

    transposed_board = transpose_board(board)

    return check_uniqueness_in_rows(transposed_board)


def transpose_board(board: list) -> list:
    """
    Return transposed board so that each column becomes a row and each row becomes a column.

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


def check_uniqueness_colors(board: list) -> bool:
    """
    Check if the numbers of each color are unique withing that color.
    Return True if unique, False otherwise.

    >>> board = ["**** ****",
    ... "***1 ****",
    ... "**  3****",
    ... "* 4 1****",
    ... "     9 5 ",
    ... " 6  83  *",
    ... "3   1  **",
    ... "  8  2***",
    ... "  2  ****"]
    >>> check_uniqueness_colors(board)
    True
    """

    for pivot in zip(range(len(board)-1, -1, -1), range(len(board))):
        nums_set = set()
        for row_idx in range(pivot[0]):
            cur_num = board[row_idx][pivot[1]]
            if cur_num.isdigit() and cur_num != '0':
                if cur_num in nums_set:
                    return False
                nums_set.add(cur_num)

        for col_idx in range(pivot[1], len(board)):
            cur_num = board[pivot[0]][col_idx]
            if cur_num.isdigit() and cur_num != '0':
                if cur_num in nums_set:
                    return False
                nums_set.add(cur_num)

    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
