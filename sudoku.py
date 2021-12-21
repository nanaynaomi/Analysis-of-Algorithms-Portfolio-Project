# Naomi Grant
# CS 325 - Analysis of Algorithms
# November 2020

def create_board():
    """ Returns a dictionary where the keys represent the rows and columns (ex: A6 is row 1, column 6)
        and the values are initialized to '_' but will later be filled with numbers.
        Represents an empty Sudoku board."""
    board = {}
    for letter in "ABCDEFGHI":
        for num in "123456789":
            board[letter + num] = '_'
    return board


def fill_board(difficulty):
    """ Takes difficulty level chosen by the user (easy, medium, or hard), and returns the board
        with the starting numbers on it, along with the list of which boxes are pre-filled."""
    board = create_board()
    boxes = []
    nums = []
    if difficulty == "easy":
        boxes = ["A2", "A4", "A6", "B2", "B3", "B4", "B7", "C1", "C2", "C4",
                 "C7", "C8", "D2", "D3", "D5", "D7", "E1", "E3", "E7", "E9",
                 "F3", "F5", "F7", "F8", "G2", "G3", "G6", "G8", "G9", "H3",
                 "H6", "H7", "H8", "I4", "I6", "I8"]
        nums = [8, 9, 3, 9, 7, 6, 5, 4, 6, 5, 8, 9, 3, 2, 7, 9, 7, 8, 2, 1,
                4, 5, 3, 6, 7, 6, 2, 1, 9, 3, 6, 7, 5, 7, 5, 3]
    elif difficulty == "medium":
        boxes = ["A4", "A7", "A9", "B2", "B6", "B9", "C1", "C2", "C3", "D4",
                 "D5", "D9", "E1", "E3", "E7", "E9", "F5", "F6", "G7", "G8",
                 "G9", "H1", "H4", "H8", "I1", "I3", "I6"]
        nums = [6, 1, 4, 2, 1, 9, 4, 1, 3, 9, 6, 1, 6, 1, 8, 7, 7, 3, 9, 5,
                3, 3, 5, 2, 9, 7, 2]
    elif difficulty == "hard":
        boxes = ["A3", "A5", "A7", "B1", "B4", "B6", "B9", "C2", "C3", "C7",
                 "C8", "D4", "D6", "E2", "E8", "F4", "F6", "G2", "G3", "G7",
                 "G8", "H1", "H4", "H6", "H9", "I3", "I5", "I7"]
        nums = [3, 2, 9, 7, 9, 3, 8, 8, 6, 4, 3, 3, 6, 3, 1, 4, 2, 1, 7, 8,
                9, 8, 5, 1, 3, 4, 3, 6]
    elif difficulty == "test":   # Graders - enter "test" for the difficulty to use this board.
        boxes = []               # You can change the numbers as needed
        nums = [6, 7, 8, 9, 4, 2, 3, 1, 5,   # This makes it easier to check that it's working,
                1, 9, 3, 5, 8, 6, 4, 7, 2,   # rather than manually entering one value at a time.
                5, 4, 2, 1, 7, 3, 6, 9, 8,
                7, 5, 1, 2, 3, 9, 8, 6, 4,
                3, 6, 9, 8, 5, 4, 7, 2, 1,
                8, 2, 4, 7, 6, 1, 5, 3, 9,
                2, 8, 5, 3, 1, 7, 9, 4, 6,
                9, 3, 6, 4, 2, 8, 1, 5, 7,
                4, 1, 7, 6, 9, 5, 2, 8, 3]
        for letter in "ABCDEFGHI":
            for num in "123456789":
                boxes.append(letter+num)
    # Puts the pre-filled numbers on the board (in the dictionary)
    for i in range(len(boxes)):
        board[boxes[i]] = str(nums[i])
    return board, boxes


def print_board(board, pre_filled):
    """ Prints the Sudoku board to be viewed by the player."""
    print("  1 2 3   4 5 6   7 8 9")
    for key, value in board.items():
        if "1" in key:
            print(key[0], end=" ")
        if key not in pre_filled:
            print('\033[1m' + value, end=" ")
            print('\033[0m', end="")
        else:
            print(value, end=" ")
        if "9" in key:
            print("\n", end="")
            if key in "C9F9":
                print("  ------|-------|------")
        elif "3" in key or "6" in key:
            print("", end="| ")


def clear_board(board, pre_filled):
    """ Resets board so that it contains only the pre-filled input."""
    for key in board.keys():
        if key not in pre_filled:
            board[key] = '_'


def user_play():
    """ Allows the Sudoku game to be played by the user. Takes user input and interacts with user."""
    print("~~~~~ SUDOKU ~~~~~")
    print_rules()

    level = input("Choose a difficulty level (easy, medium, hard): ")
    while level.lower() not in ["easy", "medium", "hard", "test"]:
        level = input("Invalid input. Please enter either Easy, Medium, or Hard: ")
    print("Here is your " + level + " Sudoku Board:")
    board, pre_filled = fill_board(level)
    print_board(board, pre_filled)

    quit_game = False
    while not quit_game:
        print("")
        print("Reminder: Enter 'q' to quit, 'submit' when done, 'solution' to give up and"
              "\n see the fully solved board, or 'help' to see the instructions again.")
        square_num = input("Enter square name and number: ")
        square, num = handle_input(square_num, pre_filled)
        if square == 0:
            quit_game = True
        elif square == 1:
            if verify(board):
                print("Good job! You solved it correctly!")
            else:
                print("Sorry, your solution is incorrect.")
            quit_game = True
        elif square == 2:
            print("Here is the solution:")
            clear_board(board, pre_filled)
            solver(board)
            print_board(board, pre_filled)
            quit_game = True
        else:
            board[square] = num
            print("Updated Board:")
            print_board(board, pre_filled)


