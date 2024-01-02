#3rd variation--- pvp 
# Define a function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))


# Define a function to check for a winner in the Tic-Tac-Toe game
def check_winner(board):
    # Check rows and columns for a win
    for i in range(3):
        if all(board[i][j] != ' ' for j in range(3)):
            return board[i][0]  # Return the player symbol if a row is filled
        if all(board[j][i] != ' ' for j in range(3)):
            return board[0][i]  # Return the player symbol if a column is filled

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]  # Return the player symbol if the main diagonal is filled
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]  # Return the player symbol if the other diagonal is filled

    return None  # Return None if no winner is found


# Define a function to check if the Tic-Tac-Toe board is full
def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False  # Return False if there's an empty cell, indicating the board is not full
    return True  # Return True if all cells are filled, indicating a tie


# Define the main Tic-Tac-Toe game function
def tic_tac_toe():
    # Initialize an empty Tic-Tac-Toe board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'  # Set the starting player to 'X'

    while True:
        print_board(board)  # Print the current state of the board

        # Get the player's move (row and column)
        row = int(input(f"Player {current_player}, enter row (0, 1, 2): "))
        col = int(input(f"Player {current_player}, enter column (0, 1, 2): "))

        # Check if the chosen position is valid and not already taken
        if board[row][col] == ' ':
            board[row][col] = current_player  # Place the player's symbol on the board
        else:
            print("That position is already taken!")
            continue  # Ask the player to choose another position if the chosen one is already taken

        # Check if there is a winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break  # End the game if a winner is found

        # Check if the board is full (a tie)
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break  # End the game if the board is full

        # Switch to the other player for the next turn
        current_player = 'O' if current_player == 'X' else 'X'

# Call the main Tic-Tac-Toe game function
tic_tac_toe()
