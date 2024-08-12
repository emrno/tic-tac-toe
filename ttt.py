import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True

    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def player_move(board):
    while True:
        row = int(input("Enter the row (1-3): ")) - 1
        col = int(input("Enter the column (1-3): ")) - 1
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
            board[row][col] = 'X'
            break
        else:
            print("Invalid move. Try again.")

def robot_move_easy(board):
    while True:
        clear_screen()
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            board[row][col] = 'O'
            break

def robot_move_medium(board):
    clear_screen()
    for i in range(3):
        if board[i].count('O') == 2 and board[i].count(' ') == 1:
            board[i][board[i].index(' ')] = 'O'
            return

        column = [board[j][i] for j in range(3)]
        if column.count('O') == 2 and column.count(' ') == 1:
            board[column.index(' ')][i] = 'O'
            return

    if board[1][1] == 'O':
        if (board[0][0] == board[1][1] == 'O' and board[2][2] == ' ') or \
           (board[0][2] == board[1][1] == 'O' and board[2][0] == ' '):
            board[2][0 if board[0][2] == ' ' else 2] = 'O'
            return

    robot_move_easy(board)

def robot_move_intermediate(board):
    clear_screen()
    for i in range(3):
        if board[i].count('X') == 2 and board[i].count(' ') == 1:
            board[i][board[i].index(' ')] = 'O'
            return

        column = [board[j][i] for j in range(3)]
        if column.count('X') == 2 and column.count(' ') == 1:
            board[column.index(' ')][i] = 'O'
            return

    if board[1][1] == 'X':
        if (board[0][0] == board[1][1] == 'X' and board[2][2] == ' ') or \
           (board[0][2] == board[1][1] == 'X' and board[2][0] == ' '):
            board[2][0 if board[0][2] == ' ' else 2] = 'O'
            return

    robot_move_medium(board)

def robot_move_hard(board):
    clear_screen()
    best_score = -float('inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    board[best_move[0]][best_move[1]] = 'O'

def minimax(board, is_maximizing):
    if check_winner(board):
        return 1 if is_maximizing else -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def robot_move_impossible(board):
    clear_screen()
    if board[1][1] == ' ':
        board[1][1] = 'O'
        return

    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    random.shuffle(corners)
    for corner in corners:
        if board[corner[0]][corner[1]] == ' ':
            board[corner[0]][corner[1]] = 'O'
            return

    robot_move_medium(board)

def play_game():
    clear_screen()
    while True:
        print("Welcome to Tic Tac Toe!\n")
        print("Please select your difficulty:")
        print("[1] Easy")
        print("[2] Medium")
        print("[3] Intermediate")
        print("[4] Hard")
        print("[5] Impossible")
        difficulty_choice = input("Enter the number for your difficulty choice: ")

        if difficulty_choice == '1':
            robot_move = robot_move_easy
        elif difficulty_choice == '2':
            robot_move = robot_move_medium
        elif difficulty_choice == '3':
            robot_move = robot_move_intermediate
        elif difficulty_choice == '4':
            robot_move = robot_move_hard
        elif difficulty_choice == '5':
            robot_move = robot_move_impossible
        else:
            print("Invalid choice. Please select a number between 1 to 5 for difficulty.")
            continue

        board = [[' ' for _ in range(3)] for _ in range(3)]
        print_board(board)

        while True:
            player_move(board)
            print_board(board)
            if check_winner(board):
                print("Congratulations! You won!")
                break
            elif is_board_full(board):
                print("It's a tie!")
                break

            robot_move(board)
            print_board(board)
            if check_winner(board):
                print("The robot wins!")
                break
            elif is_board_full(board):
                print("It's a tie!")
                break

        play_again = input("Do you want to play again?\n[1] Yes\n[2] No: ").lower()
        if play_again != '1':
            break
            clear_screen()

if __name__ == "__main__":
    play_game()
