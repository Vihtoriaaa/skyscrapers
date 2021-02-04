This project contains one module -  skyscrapers.py and it is a program for
working with the board used for skyscrapers game and checking its correctness.

There are 7 functions:
- read_input(path) - reads the game board file from path and returns list of str.

- left_to_right_check(input_line, pivot) - checks row-wise visibility from
left to right. Returns True if number of building from the left-most hint is
visible looking to the right, False otherwise.

- check_not_finished_board(board) - Checks if skyscraper board is not finished, 
i.e., '?' present on the game board. Returns True if finished, False otherwise.

- check_uniqueness_in_rows(board) - Check buildings of unique height in each row.
Return True if buildings in a row have unique length, False otherwise.

- check_horizontal_visibility(board) - Checks row-wise visibility (left-right
and vice versa). Returns True if all horizontal hints are satisfiable, i.e.,
for line 412453* , hint is 4, and 1245 are the four buildings that could be
observed from the hint looking to the right.

- check_columns(board) - Checks column-wise compliance of the board for
uniqueness (buildings of unique height) and visibility (top-bottom and vice
versa). Same as for horizontal cases, but aggregated in one function for
vertical case, i.e. columns.

- check_skyscrapers(input_path) - Main function to check the status of skyscraper game board. Return True if the board status is compliant with the rules, False otherwise.