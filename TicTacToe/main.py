import os

def display_board(board):
    os.system('cls')
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def player_input():
    while True:
        try:
            choice = int(input("Enter a position (1-9): ")) - 1
            if choice in range(9):
                return choice
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def do_move(board, marker, position):
    if board[position] == ' ':
        board[position] = marker
        return True
    else:
        print("Position already taken. Try again.")
        return False
    
def check_win(board, marker):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in win_combinations:
        if all(board[i] == marker for i in combo):
            return True
    return False

def check_draw(board):
    return all(space != ' ' for space in board)

def replay():
    return input("Do you want to play again? (y/n): ").lower().startswith('y')

def choose_marker():
    while True:
        while True:
            marker = input("Player 1, do you want to be X or O? ").upper()
            if marker in ['X', 'O']:
                return marker, 'O' if marker == 'X' else 'X'
            else:
                print("Invalid choice. Please choose X or O.")

def main():
    print("Welcome to Tic Tac Toe!")
    while True:
        # Initialize the board
        board = [' '] * 9
        player1_marker, player2_marker = choose_marker()
        game_on = True
        turn = 'Player 1'

        while game_on:
            display_board(board)
            print(f"{turn}'s turn.")
            position = player_input()

            if board[position] == ' ':
                marker = player1_marker if turn == 'Player 1' else player2_marker
                do_move(board, marker, position)

                if check_win(board, marker):
                    display_board(board)
                    print(f"Congratulations! {turn} wins!")
                    game_on = False
                elif check_draw(board):
                    display_board(board)
                    print("It's a tie!")
                    game_on = False
                else:
                    turn = 'Player 2' if turn == 'Player 1' else 'Player 1'
            else:
                print("Position already taken. Choose another.")

        if not replay():
            print("Thanks for playing!")
            break

main()