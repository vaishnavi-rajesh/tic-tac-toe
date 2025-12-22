# Tic Tac Toe - Console Based (Python)

# Function to display the board
def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

# Function to check if a player has won
def check_winner(board, player):
    winning_combinations = [
        (0,1,2), (3,4,5), (6,7,8),   # rows
        (0,3,6), (1,4,7), (2,5,8),   # columns
        (0,4,8), (2,4,6)             # diagonals
    ]

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to check for a draw
def check_draw(board):
    return ' ' not in board

# Main game function
def tic_tac_toe():
    board = [' '] * 9
    current_player = 'X'

    print("Welcome to Tic Tac Toe!")
    print("Player X goes first.")
    print("Choose positions from 1 to 9.")

    while True:
        print_board(board)

        # Take input
        try:
            move = int(input(f"Player {current_player}, enter position (1-9): ")) - 1
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        # Validate input
        if move < 0 or move > 8:
            print("Position must be between 1 and 9.")
            continue
        if board[move] != ' ':
            print("Position already taken. Choose another.")
            continue

        # Update board
        board[move] = current_player

        # Check winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        # Check draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!!")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
tic_tac_toe()
