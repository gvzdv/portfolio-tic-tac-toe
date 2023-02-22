import os


# Clear screen for a new game
def clear():
    os.system("clear")


# Game mechanics
def play_game():
    board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
    print("Available spaces: \n'top-L', 'top-M', 'top-R'\n'mid-L', 'mid-M', 'mid-R'\n'low-L', 'low-M', 'low-R'")
    playing = True
    turn = 'X'
    count = 0
    while playing:
        print_board(board)
        move = input(f'Turn for {turn}. Move on which space?\n')
        board[move] = turn
        count += 1
        # Checking if someone has won makes sense between 5 and 9 turns
        if 5 <= count < 9:
            playing = game_over(board=board, turn=turn)
        if count == 9:
            print("It's a tie!")
            playing = False
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


# Check if someone has won by comparing rows and columns
def game_over(board, turn):
    # Top row
    if board['top-L'] == board['top-M'] == board['top-R'] != " ":
        print_board(board)
        print("Game over!")
        print(f"{turn} won")
        return False
    # Middle row
    if board['mid-L'] == board['mid-M'] == board['mid-R'] != " ":
        print_board(board)
        print("Game over!")
        print(f"{turn} won")
        return False
    # Lower row
    if board['low-L'] == board['low-M'] == board['low-R'] != " ":
        print_board(board)
        print("Game over!")
        print(f"{turn} won")
        return False
    # Left column
    if board['top-L'] == board['mid-L'] == board['low-L'] != " ":
        print_board(board)
        print("Game over!")
        print(f"{turn} won")
        return False
    # Middle column
    if board['top-M'] == board['mid-M'] == board['low-M'] != " ":
        print_board(board)
        print("Game over!")
        print(f"{turn} won")
        return False
    # Right column
    if board['top-R'] == board['mid-R'] == board['low-R'] != " ":
        print_board(board)
        print("Game over!")
        print(f"{turn} won")
        return False
    # Diagonal
    if board['top-L'] == board['mid-M'] == board['low-R'] != " ":
        print_board(board)
        print("Game over!")
        print(f"{turn} won")
        return False
    # Another diagonal
    if board['top-R'] == board['mid-M'] == board['low-L'] != " ":
        print_board(board)
        print("Game over!")
        print(f"{turn} won")
        return False


# Initialize/rerun the game
while input("Do you want to play a game of Tic-Tac-Toe? \nType 'Y' or 'N': ") == "Y":
    clear()
    play_game()
