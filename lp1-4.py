# Import necessary modules from the tkinter library
import tkinter as tk
from tkinter import messagebox

#  to check if a player has won the game
def is_winner(board, player):
    # Checking for both row and column winners
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    # Checking diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# to check if the game board is full
def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

# Class representing the Tic-Tac-Toe application
class TicTacToeApp:
    def __init__(self):
        # Initialize the main Tkinter window
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        # Initialize the game board and current player
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

        # Create a 3x3 grid of buttons for the Tic-Tac-Toe board
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                # Create a button for each cell on the board , comand = lambda row=i,col=j :self.on_button-click helps perform a function when the button is clicked 
                self.buttons[i][j] = tk.Button(text='_', font=('normal', 20), width=2, height=2,
                                              command=lambda row=i, col=j: self.on_button_click(row, col))
                # Place the button in the grid
                self.buttons[i][j].grid(row=i, column=j)

    # Callback function for button clicks
    def on_button_click(self, row, col):
        # when button is clicked 
        if self.board[row][col] == ' ':
            # Update the board and button text with the current player's symbol
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, state=tk.DISABLED)

            # Check for a winner or a tie
            if is_winner(self.board, self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()#reset thr board for the next match 
                
            elif is_board_full(self.board):
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                # Switch to the other player for the next turn
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    # Function to reset the game
    def reset_game(self):
        # Reset the game board and enable buttons for a new game
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ' '
                self.buttons[i][j].config(text='_', state=tk.NORMAL)

    # Function to run the Tkinter main loop which helps to create the window
    def run(self):
        self.root.mainloop()

# Create an instance of the TicTacToeApp class and run the game
if __name__ == "__main__":
    TicTacToeApp().run()