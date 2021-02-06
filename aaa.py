"""
This is module for skyscrapers.py program
"""

def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    >>> read_input("check.txt")
    ['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']
    """
    file = open(path, 'r')
    return [line.strip() for line in file.readlines()]


def left_to_right_check(input_line, pivot):
    """
    str, int -> bool
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    building_heights = input_line[1:-1]
    curr_visibility = 1
    max_visible_height = int(building_heights[0])
    for i in range(1, len(building_heights)):
        if int(building_heights[i]) > int(building_heights[i - 1]) and \
        int(building_heights[i]) > max_visible_height:
            curr_visibility += 1
    return curr_visibility == pivot
print(left_to_right_check("132354*", 3))

def check_not_finished_board(board):
    """
    list -> bool
    Check if skyscraper board is not finished, i.e., '?' present on the game board.
    Return True if finished, False otherwise.
    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', \
'*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', \
'*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', \
'*5?3215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    return '?' not in ''.join(board)


def check_uniqueness_in_rows(board):
    """
    list -> bool
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', \
'*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', \
'*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', \
'*553215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for row in board:
        heights = row[1:-1]
        heights = heights.replace('*', '')
        if len(set(heights)) != len(heights):
            return False
    return True


def check_horizontal_visibility(board):
    """
    list -> bool
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', \
'*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', \
'*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', \
'*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for row in board:
        if row[0]=='*' or left_to_right_check(row, int(row[0])):
            right_to_left = row[::-1]
        else:
            return False

        if right_to_left[0] == '*' or left_to_right_check(right_to_left, int(right_to_left[0])):
            continue
        else:
            return False
    return True


def check_columns(board):
    """
    list -> bool
    Check column-wise compliance of the board for uniqueness (buildings of
    unique height) and visibility (top-bottom and vice versa).
    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    size = len(board)
    turned_board = [''] * size

    for i in range(size):
        for j in range(size):
            turned_board[j] += board[i][j]

    if not check_uniqueness_in_rows(turned_board):
        return False

    return check_horizontal_visibility(turned_board)



def check_skyscrapers(input_path):
    """
    str -> bool
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.

    >>> check_skyscrapers("check.txt")
    True
    """
    game_board = read_input(input_path)
    if not check_horizontal_visibility(game_board) or \
        not check_uniqueness_in_rows(game_board) or \
            not check_not_finished_board(game_board) or \
                not check_columns(game_board):
                return False
    return True


if __name__ == "__main__":
    print(check_skyscrapers("check.txt"))
