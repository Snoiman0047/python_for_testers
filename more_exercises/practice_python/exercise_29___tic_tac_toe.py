"""
Exercise 29: Tic Tac Toe Game
(https://www.practicepython.org/exercise/2016/08/03/29-tic-tac-toe-game.html - question link)
"""
import random


def random_first_player():
    return 'X' if random.randint(0, 1) == 1 else 'O'


def display_winner(victory_tracking, _player):
    calc_player_wins(victory_tracking, _player)
    print('\nMatch Draw!') if _player == '_' else print(f"\nYeah we have a winner,\n"
                                                        f"Congratulations to player {_player} who won the game!\n")


def check_row_winner(_row):
    return _row[0] if _row[0] == _row[1] and _row[1] == _row[2] else '_'


def get_board_col(_board, col):
    return [_board[row][col] for row in range(3)]


def get_board_row(_board, row):
    return _board[row]


def winning_search(_board):
    board_slices = []

    # check rows and columns
    for index in range(3):
        board_slices.append(get_board_row(_board, index))
        board_slices.append(get_board_col(_board, index))

    # check diagonals
    down_diagonal = [_board[index][index] for index in range(3)]
    up_diagonal = [_board[0][2], _board[1][1], _board[2][0]]
    board_slices.append(down_diagonal)
    board_slices.append(up_diagonal)

    for _ in board_slices:
        _winner = check_row_winner(board_slices)
        if _winner != '_':
            return _winner
    return _winner


def init_board_game():
    return [['_', '_', '_'] for x in range(3)]


def display_board(_board):
    print()
    for _row in _board:
        for _col in _row:
            print(_col, end=' ')
        print()


def add_piece_in_game_board(_board, _player, _row, _column):
    _board[_row][_column] = _player
    return _board


def check_spot_empty(_game, _row, _column):
    return _game[_row][_column] == '_'


def convert_spot_to_coordinate(spot):
    return spot - 1


def switch_player(_player):
    return 'X' if _player == 'O' else 'O'


def moves_exist(_game):
    for row_num in range(3):
        for col_num in range(3):
            if _game[row_num][col_num] == '_':
                return True
    return False


def more_game():
    more = input('\n\nCome on, streaming with me on another game? ')
    return True if more.lower() == 'y' or more.lower() == 'yes' else False


def game_result(victory_tracking):
    games = victory_tracking["X"] + victory_tracking["O"] + victory_tracking["_"]
    print(f'\n\nPlayer X has won in {victory_tracking["X"]} games out of {games}.\n'
          f'Player O has won in {victory_tracking["O"]} games out of {games}.\n'
          f'Match draw: {victory_tracking["_"]}')


def calc_player_wins(victory_tracking, player):
    match player:
        case 'X':
            victory_tracking['X'] += 1
        case 'O':
            victory_tracking['O'] += 1
        case _:
            victory_tracking['_'] += 1


def start_play(victory_tracking):
    board = init_board_game()
    player = random_first_player()
    winner = '_'
    display_board(board)

    while winner == '_' and moves_exist(board):
        player = switch_player(player)
        print(f"\nPlayer {player} turn\n")
        row, column, available = None, None, False
        while not available:
            row = convert_spot_to_coordinate(int(input('row to spot? ')))
            column = convert_spot_to_coordinate(int(input('column to spot? ')))
            available = check_spot_empty(board, row, column)
        board = add_piece_in_game_board(board, player, row, column)
        display_board(board)
        winner = winning_search(board)
    display_winner(victory_tracking, winner)
    if more_game():
        start_play(victory_tracking)
    else:
        game_result(victory_tracking)


start_play({'O': 0, 'X': 0, '_': 0})
