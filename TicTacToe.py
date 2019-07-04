# game board
board = ["-","-","-","-","-","-","-","-","-",]

# If game is still going
game_still_going = True

# Who won? or Tie!
winner = None

# Who's turn it is?
current_player = "x"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    # Display board
    display_board()

    while game_still_going:
        handle_turn(current_player)
        check_if_game_is_over()
        flip_player()

    #Game ended
    if winner == "x" or winner == "o":
        print(winner + " won!")
    elif winner == None:
        print("Tie...")
    


def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1 to 9: ")

    valid = False
    while not valid:
        # checks for invalid syntax
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "q", "quit", "Quit"]:
            position = input("Choose a position from 1 to 9: ")

        if position == "q" or position == "quit" or position == "Quit":
            exit()

        position = int(position) - 1

        # checks for rewriting in the board
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there go again..")

    board[position] = player
    display_board()


def check_if_game_is_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagonals_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonals_winner:
        winner = diagonals_winner
    else:
        winner = None

    return

def check_rows():
    global game_still_going

    # All row should equal but not contain "-"
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False

    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return

def check_columns():
    global game_still_going

    # All row should equal but not contain "-"
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False

    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]
    return

def check_diagonals():
    global game_still_going

    # All row should equal but not contain "-"
    daigonals_1 = board[0] == board[4] == board[8] != "-"
    daigonals_2 = board[6] == board[4] == board[2] != "-"

    if daigonals_1 or daigonals_2:
        game_still_going = False

    if daigonals_1:
        return board[0]
    if daigonals_2:
        return board[6]
    return

def check_if_tie():
    global game_still_going

    if "-" not in board:
        game_still_going = False
    return

def flip_player():
    global current_player

    if current_player == "x":
        current_player = "o"
    elif current_player == "o":
        current_player = "x"
    return


play_game()

    
