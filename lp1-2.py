#2nd variation - ramdom entry 
# the basic flow of this code is such that first the usesr inputs then the 
import random
#used to print the board 
def print_board(board):
    for row in board:
        print(" | ".join(row))
       
#used to check for the winner .Takes board and the current player to compare
def is_winner(board, player):
    #check if the player wins by vertical and horizontal stike 
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    #check for diagonal strikes 
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    #return ture if a player wins 
    return False
    #return false if its a draw or the entry is not complete

def is_board_full(board):
    #all() is used to return true or false value 
    return all(all(cell != ' ' for cell in row) for row in board)

def get_empty_cells(board):
    #returs the list of all the empty slots in the board which is then used by the fuction get_computer_move
    for i in range(3) :
        for j in range(3) :
            if board[i][j] == ' ':
                 return [(i, j)]

def get_player_move(board):
    while True:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if board[row][col] == ' ':
                return row, col
            else:
                print("Cell already occupied. Try again.")
        
# to get the slot where the computer/second player will occupie
def get_computer_move(board):
    #here empty_cell is the list containing all the empty slots of the board
    empty_cells = get_empty_cells(board)
    #out of the list of vacent slot we choose one in random using the random pacage 
    return random.choice(empty_cells)

def play_tic_tac_toe():
    #creating the 3*3 board for the game 
    board = [[' ' for _ in range(3)] for _ in range(3)]
    
    # loop is matinatin untill a winner is diclare or all the slots are occupied in the board
    while True:
        print_board(board)

        # Player's turn - using get_player_move which retuns 2 values i and j
        player_row, player_col = get_player_move(board)
        #player_row=i   player_col=j
        board[player_row][player_col] = 'X'

        #check for the winner 
        if is_winner(board, 'X'):
            print_board(board)
            print("Congratulations! You win!")
            break
            #exixt the while loop as x has won
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
            #exixt the while loop as its a draw

        # Computer's turn-- using get_computer_move which retuns 2 values i and j
        print("\nComputer's turn:")
        computer_row, computer_col = get_computer_move(board)
        #computer_row=i        computer_col=j
        board[computer_row][computer_col] = 'O'

        #check for winner 
        if is_winner(board, 'O'):
            print_board(board)
            print("Oops! You lose. Better luck next time!")
            break
            #exixt the while loop as o has won
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
            #exixt the while loop as its a draw
            
            
            
if __name__ == "__main__":
    play_tic_tac_toe()