def handle_input(user_in, pre_filled):
    """ Takes user input and the list of which boxes are pre-filled.
        Makes sure user enters valid input. If user enters 'q', 'submit', or 'solution',
        different numbers are returned to represent codes of what to do in those instances.
        Otherwise returns the square (key) and the number (value) for the dictionary board."""
    while user_in != 'q' and user_in != 'submit' and user_in != 'solution':
        if user_in == 'help':
            print_rules()
        elif len(user_in) != 4:
            print("Invalid input. Example of valid input: 'A7 3'")
        else:
            square = user_in[0].upper() + user_in[1]
            num = user_in[3]
            if square in pre_filled:
                print("Pre-filled squares cannot be changed.")
            elif square[0] not in "ABCDEFGHI" or square[1] not in "123456789":
                print("That is not a valid square. Some examples: A6, E3, D4, etc.")
            elif num not in "123456789_":
                print("Invalid number. Must be between 1-9, or '_' to make it blank.")
            else:
                return square, num
        user_in = input("Enter square name and number: ")
    check = input("Are you sure? (Y/N): ")
    if check.upper() == 'Y':
        if user_in == 'q':
            return 0, 0
        elif user_in == 'submit':
            return 1, 1
        else:
            return 2, 2
    else:
        user_in = input("Enter square name and number: ")
        square, num = handle_input(user_in, pre_filled)
        return square, num


def print_rules():
    """ Prints the Sudoku rules and playing instructions."""
    print("Game Rules: The 9x9 board is divided into 9 larger squares (each with 9 squares inside). "
          "\nThe goal is to get the numbers 1-9 in each big square. \nEach number can only appear "
          "once in a row, column, or big square.")
    print("")
    print("Playing Instructions: \nUse the letters on the left and numbers on the top of the board"
          " to see the names of the squares (Ex: A6, G2, etc.). \nTo enter a number into a square,"
          " you enter the square name and the number you wish to put there, separated by a space. "
          "\nFor example, 'A4 3' would put a '3' in spot 'A4'. \nTo make the spot empty again, just put"
          " an underscore in place of a number: 'A4 _'")
    print("")


def verify(board):
    """ Checks the user's game solution.
        Returns True if they did it right, and False otherwise."""
    rows = 'ABCDEFGHI'
    cols = '123456789'
    nums_seen = ""

    # Check rows and columns
    if not rows_cols(board, rows, cols, nums_seen, True):
        return False

    # Check 3x3 squares
    for rows in ('ABC', 'DEF', 'GHI'):
        for cols in ('123', '456', '789'):
            if not rows_cols(board, rows, cols, nums_seen, False):
                return False
            nums_seen = ""

    return True


def rows_cols(board, rows, cols, nums_seen, checking_rows_cols):
    """ This is a helper function for verify(board).
        board: game board dictionary
        rows and cols: 'ABCDEFGHI' and '123456789'
        nums_seen: a list of numbers already seen in that row/column/box
        checking_rows_cols: True - checking rows and columns, False - checking 3x3 box
        Returns True if the user's input is correct so far, and False otherwise"""

    # Check each row
    for row in rows:
        for col in cols:
            if board[row + col] not in nums_seen:
                nums_seen += board[row + col]
            else:
                return False
        if checking_rows_cols:
            nums_seen = ''

    # Check each column - this part doesn't run when checking 3x3 squares
    if checking_rows_cols:
        for col in cols:
            nums_seen = ''
            for row in rows:
                if board[row + col] not in nums_seen:
                    nums_seen += board[row + col]
                else:
                    return False
    return True


def blank_square(board):
    """ Finds unfilled (blank) squares on the board."""
    for key, value in board.items():
        if value == '_':
            return key
    return None


def solver(board):
    """ Recursively finds a solution to the Sudoku board by checking if numbers work in each
        empty box and backtracking.
        Returns True if a solution has been found, and False otherwise."""
    square = blank_square(board)
    if not blank_square(board):
        return True
    for number in "123456789":
        if checker(board, number, square):
            board[square] = number
            if solver(board):
                return True
            board[square] = '_'
    return False

def checker(board, num, key):
    row = key[0] # A, B, C, etc.
    col = key[1] # 1, 2, 3, etc.
    rows = "ABCDEFGHI"
    cols = "123456789"
    # Check if the number matches another square in its row
    for c in cols:
        if board[row + c] == num and col != c:
            return False
    # Check if the number matches another square in its column
    for r in rows:
        if board[r + col] == num and row != r:
            return False
    # Check if the number matches another square in its 3x3 box
    box_rows, box_cols = "", ""
    for r_box in ['ABC', 'DEF', 'GHI']:
        if row in r_box:
            box_rows = r_box
    for c_box in ['123', '456', '789']:
        if col in c_box:
            box_cols = c_box
    for r in box_rows:
        for c in box_cols:
            if board[r+c] == num and r + c != key:
                return False
    return True


user_play()
