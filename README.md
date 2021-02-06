# puzzle

### Project for checking if the board in puzzle game is ready.

<br>

<b>puzzle</b> project provides <a href="https://github.com/bogdanmagometa/puzzle/blob/main/puzzle.py">puzzle.py</a> module containing function validate_board(board). To check whether the puzzle is ready for the game, import and invoke validate_board function with the argument (list of strings) representing the board.

The board is considered valid iff all of the following conditions are satisfied:
<ul>
<li>Each group of cells of the same color on the board has unique numbers (digits between 1 and 9)</li>
<li>Each row of the board has unique numbers (digits between 1 and 9)</li>
<li>Each column of the board has unique numbers (digits between 1 and 9)</li>
</ul>
