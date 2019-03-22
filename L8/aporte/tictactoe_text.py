"""
Development Exercises - L8
Text version of Tic Tac Toe Game
"""

from random import randint
from tictactoe_board import tictactoe_board

def get_player_selection():
    letter = ''
    while not (letter =='X' or letter == 'O'):
        print("Please select X or O: ")
        letter = input().upper()
    return letter

def get_random_turn():
    if randint(0, 1) == 0:
        return 'ai'
    else:
        return 'player'

def main():

    player_wants_to_play = True

    while player_wants_to_play:

        player_selection = get_player_selection() # player can select X or O

        board = tictactoe_board(player_selection)

        playing = True

        turn = get_random_turn() # select who will go first

        while playing:

            if turn == 'player':
                board.draw_board() # draw the board

                # ask for the player move
                valid_moves = board.get_valid_moves()
                print("Please select your move: {0}".format(valid_moves))
                player_move = input()
                player_move = int(player_move)

                if player_move in valid_moves:
                    board.do_player_move(player_move)
                else:
                    continue

                if board.player_won(): # PLayer won
                    board.draw_board()
                    print("You Won")   # Notify the player
                    playing = False
                    break
                elif board.tied():      # Game is tied
                    board.draw_board()
                    print("Game is a tie")
                    playing = False
                    break
                else:
                    turn = 'ai'         # no win nor tie, ai is next
            else:
                board.do_ai_move()      # select ai move

                if board.ai_won():      # AI won
                    board.draw_board()
                    print("AI Won")   # Notify the Player
                    playing = False
                    break
                elif board.tied():
                    board.draw_board()
                    print("Game is a tie")
                    playing = False
                    break
                else:
                    turn = 'player'     # no win nor tie, player is next

        print("Play Again (y/n)?")   # Game is over, ask if he wants to play again
        if not input().lower().startswith('y'):
            player_wants_to_play = False

if __name__ == '__main__':
    main()
    pass