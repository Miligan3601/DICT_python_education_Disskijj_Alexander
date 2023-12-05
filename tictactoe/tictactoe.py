def print_game_board(board):
    print('---------')
    for row in board:
        print('|', ' '.join(row), '|')
    print('---------')

def create_game_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def game_state(board):
    rows = board
    cols = [[board[j][i] for j in range(3)] for i in range(3)]
    diagonals = [[board[i][i] for i in range(3)], [board[i][2 - i] for i in range(3)]]

    x_wins = any(all(cell == 'X' for cell in line) for line in rows + cols + diagonals)
    o_wins = any(all(cell == 'O' for cell in line) for line in rows + cols + diagonals)

    if x_wins:
        return 'X wins'
    elif o_wins:
        return 'O wins'
    elif any(' ' in row for row in board):
        return 'Game not finished'
    else:
        return 'Draw'

def user_move(board, player):
    while True:
        try:
            coordinates = input("Enter the coordinates: ").split()
            x, y = map(int, coordinates)

            if x < 1 or x > 3 or y < 1 or y > 3:
                print("Coordinates should be from 1 to 3!")
                continue

            if board[3 - y][x - 1] != ' ':
                print("This cell is occupied! Choose another one!")
                continue

            board[3 - y][x - 1] = player
            break

        except ValueError:
            print("You should enter numbers!")
        except IndexError:
            print("Coordinates should be from 1 to 3!")

def tic_tac_toe_game():
    board = create_game_board()
    print_game_board(board)
    current_player = 'X'

    while True:
        user_move(board, current_player)
        print_game_board(board)
        game_result = game_state(board)

        if game_result != 'Game not finished':
            print(game_result)
            break

        current_player = 'O' if current_player == 'X' else 'X'

tic_tac_toe_game()
