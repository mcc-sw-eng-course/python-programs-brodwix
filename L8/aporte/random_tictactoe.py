"""
Development Exercises - L8
Design a game to play Tic-Tac-Toe (Gato)
The interface could be text-based or graphical
The program should implement the logic to play against one human player
Add a test file explaining how you design the game
Be prepare to define classes for a future checkers game
"""

from random import randint

def drawBoard(board):
    # This function prints out the board that it was passed.
    # "board" is a list of 10 strings representing the board (ignore
    # index 0).
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def return_valid_moves(board):
    valid_moves = []
    for i in range(9):
        i += 1
        if board[i] == ' ':
            valid_moves.append(i)
    return valid_moves

def validate_move(board, move):
    valid_move = False
    if board[move] == ' ':
        valid_move = True
    return valid_move

def check_win(board, player):
    won = False
    if ((board[7] == player and board[8] == player and board[9] == player) or
        (board[4] == player and board[5] == player and board[6] == player) or
        (board[1] == player and board[2] == player and board[3] == player) or
        (board[7] == player and board[4] == player and board[1] == player) or
        (board[8] == player and board[5] == player and board[2] == player) or
        (board[9] == player and board[6] == player and board[3] == player) or
        (board[7] == player and board[5] == player and board[3] == player) or
        (board[9] == player and board[5] == player and board[1] == player)):
       won = True
    return won

def computer_move(board, computer_selection):
    moves = return_valid_moves(board)
    move = randint(0, len(moves)-1)
    board[moves[move]] = computer_selection

def game_is_tie(board):
    spaces = 0
    for i in range(9):
        i += 1
        if board[i] == ' ':
            spaces += 1

    if spaces == 0:
        print("Game is tie")
        return True
    else:
        return False

def main():
    player_wants_to_play = True
    board = [' ']*10

    print("Please select X or O: ")
    player_selection = input().upper()
    computer_selection = ''

    if player_selection == 'X':
        computer_selection = 'O'
    else:
        computer_selection = 'X'

    while player_wants_to_play:
        drawBoard(board)
        print("Please select your move: {0}".format(return_valid_moves(board)))
        player_move = input()
        player_move = int(player_move)
        if validate_move(board, player_move):
            board[player_move] = player_selection
        else:
            continue
        if check_win(board, player_selection):
            print("You Won")
            drawBoard(board)
            player_wants_to_play = False
            continue
        elif game_is_tie(board):
            player_wants_to_play = False
        computer_move(board, computer_selection)

        if check_win(board, computer_selection):
            print("Computer Won")
            drawBoard(board)
            player_wants_to_play = False
            continue
        elif game_is_tie(board):
            player_wants_to_play = False
    pass



if __name__ == '__main__':
    main()
    pass