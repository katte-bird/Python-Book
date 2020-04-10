# 09.04.2020
# tic-tac-toe
# a computer plays tic-tac-toe against a user


# global constants
X = "X"
O = "O"
EMPTY = " "     # represents an empty field on the game board
TIE = "TIE"     # represents the state of a draw
NUM_SQUARES = 9 # represents the number of fields on the board


def display_instruct():
    """Displays instructions for a player"""
    print(
        """
        Welcome to the ring of the grandest intellectual competition of all time. 
        Your brain and my processor will converge in a battle at the board of the game "Tic-Tac-Toe." 
        To make a move, enter a number from O to 8. The numbers correspond uniquely to the fields
        boards - as shown below:

        0 | 1 | 2
        --------
        3 | 4 | 5
        --------
        6 | 7 | 8

        Get ready for battle, human. The decisive battle is about to begin.
        \n
        """
        )


def ask_yes_no(question):
    """Ask a yes or no question"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Asks to enter a number within a range"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def who_starts():
    """Determine if player or computer goes first"""
    go_first = ask_yes_no("Do you require the first move? (y/n): ")
    if go_first == "y":
        print("\nThen take the first move. You will need it")
        human = X    
        computer = O     
    else:
        print("\nI will go first")
        computer = X     
        human = O    
    return computer, human


def new_board():
    """Create a new game board"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """Displays the game board on the screen"""
    print("\n\t", board[0], "|", board[1], "|", board[2]) 
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5]) 
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")


def legal_moves(board):
    """Creates a list of available moves"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """Determines the winner of the game"""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 4, 8),
                   (2, 4, 6),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8))
    for row in WAYS_TO_WIN: # loop iterates each row in WAYS_TO_WIN
                            # if all three are equal and not empty, 
                            # the winner is equal to symbol filling the squares

        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board: # if there are no empty squares on the board
            return TIE
    return None


def human_move(board, human):
    """Get human move"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nThat square is already occupied. Choose another\n")
    print("Fine...")
    return move


def computer_move(board, computer, human):
    """Get computer move"""
    # сcreate a working copy of the board,
    # because the function will change some values in the list
    board = board[ : ]

    # squares from best to worst
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print("I will take square number", end=" ")

    # if computer can win, take that move
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # checked this move cancel it
        board[move] = EMPTY

    # if human can win, block that move    
    for move in legal_moves(board):
        board[move]= human
        if winner(board) == human:
            print(move)
            return move
        # checked this move cancel it
        board[move] = EMPTY

    # since no one can win on next move, pick best open square
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


def next_turn(turn):
    """Switch turns"""
    if turn == X:
        return O
    else:
        return X # This function is used to alternate moves as players make them


def congrat_winner(the_winner, computer, human):
    """Congratulates the winner of the game"""
    if the_winner != TIE:
        print(the_winner, "won!\n")
    else:
        print("It's a tie!\n")

    if the_winner == computer:
        print("As I predicted, human, I am triumphant once more.\n"\
              "Proof that computers are superior to humans in all regards")
    
    elif the_winner == human:
        print("No, no! It cannot be! Somehow you tricked me, human.\n" \
              "But never again! I, the computer, so swear it!")
    
    elif the_winner == TIE:
        print("You were most lucky, human, and somehow managed to tie me.\n" \
              "Celebrate today... for this is the best you will ever achieve.")


def main():
    display_instruct()
    computer, human = who_starts()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

# start the program
main()

input("\nPress the enter key to quit...")
